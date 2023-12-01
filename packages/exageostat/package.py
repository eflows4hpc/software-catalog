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
#     spack install exageostat
#
# You can edit this file again by typing:
#
#     spack edit exageostat
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Exageostat(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
   # url      = "https://github.com/ecrc/exageostat/archive/refs/tags/v1.1.0.tar.gz"
    git      = "https://github.com/omar-hmarzouk/exageostat.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    
    version('master', branch='Spack-changes', submodules=True)
    #version('spack', branch='spack', submodules=True)
    #version('1.1.0', tag='v1.1.0', submodules=True)
    variant('mpi', default=False, description='Enable MPI')
    variant('cuda', default=False, description='Enable CUDA')
    variant('hicma', default=False, description='Enable HiCMA')
    # FIXME: Add dependencies if required.
    # depends_on('foo')
#    depends_on("intel-mkl")
    depends_on('chameleon-ecrc@default')
    depends_on('chameleon-ecrc@default~mpi',when='~mpi')
    depends_on('chameleon-ecrc@default+mpi',when='+mpi')
    depends_on('chameleon-ecrc@default+cuda',when='+cuda')
    depends_on('chameleon-ecrc@default~cuda',when='~cuda')
    depends_on('gsl')
    depends_on('nlopt')
    depends_on('stars-h@exageostat', when='+hicma')
    #depends_on('stars-h@exageostat', when='~hicma')
    depends_on('hicma@exageostat', when='+hicma')
    #depends_on('hicma@exageostat', when='~hicma')

    def setup_build_environment(self, env):
        print(self.stage.source_path)
        env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib)
        env.prepend_path('CPATH', self.prefix.include)
        env.prepend_path('PATH', self.prefix.include)
 #       os.path.join(self.stage.source_path, "include")
        env.prepend_path('CPATH', self.stage.source_path)
        env.prepend_path('PATH', self.stage.source_path)
        #if self.spec.satisfies("+mpi"):
        #    env.set('CC', 'mpicc')
        #    env.set('FC','mpifort')
        #    env.set('CXX', 'mpicxx')

    def cache_test_sources(self):
        """Copy the example source files after the package is installed to an
        install test subdirectory for use during `spack test run`."""
        self.cache_extra_test_sources(['include'])

    def setup_run_environment(self, env):
        env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib)
        env.prepend_path('CPATH', self.prefix.include)
        env.prepend_path('PATH', self.prefix.include)

    def cmake_args(self):
        spec = self.spec
        args = [
                "-Wno-dev",
                self.define("CMAKE_COLOR_MAKEFILE", "ON"),
                self.define("CMAKE_VERBOSE_MAKEFILE", "ON"),
                self.define_from_variant("EXAGEOSTAT_USE_MPI", "mpi"),
                self.define_from_variant("EXAGEOSTAT_USE_CUDA", "cuda"),
                self.define("EXAGEOSTAT_EXAMPLES" ,"ON"),
                self.define("EXAGEOSTAT_SCHED_STARPU", "ON")
                #self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
                ]
        #args.append('-j') apparently not needed, done by default.
        args.append("-DECRC_VERBOSE_FIND_PACKAGE=ON")

        if spec.satisfies('+mpi'):
            print("EXAGEOSTAT-MPI")
            args.extend([
                self.define("MPI_C_COMPILER", self.spec['mpi'].mpicc),
                self.define("MPI_CXX_COMPILER", self.spec['mpi'].mpicxx),
                self.define("MPI_Fortran_COMPILER", self.spec['mpi'].mpifc),
            ])
        if spec.satisfies('+hicma'):
            print("EXAGEOSTAT-HiCMA")
            args.extend([
                self.define("EXAGEOSTAT_USE_HICMA", "ON"),
            ]) 
        return args
