# HEU

This repositories contains the script for comparing the data from two different groups given in different files.


# System Requirements

- Ubuntu Linux 18.04
- Python 3.6.8 | Anaconda
- Python modules
	- NumPy
	- SciPy
	- Pandas



## Instructions to use



```bash
cd src
python stats.py -d <csv_directory> -o <output_file.csv> -c <Binary Category Column> 
```


## Demo and Demo data





# System Requirements

## Hardware Requirements

Python script `stats.py` requires only a standard computer or laptop.

The runtimes will vary based on the data size. For our data, the runtime was less than 10 seconds.

## Software Requirements

### OS Requirements

Python script `stats.py` is supported for *Linux* operating systems. It has been tested on the following systems:

Linux: Ubuntu 18.04
Mac OSX:
Windows:


### Python and dependencies

Python 3.6.8
Pandas 0.24.2
Numpy 1.16.2
Scypy 1.2.1
Click 7.0

#### Installing dependencies

```bash
pip install numpy scipy pandas click
````

It will take about 2-3 minutes, depending on network speed.


#### Issue help

In case of any issue, please report us at [Issue](https://github.com/codemeleon/HEU/issues).


# Pseudocode

Input: A folder containing csv files having common column names and one binary categorical variable
Output: Statistical comparision of numerical variable based on catgorical variable.
Split numerical variable in two groups based on categorical variable
Check whether both groups are normally distributed (Shapiro-Wilk test)
if both group are nomally distributed
	apply t-test and provide mean and 95% confidence interval
else
	apply Mann-Whitney U test and provide median and inter quartile range.
summaries the results in table format

