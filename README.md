Fully git command binding for python, compatible with all git and python 2 & 3 version.

## Installation

```
pip3 install gitbinding
```

## Usage

```python
from gitbinding import Git

git = Git(path = None, direct_output = True)
"""
path:
working directory, None = use current directory.

direct_output:
if direct_output set to False, the output is redirect to command/function return.
"""
```
now you can run any git command like `git.init()`, `git.clone("gitrepo destination")`, `git.commit()`, `git.push()`,`git.config()` etc.

> git command with "-" can be replaced with "_" like git rev-parse to git.rev_parse()

you can also put git command argument in separate function args like `git.clone("gitrepo","destination")`.

> when git.clone() finished without error, the path will automatic move to clone destination.

## change git bin

to change git binary location, use:
```
git.gitbin = "path/to/git/binary"
```