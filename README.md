# Ideal Pento Charto

Program allowing quick and easy data analysis, generating charts and so much more!

## Table of Contents

* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup and Usage](#setup-and-usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)

## General Information

Ideal Pento Charto can help you with analyzing data and especially creating multiple charts - straight from given data or with transformations such as derivatives.

## TL;DR

You throw your folder with files into the pento charto folder and run the 'main.py' from the terminal. The rest you can decipher from config.txt
By design your source files must have at least some kind of numbers separated by commas or dots in the first 20 lines of a file.

## Technologies Used

- Python version 3.4 and up
- NumPy 1.23.0
- Matplotlib 3.5.2
- Pandas 1.4.3
- Os for Python 3.9
- Glob for Python 3.9

## Features

- generate simple charts from given data
- calculate first and second derivative of given data
- generate first and second derivative charts
- editing data in specific column, eg. multiplying by constant

## Setup and Usage

Project works only for .txt documents for now.

1. Open Terminal and type:
`python3 main_code.py`
2. Drop the folder with all the project files in the directory with the folder with your
data.
3. Specify the folder name and columns from the files you want to use in the cofig file.
4. When you start the .py file, you will be presented with the list of files to be used.

Data are presented in order: 1st line - title, 2nd and up lines - analyzed data; 1st
column - X axis, 2nd and up columns - Y axis.

## Project Status

Project is: _in progress_.

## Room for Improvement

Room for improvement:

- Current code works for files that consists only of title and data just below it (in second
line). We are working on code that would work for all kinds of files, including those with
more text in first few lines.
- Adding more possible formats of data (not just .txt)

## Acknowledgements

Huge thanks to Asia Jędrzejewska-Szmek, who encouraged us to do the project and helped with
understanding how Python and Github work.
