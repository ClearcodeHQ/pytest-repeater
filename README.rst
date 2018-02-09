pytest_repeater
===============

.. image:: https://pypip.in/v/pytest_repeater/badge.png
    :target: https://pypi.python.org/pypi/pytest_repeater/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/pytest_repeater/badge.png
    :target: https://pypi.python.org/pypi/pytest_repeater/
    :alt: Number of PyPI downloads

.. image:: https://pypip.in/wheel/pytest_repeater/badge.png
    :target: https://pypi.python.org/pypi/pytest_repeater/
    :alt: Wheel Status

.. image:: https://pypip.in/egg/pytest_repeater/badge.png
    :target: https://pypi.python.org/pypi/pytest_repeater/
    :alt: Egg Status

.. image:: https://pypip.in/license/pytest_repeater/badge.png
    :target: https://pypi.python.org/pypi/pytest_repeater/
    :alt: License

Package status
--------------

.. image:: https://travis-ci.org/ClearcodeHQ/pytest-repeater.svg?branch=v0.1.0
    :target: https://travis-ci.org/ClearcodeHQ/pytest-repeater
    :alt: Tests

.. image:: https://coveralls.io/repos/ClearcodeHQ/pytest-repeater/badge.png?branch=v0.1.0
    :target: https://coveralls.io/r/ClearcodeHQ/pytest-repeater?branch=v0.1.0
    :alt: Coverage Status

.. image:: https://requires.io/github/ClearcodeHQ/pytest-repeater/requirements.svg?tag=v0.1.0
     :target: https://requires.io/github/ClearcodeHQ/pytest-repeater/requirements/?tag=v0.1.0
     :alt: Requirements Status

python package template - to make easier for me to duplicate general package structure.


.. warning::

    This pytest plugin's development, has been stopped.
    Please use `pytest-repeat <https://pypi.python.org/pypi/pytest_repeat/>`_ instead.


History
-------

This package was created based on `thread from StackOverflow`_ about repeating py.test tests.

.. _thread from StackOverflow: http://stackoverflow.com/questions/21764473/how-can-i-repeat-each-test-multiple-times-in-a-py-test-run


Use case
--------

Track down heisenbug in **foo_test** by running it 50 times::

    py.test -k foo_test --repeat 50


Package resources
-----------------

* Bug tracker: https://github.com/ClearcodeHQ/pytest-repeater/issues



Travis-ci
---------

After creating package on github, move to tracis-ci.org, and turn on ci builds for given package.
