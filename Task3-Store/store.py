"""
2020.08.28
3) Backup all files in /Backup and databases and Store in a remote place.
    a. Use the python package os and re
"""

# #!/usr/bin/python3
# coding:utf-8

from git import Repo


repo = Repo(r"..")
print(repo.active_branch)


print(repo.tags)

from git import Git
g = Git(r"..")


print(g.execute("git add --all"))
print(g.execute("git commit -m 'git'"))
print(g.execute("git log"))
