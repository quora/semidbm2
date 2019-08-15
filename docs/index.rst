Semidbm
=======

Semidbm is a fast, pure python implementation of a dbm, which is a
persistent key value store. It allows you to get and set keys through
a dict interface::

    import semidbm2
    db = semidbm2.open('testdb', 'c')
    db['foo'] = 'bar'
    print db['foo']
    db.close()

These values are persisted to disk, and you can later retrieve
these key/value pairs::

    # Then at a later time:
    db = semidbm2.open('testdb', 'r')
    # prints "bar"
    print db['foo']


It was written with these things in mind:

* Pure python, supporting python 2.6, 2.7, 3.4, 3.6 and 3.7.
* Cross platform, works on Windows, Linux, Mac OS X.
* Supports CPython, pypy, and jython (versions 2.7-b3 and higher).
* Simple and Fast (See :doc:`benchmarks`).


Post feedback and issues on
`github issues <https://github.com/quora/semidbm2/issues>`_, or check out the
latest changes at the `github repo <https://github.com/quora/semidbm2>`_.


Topics
------

.. toctree::
    :maxdepth: 2

    overview
    details
    benchmarks
    changelog


Developer Documentation
-----------------------

.. toctree::
    :maxdepth: 2

    api_semidbm2
    fileformat


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

