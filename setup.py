from setuptools import setup, find_packages

setup(
    name='text_based_hangman',
    version='1.0',
    packages=find_packages(),
    author='Your Name',  # Replace with your actual name
    author_email='your.email@example.com',  # Replace with your actual email
    description='A simple text-based hangman game',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/text_based_hangman',  # Replace with your actual GitHub URL
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        # Add any dependencies here if needed
    ],
    entry_points={
        'console_scripts': [
            'hangman=main:main',
        ],
    },
)