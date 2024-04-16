# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install stars-h
#
# You can edit this file again by typing:
#
#     spack edit stars-h
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
import os

class StarsH(CMakePackage):
    """Package for installing stars-H"""

    #homepage = "https://ecrc.github.io/stars-h/index.html"
    #url      = "https://github.com/sabdulah/stars-h/archive/refs/tags/v0.3.0.tar.gz"
    git      =  "https://github.com/sabdulah/stars-h.git"
    url       = "https://github.com/sabdulah/stars-h"


    #git submodule update --init --recursive?
    version('master', branch='master', submodules=True)
    version('hicma', commit='5347cf6a33f3762b25f959e4eb08bbfa7b766016', submodules=True)
    #version('exageostat', commit='aacd9cc065c91cd4c00a2fd1f2d1c977d9cf5b81', submodules=True)
    version('exageostat', branch='sabdulah/spack-version', submodules=True)
    #version('release/v0.1.1', branch='release/v0.1.1')
    #version('0.3.0', sha256='883c2091c7910c24ed22ffc99ce29b2b2d21e4b4c9df6764b6157457fd9b167b')
    #version('0.2.0', sha256='b58c0fdb2f157cb0320c7da8062c200d4bd20a779ff7f790bb5177e6df20e48b')

    #variant('shared', default=True, description='Build chameleon as a shared library')
    #dependencies.
    #depends_on('openblas') #queries the system for the best BLAS
    extends('python')
    #depends_on('qt', type='build')
    depends_on('py-sip', type='build')
    depends_on("pkgconfig", type='build')
    depends_on('gsl')
    #depends_on("pkgconfig", type='build')
    #depends_on('lapack')
    #depends_on('netlib-xblas')
    #depends_on('netlib-lapack')
    #depends_on('gcc')
    #depends_on('fortran')
    depends_on('intel-mkl')
    #variants
    #depends_on("pkgconfig", type='build')
    #no variants needed for stars-H
    #print(os.path.dirname(os.path.abspath(__file__)))
    
    def setup_build_environment(self, env):
        env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib)
        env.prepend_path('CPATH', self.prefix.include)
        env.prepend_path('PATH', self.prefix.include)
        os.path.join(self.stage.source_path, "include")
        env.prepend_path('CPATH', self.stage.source_path)
        env.prepend_path('PATH', self.stage.source_path)

    def cache_test_sources(self):
    #    """Copy the example source files after the package is installed to an
    #    install test subdirectory for use during `spack test run`."""
        self.cache_extra_test_sources(['include'])

    #def setup_run_environment(self, env):
        #I don't know if line 45 is the correct syntax for the second argument self.prefix.pkgconfig
        #put in different function?
        #env.prepend_path('PKG_CONFIG_PATH', self.prefix.pkgconfig) #export PKG_CONFIG_PATH=$STARSHDIR/build/install_dir/lib/pkgconfig:$PKG_CONFIG_PATH
        #env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib)
        #env.prepend_path('CPATH', self.prefix.include)
        #env.prepend_path('PATH', self.prefix.include)
 #       os.path.join(self.stage.source_path, "include")  
  #export LD_LIBRARY_PATH=$STARSHDIR/build/install_dir/lib:$LD_LIBRARY_PATH

    def cmake_args(self):
        spec = self.spec
        args = [
              #  "-Wno-dev",
                #self.define("CMAKE_C_FLAGS_RELEASE", "-lm"),
              #  self.define("CMAKE_VERBOSE_MAKEFILE", "ON"),
                #self.define("CHAMELEON_ENABLE_EXAMPLE", "ON"),
                #self.define("CHAMELEON_ENABLE_TESTING", "ON"),
              #  self.define("BUILD_SHARED_LIBS", "ON"),
               ]
        #args.append('-j') apparently not needed, done by default.
        #args.append("-DECRC_VERBOSE_FIND_PACKAGE=ON")
        #args.append('-DEXAMPLES=OFF')
        args.append('-DSTARPU=OFF')
        #args.append('-DTESTING=ON')
        args.append('-DCMAKE_C_FLAGS=-fPIC')
        #args.append('-DCMAKE_BUILD_TYPE="Release"')
        #args.append('-DCMAKE_C_FLAGS_RELEASE="-lm -O3 -Ofast -w -ldl -g"')
        args.append('-DOPENMP=OFF')
        args.append('-DMPI=OFF')
        args.append('-DGSL=ON')
        return args
