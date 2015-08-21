#!/usr/bin/env python

import ice_pick

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'ice_pick',
    'ice_pick.filters',
]

test_requires = []
with open('requirements_test.txt') as f:
    test_requires = f.read().split('\n')

requires = []
with open('requirements.txt') as f:
    requires = f.read().split('\n')

setup(name=ice_pick.__title__,
      version=ice_pick.__version__,
      description='Python data access interface for Netflix OSS Ice Tool',
      author=ice_pick.__author__,
      author_email='opensource@demandmedia.com',
      url='https://github.com/demandmedia/ice_pick',
      license='Apache 2.0',
      packages=packages,
      package_dir={'ice_pick': 'ice_pick'},
      install_requires=requires,
      tests_require=test_requires,
      setup_requires=['nose==1.3.0'],
      classifiers=('Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'License :: OSI Approved :: Apache Software License',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
      )
)
