from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Function-Growth-Hierarchy',
    version='0.1.0',
    author='Bertrand Brodeau',
    author_email='bbrodeau@gmail.com',
    description='A complete hierarchy of function growth rates, from constants to functions beyond tetration.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/valorisa/Function-Growth-Hierarchy',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
