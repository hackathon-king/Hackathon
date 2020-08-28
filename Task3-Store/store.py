"""
2020.08.28
3) Backup all files in /Backup and databases and Store in a remote place.
    a. Use the python package os and re
"""

# #!/usr/bin/python3
# coding:utf-8

from git import Git


class GitHack(object):

    def __init__(self, working_dir=r".."):
        self.git = Git(working_dir)

    # show command and result
    @staticmethod
    def show(command, res):
        print(f"[ {command}]\n{res}")

    def branch(self, para=""):
        command = "git branch " + para
        res = self.git.execute(command)
        self.show(command, res)

    def status(self, para=""):
        command = "git status " + para
        res = self.git.execute(command)
        self.show(command, res)

    def add(self, para="--all"):
        command = "git add " + para
        res = self.git.execute(command)
        self.show(command, res)

    def commit(self, para=" -m ", comment=""):
        command = "git commit " + para + comment
        res = self.git.execute(command)
        self.show(command, res)

    def push(self, para=""):
        command = "git push " + para
        res = self.git.execute(command)
        self.show(command, res)

    # show log info
    def log(self, para=""):
        command = "git log " + para
        res = self.git.execute(command)
        self.show(command, res)


if __name__ == "__main__":
    # Create a object for GitHack with git
    git_hack = GitHack()

    # show current active branch and status
    git_hack.branch()
    git_hack.status()

    # add files
    git_hack.add()

    # input comment for committing
    print("commit comment: ", end="")
    comment = input()
    print(comment)
    git_hack.commit(comment=comment)

    # push codes to remote repository
    git_hack.push()

    # could show log
    git_hack.log()

