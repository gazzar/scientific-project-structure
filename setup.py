from setuptools import setup
import re


with open('new_acsemble/version.py', 'r') as f:
    version = re.search(r"__version__ = '(.*)'", f.read()).group(1)
    name = re.search(r"__name__ = '(.*)'", f.read()).group(1)

setup(
    name=name,
    version=version,
    packages=['new_acsemble'],
    entry_points={
        'console_scripts': [
            'main-script = new_acsemble.main:main'
        ]
    },
    install_requires=[
        'click==6.6',
    ],
)