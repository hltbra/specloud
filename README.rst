PyUnitBDD
=========

Use nosetests and plugins to take BDD specifications easier.


Installation
------------

    $ easy_install pyunitbdd
    
    or

    $ pip install pyunitbdd



Usage
=====

Get a python file with BDD-like test names (starting with it, ensure, should, must) and add them to the test suite


For example::

    $ cat example.py
    import unittest


    class PyUnitWrapExample(unittest.TestCase):

        def it_should_pass(self):
            pass

        def ensure_it_pass(self):
            pass

        def should_pass(self):
            pass

        def must_pass(self):
            pass

        def test_pass(self):
            pass

    $ pyunitbdd  example.py
    .....
    ----------------------------------------------------------------------
    Ran 5 tests in 0.001s
    
    OK
    $ pyunitbdd  example.py --with-spec
    
    Py unit wrap example
    - ensure it pass
    - it should pass
    - must pass
    - should pass
    - pass
    
    ----------------------------------------------------------------------
    Ran 5 tests in 0.002s
    
    OK
    
    $ pyunitbdd  example.py --with-spec --spec-color # it colorizes
    
    Py unit wrap example
    - ensure it pass
    - it should pass
    - must pass
    - should pass
    - pass
    
    ----------------------------------------------------------------------
    Ran 5 tests in 0.002s
    
    OK
    
