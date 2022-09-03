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

[Link](https://realpython.com/python-virtual-environments-a-primer/)

## GIT

Git is a distributed version control system
- Git stores information in the form of a list of file-based changes and changes made to each file over time.

- In projects where there are often lots of developers working in parallel, 
Git is essential to ensure there are no code conflicts between developers.

- Some of the benefits of Git:
   - Easy to use, fast, quick and safe operation.
   - Easily combine branches.
   - Just clone the source code from the repository or clone a modified version from the repository, 
   or a branch from the repository, and you can work anywhere.
   - Deployment your product easily.

### 1.1 Basic commands

This great GitHub commands cheat sheet saved my butt multiple times:
<https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet>

### 1.2 Basic Git flow
Check out the branch from the develop branch

Before checking out the branch you should pull the code back.
```
git pull
```
How to name the branch: id_task-description_task
```
git checkout "id_task-description_task"
```
After completing the assigned task, commit with the following syntax:
```
git commit -m "#id_task-description"
```

After committing, you push the code to the branch:
```
git push origin name_branch
```


![Basic git flow](images/basic_git_flow.jpg?raw=true "Css")

- Some important Git terms:
#### 1. Branch
- Branches represent specific instances of a repository separate from your main Project.
- Branch allows you to keep track of your changes to the repository, so you can roll back to earlier versions.

#### 2. Commit
- Commit represents a specific moment in your project history. Using the commit and git add commands keeps your changes saved to local repository.

#### 3. Checkout
- Use **git checkout** to switch between branches
    - git checkout "name-branch"
 
#### 4. Fetch
- The git fetch command fetches the copies and downloads all branches to your computer.

#### 5. Head
- Commits at the beginning of a branch are called Head. 
It represents the most recent commit of the repository you are working on.

#### 6.  Index
- Whenever you add, edit, delete, or change a file, it stays in the index until you're ready to commit.
  Use git status to see those changes (file index).

#### 7. Master
- Master is the main branch of your repository. It includes the most recent changes and commits.

#### 8. Merge
- The git merge command combines pull requests to add changes from branch to branch.

#### 9. Origin
- git push origin master => to push local changes to the main branch.

#### 10. Pull
- To pull all of the pushed code back to your branch
    - git pull

#### 11. Push
- The git push command is used to push the code to your branch.

#### 12. Rebase
- The git rebase command allows you to split, move, and exit a commit. It can also be used to combine two branches.

#### 13. Stash
- The git stash saves your local modifications away and reverts the working directory to match the HEAD commit. 

#### 14. Fetch
- The git fetch command downloads objects to the local machine without overwriting existing local code in the current branch. The command pulls a record of remote repository changes, allowing insight into progress history before adjustments

![Basic git commands](images/git_commands.jpg?raw=true "Css")

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

## Readability and maintainability: 

- Is the code readable as written?  
- Does it require additional comments, better naming, or general refactoring to be easily understood?  
- Does the code generally conform to the style of coding for the project?
- use code standard ([PEP8](https://www.zenesys.com/blog/python-coding-standards-best-practices))
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

