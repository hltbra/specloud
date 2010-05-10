PyUnitBDD
=========

Use nosetests and plugins to take BDD specifications easier.


Installation
------------

You need any version of ``pinocchio`` greater than 0.1 first.
You can download and install it apart and then::

    $ easy_install pyunitbdd
    
    or

    $ pip install pyunitbdd

    
Or you can use pip and the requirements resource::
    
    $ pip install pyunitbdd -r http://github.com/hugobr/pyunitbdd/raw/master/requirements.txt 


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


    $ pyunitbdd example.py # it colorizes
    
    Py unit wrap example
    - ensure it pass
    - it should pass
    - must pass
    - should pass
    - pass
    
    ----------------------------------------------------------------------
    Ran 5 tests in 0.002s
    
    OK
