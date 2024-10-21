# setup.py

from setuptools import setup, find_packages

setup(
    name='excel_to_json_converter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    description='A simple library to convert Excel sheets to JSON format by Ksr小熙.',
    author='Ksr小熙',
    author_email='',
    url=''
)
