========
Overview
========

.. image:: https://secure.travis-ci.org/quora/semidbm2.png?branch=master
   :target: http://travis-ci.org/quora/semidbm2


Semidbm is a fast, pure python implementation of a dbm, which is a
persistent key value store. This is a fork of https://github.com/jamesls/semidbm
which includes a fix for read-only mode. In the original fork, read only mode
will still attempt to create the data directory if it does not exist, may write
headers, and uses read and write flags.
