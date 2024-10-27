# Python in practice
<<<<<<< HEAD
LaTeX Tools
LaTeX Tools is a Python package that simplifies the generation of LaTeX documents. It provides functionality to automatically create tables and include images in your LaTeX documents, making it easier to incorporate data and visuals into your LaTeX projects.

Features
Generate LaTeX code for tables from Python lists.
Include images in your LaTeX documents with simple Python commands.
Installation
You can install LaTeX Tools directly from PyPI:

sh
Copy code
pip install latexgen-renzo-fu
Replace latexgen-renzo-fu with the actual name of your package on PyPI.

Usage
Creating a Table
To create a table in your LaTeX document, use the generate_latex_table function:

python
Copy code
from latex_tools import generate_latex_table

data = [
    ["Header 1", "Header 2", "Header 3"],
    ["Row 1, Cell 1", "Row 1, Cell 2", "Row 1, Cell 3"],
    ["Row 2, Cell 1", "Row 2, Cell 2", "Row 2, Cell 3"]
]

latex_code = generate_latex_table(data)
print(latex_code)
Including an Image
To include an image in your LaTeX document, use the generate_latex_image function:

python
Copy code
from latex_tools import generate_latex_image

image_code = generate_latex_image('path/to/your/image.png', 'Caption for the image', 'fig:image_label')
print(image_code)
Contributing
Contributions to LaTeX Tools are welcome! Please fork the repository and submit a pull request with your improvements.

License
LaTeX Tools is licensed under the MIT License. See the LICENSE file for more details.
=======

# CLI Utilities Homework

## Author

Renzo Flores Ugarte Флорес Угарте Рензо

## Introduction

This repository contains my implementations of simplified versions of the Unix utilities `nl`, `tail`, and `wc` as part of my homework assignments. These scripts are written in Python and designed to replicate some of the basic functionalities of their original counterparts.

## Pratical implementation

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
### 2. Simplified tail Utility (simplified_tail.py)
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

### 3. Simplified wc Utility (simplified_wc.py)
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
>>>>>>> 4cec58b411b5bd3f1db5cb6ed81b0f9c49240e88
