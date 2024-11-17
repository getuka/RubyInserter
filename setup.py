from setuptools import setup, find_packages

setup(
    name='rubyinserter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "mecab-python3",
        "pykakasi",
    ],
    description='A library to insert Ruby text for Japanese.',
    url='https://github.com/getuka/RubyInserter.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
