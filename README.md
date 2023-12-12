# Muncher
A python package for data analytics.<br />
[Package Main Website](https://github.com/ShaoPG47/DS5010_Project.git)

## Description
Muncher is a package that provides importing, merging, manipulation, and exporting.
It also supports data visualization and statistical analysis.

## Installation
Currently, Muncher can be installed by downloading the source code directly. Future versions may be available via pip.

## Usage

### 1. importer
importer is a tool for reading in .csv files without using any external packages,
it contains certain functions that can help users to understand some basic informations of the 
dataset.

#### Load in csv file
```py
from muncher import importer as imp

df = imp("your_csv_file.csv")
df.readCsv()
```

#### Data Visualization
```py
df.table() #Convert data set to a table with row index and column index
df.colnames #Prints out column names
df.header #Print out the begining of the data set as table with default length of 5 rows
```
#### Accessing Data
```py
df[i,j] #Access the element on the ith row and jth column
df['column_name'] #Access the elements under "column name"
```
#### Data handling
```py
df.addrow() #Add a row
df.droprow() #Drop a row
df.addcol() #Add a column
df.dropcol() #Drop a column by index or column name
df.dropna() #Drop all rows with NA values
```

### 2. merger
merger is a tool for multiple data merging, it helps user to understand 
which pair of importer type data sets in the the data sets list has common columns and it's name.

#### Create the data set list
```py
from muncher import importer as imp
from muncher import merger as meg
df1 = imp("your_csv_file.csv")
df2 = imp("your_csv_file.csv")
df1.readCsv()
df2.readCsv()

df_list = [df1,df2]
```
#### Merging
```py
meg_list = meg(df_list)
meg_list.commonCols() #Returns the common column names of each pair in the data list
meg_list.merge([i,j], key) #left merge the ith and jth element in data list by key
```

### 3. Manipulation


### 4. Utilities


### 5. Exporter


## Known Issues
1. importer.table() function would not work if there is NA values in data set <br />


## Authors
#### Anqi Guo
Contact Info: [guoanqi57@gmail.com](guoanqi57@gmail.com) <br />
Main Contributions: 

#### Zhenan Zhuang
Contact Info: [z28964713@gmail.com](z28964713@gmail.com) <br />
Main Contributions: 

#### Zuoming Zhang
Contact Info: [zhang.zu@northeastern.edu](zhang.zu@northeastern.edu) <br />
Main Contributions: 

#### Pengli Shao
Contact Info: [shao.pe@northeastern.edu](shao.pe@northeastern.edu) <br />
Main Contributions: muncher.importer, muncher.merger

## Reference


