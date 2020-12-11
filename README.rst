PyImgflip
=========
A python api to imgflip.


Install
-------
::

  pip install pyimgflip


How to use?
-----------
::

  python -m pyimgflip.cli


Development
-----------
setup::

  python -m pip install --upgrade pip wheel setuptools flake8 twine
  python -m pip install -e .

check src::

  flake8 pyimgflip

Check readme::

  python setup.py sdist
  twine check dist/*
