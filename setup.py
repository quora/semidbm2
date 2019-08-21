import os
from setuptools import setup, find_packages


setup(
    name="semidbm2",
    version="0.5.2",
    description="Cross platform (fast) DBM interface in python",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
    license="BSD",
    author="Quora, Inc.",
    author_email="asynq@quora.com",
    packages=find_packages(),
    zip_safe=False,
    keywords="semidbm, semidbm2, dbm",
    url="https://github.com/quora/semidbm2",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: Jython",
        "License :: OSI Approved :: BSD License",
    ],
)
