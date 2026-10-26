# Modified in the goto4711/learntools fork (26 October 2026): the version is read
# from learntools/__init__.py as text instead of importing the package. Importing
# it needs pandas, which is not available when pip or uv build the package in an
# isolated environment, so the install failed. See FORK.md.
import re
from pathlib import Path

from setuptools import setup
from setuptools import find_packages

version = re.search(r"__version__\s*=\s*['\"]([^'\"]+)['\"]",
                    Path(__file__).with_name('learntools').joinpath('__init__.py').read_text()).group(1)

setup(name='learntools',
      version=version,
      description='Utilities for Kaggle Learn exercises',
      url='http://github.com/kaggle/learntools',
      author='Dan Becker',
      author_email='dan@kaggle.com',
      license='Apache 2.0',
      packages=find_packages(),
      zip_safe=True)
