# Bookbot

**Bookbot** is a Python-based command-line tool designed to analyze the contents of text files (specifically books). It automates the tedious task of counting words and analyzing character frequency, providing a detailed report for any ```.txt``` file you provide.

## Features

- **Dynamic File Analysis:** No longer limited to a single hardcoded file. Analyze any book by passing its path as a command-line argument.
- **Word Counting:** Quickly determines the total number of words in a document.
- **Character Frequency:** Provides a breakdown of how many times each character appears (case-insensitive).
- **Error Handling:** Includes built-in validation to ensure the program is used correctly.

## Prerequisites

To run Bookbot, you need to have **Python 3** installed on your system.

## Setup

**1. Clone the repository:**

```Bash

git clone <your-repository-link>
cd bookbot

```

**2. Prepare your data:** Create a ```books/``` directory and download some text files to analyze. You can use the following commands to get started with the classics:

```Bash

mkdir books
wget -O books/mobydick.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/mobydick.txt
wget -O books/prideandprejudice.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/prideandprejudice.txt
wget -O books/frankenstein.txt https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt

```

## Usage

Run the script from your terminal by providing the path to a book file as the second argument:

```Bash

python3 main.py books/frankenstein.txt

```

### Argument Validation

If you forget to provide a file path, Bookbot will guide you on the correct usage:

```
Usage: python3 main.py <path_to_book>
```

## Example Output

When running ```python3 main.py books/frankenstein.txt```, you will see a report similar to this:

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============

```

***This project was built as part of the Boot.dev backend development curriculum.***

BookBot is my first [Boot.dev](https://www.boot.dev) project!
