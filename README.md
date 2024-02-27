# Python_course

# CLI Utilities Homework

## Author

Renzo Flores Ugarte Флорес Угарте Рензо

## Introduction

This repository contains my implementations of simplified versions of the Unix utilities `nl`, `tail`, and `wc` as part of my homework assignments. These scripts are written in Python and designed to replicate some of the basic functionalities of their original counterparts.

## Homework Assignments

### 1. Simplified `nl` Utility (`simplified_nl.py`)

This script outputs the contents of a file or stdin, with each line numbered. It mimics the basic functionality of the `nl` command.

#### Usage

To run the script with a file:

```bash
python simplified_nl.py <file_name>
```
For stdin input:

```bash
cat <file_name> | python simplified_nl.py
```
###2. Simplified tail Utility (simplified_tail.py)
A Python script that replicates the basic functionality of the tail command, outputting the last 10 lines of each input file or the last 17 lines from stdin if no file is specified.

Usage
To run the script with files:

```bash
python simplified_tail.py <file1> <file2> 
```
For stdin input:

```bash
cat | python simplified_tail.py
```

###3. Simplified wc Utility (simplified_wc.py)
This script functions similarly to the wc command, providing a count of lines, words, and characters for each input file or stdin input.

Usage
To run the script with files:

```bash
python simplified_wc.py <file1> <file2> ...
```
For stdin input:

```bash
cat | python simplified_wc.py
```
Testing
Each script has been thoroughly tested with various inputs to ensure accuracy and reliability. Test outputs and examples are provided in the artifacts directory for reference.

Requirements
No external libraries are required to run these scripts. They are compatible with Python 3.x.

Conclusion
I hope these implementations serve as a useful demonstration of my ability to replicate fundamental Unix utility functionalities in Python. Feedback and suggestions for improvement are always welcome.
