from setuptools import setup, find_packages

setup(
    name="bengsky-tools",
    version="0.1.0",
    packages=find_packages(),
    description="A set of useful tools by bengsky for ctf",
    author="Bambang (Bengsky) Priyanto",
    author_email="bengskysec@gmail.com",
    url="https://github.com/bengsky13/tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'bengsky = bengsky.__main__:main',
        ],
    },
    python_requires='>=3.10',
)
