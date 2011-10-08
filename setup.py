from distribute_setup import use_setuptools
from setuptools import setup

setup(
    name='subs-crawler',
    author='Andrea Francia',
    entry_points={ 'console_scripts' : [ 'crawls-subs = crawler:main']},
    py_modules=['crawler'],
    )
