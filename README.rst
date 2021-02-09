imgflip
=========
A python api to imgflip.


Install
-------
::

  pip install imgflip


How to use?
-----------
::

  python -m imgflip.cli
  python -m imgflip
  imgflip


Development
-----------
setup::

  python -m pip install --upgrade pip wheel setuptools coverage pytest flake8 pylint twine
  python -m pip install -e .

run tests::

  python -m coverage run --branch --source imgflip -m pytest
  coverage report -m

check src::


  python -m flake8 imgflip
  python -m pylint --rcfile=setup.cfg imgflip

check readme::

  python setup.py sdist
  twine check dist/*

make package::

  python setup.py sdist bdist_wheel
  python -m twine upload dist/*
