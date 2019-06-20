========
Overview
========

.. image:: https://secure.travis-ci.org/benpankow/semidbm.png?branch=master
   :target: http://travis-ci.org/benpankow/semidbm


Semidbm is a fast, pure python implementation of a dbm, which is a
persistent key value store. This fork includes a fix for read-only mode. In
the original fork, read only mode will still attempt to create the data
directory if it does not exist, may write headers, and uses read and write flags.
