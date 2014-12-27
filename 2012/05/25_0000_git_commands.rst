Git commands
============

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2012/05/git.png
    :width: 400px
    :alt: Git SCM
    :align: left

Base
----

Get help:

.. code-block:: bash

    git help <command>
    git <command> --help
    man git-<command>

Set git user username and email:

.. code-block:: bash

    # globally (for current user)
    git config --global user.name "Some One"
    git config --global user.email "someone@mail.com"
    # locally (for current project)
    git config user.name "Some One"
    git config user.email "someone@mail.com"

Manage repositories
-------------------

Init:

.. code-block:: bash

    git init .
    git add main.c module.c
    git commit -a -m 'init'

Add remote repository:

.. code-block:: bash

    git remote add github git@github.com:username/project.git
    # or edit .git/config manually

Get information
---------------

View untracked files:

.. code-block:: bash

    git status

View file history:

.. code-block:: bash

    git log my_file

View commits differences:

.. code-block:: bash

    git diff xxxxxxx..xxxxxxx # xxxxxxx - commit hash
    git diff master..my_branch
    # current uncommited changes:
    git diff

Diff for specified user:

.. code-block:: bash

    git diff master..my_branch --author 'User Name'

View list of changed files:

.. code-block:: bash

    git diff --name-only master..some_branch
    git diff --name-only SHA1 SHA2
    git diff --name-only HEAD~10 HEAD~5

Show list of commits:

.. code-block:: bash

    git log
    # for user
    got log --author 'User Name'

Show file from specified revision:

.. code-block:: bash

    git show <treeish>:<file>
    git show HEAD~4:tests.py

Show changes history for specified line of code:

.. code-block:: bash

    git blame path/to/file -L <line number>

Branches
--------

Create new branch:

.. code-block:: bash

    git branch my_branch_name
    git checkout my_branch_name
    # or simpler:
    git checkout -b my_branch_name

Pull latest branch code from remote repository:

.. code-block:: bash

    git pull origin my_branch

Delete local branch:

.. code-block:: bash

    git branch -d the_local_branch

Delete remote branch:

.. code-block:: bash

    git push origin --delete branch_to_remove

Copy branch from origin:

.. code-block:: bash

    git fetch
    git checkout -b new_branch origin/new_branch

Merge branch:

.. code-block:: bash

    git commit -a -m 'some changes'
    git checkout master
    git merge my_branch --no-ff

Work with codebase
------------------

Push change to remote repository:

.. code-block:: bash

    # some changes
    git commit -a -m 'Something was changed'
    git push origin master

Move or delete files:

.. code-block:: bash

    git mv my_file.c new_name.c
    git rm my_file.c

Repair deleted files:

.. code-block:: bash

    git checkout deleted_file.c

Extend latest commit:

.. code-block:: bash

    # changes
    git commit -a -m 'Something was changed'
    git add some_new_file.c
    git commit -a --amend

Rollback last commit:

.. code-block:: bash

    git reset --hard HEAD^

Revert changes in one file:

.. code-block:: bash

    # upstream master
    git checkout origin/master -- filename
    # the version from the most recent commit
    git checkout HEAD -- filename
    # the version before the most recent commit
    git checkout HEAD^ -- filename

Copy commit from one branch to another (cherry-pick):

.. code-block:: bash

    git cherry-pick xxxxxxx # xxxxxxx - commit hash

Hide/restore not commited changes (stashing):

.. code-block:: bash

    # move uncommented changes to stack
    git stash
    # show the stack
    git stash list
    # restore latest stashed changes
    git stash apply


Links:
    - `Git SCM <http://git-scm.com/>`__

.. info::
    :tags: SCM, Git
    :place: Alchevs'k, Ukraine
