labels: Draft
        Python
        SoftwareDevelopment
created: 2017-05-07T15:17
modified: 2017-05-07T15:17
place: Phuket, Thailand
comments: true

# Python project structure

[TOC]

## Project folder vs Source folder

`Project folder` - everything we have under version control, including `README`, `docs`, `setup.py`, etc.
`Source folder` - subfolder of the project folder, contains source code mainly.

Best practice is to keep `Project folder` == `Source folder`.

```
myproject
- myproject
-- __init__.py
-- file.py
- README.md
- setup.py
```

## Tests folder

`tests` project must be on the same level with the project modules, or inside each module. Not outside source folder.

Bad:
```
myproject
- myproject
-- mymodule1
-- mymodule2
- tests
```
It is bad because there may be another tests module in the python path or a local tests module. So `from tests import ...` may be a source of errors (`from myproject.tests import ...` is more reliable).

Good:
```
myproject
- myproject
-- mymodule1
-- mymodule2
-- tests
```

And tests per module is even better idea as we can distribute module together with tests.

## Code style guide enforcement

See [flake8](http://flake8.pycqa.org/en/latest/).

```
myproject
- .flake8
```
