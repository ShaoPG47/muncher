# -*- coding: utf-8 -*-

def columnManipulation(dataset, column, manipulation_function):
    """
    Purpose: Manipulate a specific column in the dataset using a provided function.

    Parameters:
    dataset: The dataset to be manipulated.
    column: The name of the column to be manipulated.
    manipulation_function: The function to be applied to the column.
    """
    for i in range(len(dataset)):
        dataset[i][column] = manipulation_function(dataset[i][column])
    return dataset


def dataCleaning(dataset, missing_value_strategy='mean'):
    """
    Purpose: Handling missing values.

    Parameters:
    dataset: The dataset to be cleaned.
    missing_value_strategy (str, default 'mean'): The strategy to handle missing values.
      Possible values: 'mean', 'median', 'mode', 'remove' (remove rows with missing values).
    """
    cleaned_data = []
    columns = list(dataset[0].keys())

    for i, row in enumerate(dataset):
        cleaned_row = {}
        for column in columns:
            if column in row:
                value = row[column]

                if value is None or value == '':
                    if missing_value_strategy == 'mean':
                        values = [r[column] for r in dataset if column in r and r[column] not in (None, '')]
                        cleaned_row[column] = sum(values) / len(values) if values else None
                    elif missing_value_strategy == 'median':
                        values = sorted([r[column] for r in dataset if column in r and r[column] not in (None, '')])
                        cleaned_row[column] = values[len(values) // 2] if values else None
                    elif missing_value_strategy == 'mode':
                        values = [r[column] for r in dataset if column in r and r[column] not in (None, '')]
                        cleaned_row[column] = max(set(values), key=values.count) if values else None
                    elif missing_value_strategy == 'remove':
                        continue  # Skip rows with missing values
                else:
                    cleaned_row[column] = value

        cleaned_data.append(cleaned_row)

    return cleaned_data



def dataSelection(dataset, columns=None, rows=None):
    """
    Purpose: Select specific columns or rows from the dataset.

    Parameters:
    dataset: The dataset as a list of dictionaries.
    columns: List of column names to be selected.
    rows: List of row indices to be selected.
    """
    selected_data = []
    for i, row in enumerate(dataset):
        selected_row = {}
        if columns:
            selected_row.update({col: row[col] for col in columns if col in row})
        if rows is None or i in rows:
            selected_data.append(selected_row)
    return selected_data



def dataGroupBy(dataset, groupby_column, aggregation_functions):
    """
    Purpose: Group data by a specified column and apply aggregation functions.

    Parameters:
    dataset: The dataset.
    groupby_column: The column by which the data should be grouped.
    aggregation_functions: A dictionary where keys are column names and
      values are aggregation functions (e.g., 'sum', 'mean', 'max').
    """
    grouped_data = {}
    for row in dataset:
        group_key = row[groupby_column]
        if group_key not in grouped_data:
            grouped_data[group_key] = {}
        for column, agg_function in aggregation_functions.items():
            if column in row:
                if column not in grouped_data[group_key]:
                    grouped_data[group_key][column] = []

                # Handle non-iterable case
                if not isinstance(row[column], (list, tuple)):
                    row[column] = [row[column]]

                # Filter out None values before applying aggregation functions
                values = [value for value in row[column] if value is not None]
                if values:
                    grouped_data[group_key][column].extend(values)

    aggregated_data = []
    for group_key, group_data in grouped_data.items():
        aggregated_row = {groupby_column: group_key}
        for column, agg_function in aggregation_functions.items():
            if column in group_data:
                if agg_function == 'sum':
                    aggregated_row[column] = sum(group_data[column])
                elif agg_function == 'mean':
                    # Check for zero denominator
                    aggregated_row[column] = sum(group_data[column]) / len(group_data[column]) if len(group_data[column]) > 0 else None
                elif agg_function == 'max':
                    aggregated_row[column] = max(group_data[column])
                # Add more aggregation functions as needed
        aggregated_data.append(aggregated_row)

    return aggregated_data


import time

def dataSampling(dataset, fraction):
    """
    Purpose: Randomly sample a fraction of the dataset.

    Parameters:
    dataset: The dataset to be sampled.
    fraction: The fraction of the dataset to be sampled.
    """

    seed = int(time.time())
    dataset_copy = dataset.copy()

    sampled_data = []
    total_size = len(dataset_copy)
    sample_size = int(total_size * fraction)

    for _ in range(sample_size):
        index = seed % len(dataset_copy)
        sampled_data.append(dataset_copy.pop(index))
        seed += 1

    return sampled_data

def dataPivoting(dataset, pivot_column, value_column):
    """
    Purpose: Pivot the dataset based on specified columns.

    Parameters:
    dataset: The dataset as a list of dictionaries.
    pivot_column: The column whose unique values become new columns.
    value_column: The column whose values populate the new columns.
    """
    pivoted_data = {}
    for row in dataset:
        pivot_value = row[pivot_column]
        if pivot_value not in pivoted_data:
            pivoted_data[pivot_value] = {}
        pivoted_data[pivot_value] = row[value_column]
    return [{'pivot_column': key, 'value_column': value} for key, value in pivoted_data.items()]