#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy

setup(
  name="python2torch",
  version="0.1",
  description="Call torch functions from python.",
  author="Kevin Matzen",
  url="https://github.com/kmatzen/python2torch",
  cmdclass = {'build_ext': build_ext},
  ext_modules = [
    Extension("python2torch",
              sources=["python2torch.pyx"],
              include_dirs=[numpy.get_include(), '/torch-distro/install/include/'],
              library_dirs=['/torch-distro/install/lib'],
              libraries = ['TH', 'luaT', 'luajit'])
  ]
)
