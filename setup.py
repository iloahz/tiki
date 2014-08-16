from setuptools import setup, find_packages

setup(
    name='tiki',
    version='0.1',
    packages=find_packages(),
    package_data = {
        '': ['dict.txt', 'README.md']
    },
    url='https://github.com/iloahz/tiki',
    license='Creative Commons Attribution 4.0 International License.',
    author='iloahz',
    author_email='iloahz@gmail.com',
    description='Generate fancy names'
)
