# -*-coding:utf8;-*-
from typing import Optional, Tuple, Callable, Any
from anybinding import Bind
import os


class Git:
    def __init__(self, path: Optional[str] = None, direct_output: bool = True) -> None:
        if path is None:
            self.path = os.getcwd()
        else:
            if os.path.isdir(path):
                self.path = path
            else:
                raise IOError("path isn't exists!")

        self.git = Bind("git", direct_output=direct_output)
        self.prompt: Optional[str] = None
        self.gitbin = "git"

    def _update_path(self, args: Tuple[str]) -> None:
        if len(args) >= 2:
            p = args[1]
            self.path = os.path.join(self.path, p.strip())
        else:
            p = args[0]
            p = os.path.basename(p)
            if p.endswith(".git"):
                p = p[:-4]
            self.path = os.path.join(self.path, p.strip())

    def __getattr__(self, name: str) -> Callable[..., str]:
        def call_git(*args: Any, **kwargs: Any) -> str:
            self.git.path = self.path
            self.git.prompt = self.prompt
            self.git.bin = self.gitbin
            ret = getattr(self.git, name)(*args, **kwargs)
            if name == "clone":
                self._update_path(args)
            return str(ret)

        return call_git
