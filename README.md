[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) 
[![status workflow test](https://github.com/guangrei/Gitpybinding/actions/workflows/python-app.yml/badge.svg)](https://github.com/guangrei/Gitpybinding/actions) 

[![Downloads](https://static.pepy.tech/badge/gitbinding)](https://pepy.tech/project/gitbinding) [![Downloads](https://static.pepy.tech/badge/gitbinding/month)](https://pepy.tech/project/gitbinding) [![Downloads](https://static.pepy.tech/badge/gitbinding/week)](https://pepy.tech/project/gitbinding)

Fully git command binding for Python.

Features:

🔥 support any git commands, git command with "-" can be replaced with "_" like `git rev-parse` to `git.rev_parse()`.

🔥 support prompt input with `git.prompt = "value"`.

🔥 auto change path to clone destination.

🔥 custom git binary location `git.gitbin = "path/to/git/binary"`.

🔥 support direct output to stdout or capture output to function return.

🔥 raise exception on non-zero exit code.

🔥 compatible with `mypy --strict`.

## Example

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
Now you can run any git command like `git.init()`, `git.clone("gitrepo", "destination")`, `git.commit()`, `git.push()`, `git.config()` etc.

author: Guangrei.
