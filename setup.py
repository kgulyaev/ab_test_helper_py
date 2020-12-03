import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ab_test_helper",
    version = "0.0.1",
    author = "Kirill Guliaev",
    author_email = "k.gulyaev@municorn.com",
    description = "",
    license = "Apache 2",
    keywords = "",
    url = "https://github.com/kgulyaev/ab_test_helper_py",
    packages=['ab_test_helper'],
    install_requires=[
        "statsmodels",
        "bootstrapped"
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: Apache Software License",
    ],
)