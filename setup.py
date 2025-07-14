# setup.py
from setuptools import setup, find_packages

setup(
    name="booknotes",
    version="0.1.4",
    description="Terminal-based note app for book lovers",
    author="Eren Öğrül",
    author_email="termapp@pm.me",
    url="https://github.com/bearenbey/book-notes",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'booknotes = book_notes.cli:run',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Environment :: Console :: Curses",
    ],
    python_requires='>=3.6',
)