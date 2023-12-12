from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='LiDoS',
    version='0.1.1',
    description='A library for managing License keys with Google Sheets integration.',
    author='devwalker-cmyk',
    keywords=['License', 'Google Sheets', 'License Manager'],
    url='https://github.com/devwalker-cmyk/License-Docs-Sheets',
    long_description=read('README.md'),
    license='MIT',
    install_requires=[
        'requests',
        'bs4'
    ],
    packages=['LiDoS'],
    python_requires='>=3.6', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
