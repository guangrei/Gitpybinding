# -*-coding:utf8;-*-
"""
The MIT License (MIT)

Copyright (c) 2022 gitbinding https://github.com/guangrei/Gitpybinding

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from subprocess import Popen, PIPE
import os
import sys
import shlex


class Git(object):

    stdout = ""
    stderr = ""
    gitbin = "git"

    def __init__(self, path=None, direct_output=True):
        self.direct_output = direct_output
        if path is None:
            self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        else:
            if os.path.isdir(path):
                self.path = path
            else:
                raise IOError("path isn't exists!")

    def _evaluate(self, command):
        command = shlex.split(command)
        if self.direct_output:
            p = Popen(command, cwd=self.path)
            p.communicate()
            if p.poll() != 0:
                raise RuntimeError("exit code: {}".format(p.poll()))
        else:
            p = Popen(command, cwd=self.path, stdout=PIPE,
                      stderr=PIPE, universal_newlines=True)
            self.stdout, self.stderr = p.communicate()
            if p.poll() != 0:
                raise RuntimeError("{}".format(self.stderr))

    def _update_path(self, args):
        if len(args) >= 2:
            p = str(args[1])
            self.path = p.strip()
        else:
            p = str(args[0])
            p = p.split("/")
            p = p[-1]
            if p.endswith(".git"):
                p = p[:-3]
                self.path = p.strip()

    def __getattr__(self,
                    name):

        def call_git(*args):

            arg = " ".join([str(i) for i in args])
            command = "{0} {1} {2}".format(self.gitbin, name, arg)
            self._evaluate(command)
            if name == "clone":
                self._update_path(args)

        return call_git


if __name__ == "__main__":
    pass
