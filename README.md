Fully git command binding for python, compatible with any git and python 3 version.

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
if direct_output set to False, output stdout/stderr assigned to git.stdout and git.stderr
"""
```
now you can run any git command like `git.init()`, `git.clone("gitrepo destination")`, `git.commit()`, `git.push()`,`git.config()` etc.

you can also put git command argument in separate function args like `git.clone("gitrepo","destination")`.

> when git.clone() finished without error, the path will automatic move to clone destination.

## change git bin

to change git binary location, use:
```
git.gitbin = "path/to/git/binary/"
```