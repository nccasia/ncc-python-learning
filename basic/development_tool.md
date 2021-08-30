## Install Python

For the vast majority of beginners, you can just do a default install of Python 3.8 from [python.org/downloads](https://python.org/downloads)

Once you have it downloaded, you can open a program called `Idle` in the Python 3.8 folder (aka directory). 

If you want more pro-level installation visit the following:

- [Mac setup](https://www.codingforentrepreneurs.com/blog/install-django-on-mac-or-linux)
- [Windows setup](https://www.codingforentrepreneurs.com/blog/install-python-django-on-windows)

## Pip

 - pipfile
 - pipfile.lock

## IDE

 - Visual Studio Code
 - Pycharm

## Virtual environment



## Working rules

- Make sure you understand the requirement
- When in doubt - don’t guess! Ask questions!
- Do research for solution and Ask questions!
- First make it work then make it pretty
- Embrace the unknown - Stay curious!
- Discuss with other developer if you change his code
- Keep commitment!
- Always test the code locally before submitting for review
- Write down document as much as possible


## Readability and maintainability: Is the code readable as written?  Does it require additional comments, better naming, or general refactoring to be easily understood?  Does the code generally conform to the style of coding for the project?
 - use code standard (PSR)
 - internal review before submitting
 - Names are simple and if possible short
 - Names are spelled correctly
 - No hardcoded constants that could possibly change in the future
 - There is no commented out code
 - Debugging code is absent
 
 
## Quality and expandability:
 - All variables are in the smallest scope possible
 - There is no dead code (inaccessible at Runtime)
 - No code that can be replaced with library functions
 - Variables are not accidentally used with null values
 - Code is not repeated or duplicated
 - No complex/long boolean expressions
 - No empty blocks of code
 - Ideal data structures are used
 - Catch clauses are fine-grained and catch specific exceptions. Exceptions are not eaten if caught unless explicitly documented otherwise
 - Blocks of code inside loops are as small as possible
 - Code is unit-testable and is covered at least 70%
 - each function contain a (very) brief comment describing functionality, inputs, and outputs
 - Design patterns if used are correctly applied
 - A class should have only a single responsibility
 - Many client-specific interfaces are better than one general-purpose interface
 - Depend upon Abstractions. Do not depend upon concretions


## Testing the Code

Tests are made using pytest framework.

You may add new tests for yourself by adding files and functions with test_ prefix (i.e. test_topic.py with def test_sub_topic() function inside).

To run all the tests please execute the following command from the project root folder:
```
pytest
```

To run specific tests please execute:
```
pytest ./path/to/the/test_file.py
```

## Linting the Code

Linting is done using [pylint](http://pylint.pycqa.org/) and [flake8](http://flake8.pycqa.org/en/latest/) libraries.

### PyLint

To check if the code is written with respect
to [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide please run:

```bash
pylint ./src/
```

In case if linter will detect error (i.e. `missing-docstring`) you may want to read more about 
specific error by running:

```bash
pylint --help-msg=missing-docstring
```

[More about PyLint](http://pylint.pycqa.org/)

### Flake8

To check if the code is written with respect
to [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide please run:

```bash
flake8 ./src
```

Or if you want to have more detailed output you may run:

```bash
flake8 ./src --statistics --show-source --count
```

[More about Flake8](http://flake8.pycqa.org/en/latest/)

