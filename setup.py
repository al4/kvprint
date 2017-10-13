""" kvprint

https://github.com/al4/kvprint
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


test_requirements = ['pytest']

setup(
    name='kvprint',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='Simple module for printing key-values aligned by separator',
    long_description=long_description,
    url='https://github.com/al4/kvprint',
    author='Alex Forbes',
    license='MIT',
    keywords='infrastructure',
    packages=find_packages(
        where='./src',
        exclude=['contrib', 'docs', 'tests', 'build', 'cert']
    ),
    package_dir={'': 'src'},
    install_requires=[
        'six',
    ],
    extras_require={
        'test': test_requirements,
    },
    tests_require=test_requirements,
    zip_safe=True,
)
