# Setup script for the hangman game

from setuptools import setup, find_packages

setup(
    name='text_based_hangman',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here if needed
    ],
    entry_points={
        'console_scripts': [
            'hangman=main:main',
        ],
    },
)