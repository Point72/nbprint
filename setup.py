from setuptools import setup, find_packages
from codecs import open
from os import path

from jupyter_packaging import ensure_python, get_version

pjoin = path.join

ensure_python(('2.7', '>=3.3'))

name = 'nbcx_templates'
here = path.abspath(path.dirname(__file__))
version = get_version(pjoin(here, name, '_version.py'))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requires = f.read().split()


setup(
    name=name,
    version=version,
    description='NBConvert Templates',
    long_description=long_description,
    url='https://github.com/timkpaine/nbcx_templates',
    author='Tim Paine',
    author_email='t.paine154@gmail.com',
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Jupyter',
    ],

    keywords='jupyter nbconvert',
    packages=find_packages(exclude=['tests', ]),
    install_requires=requires,
    extras_require={
        'dev': requires + ['pytest', 'pytest-cov', 'pylint', 'flake8', 'bumpversion', 'mock', 'codecov']
    },
    include_package_data=True,
    zip_safe=False,

)
