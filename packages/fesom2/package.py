# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
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
#     spack install fesom2
#
# You can edit this file again by typing:
#
#     spack edit fesom2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Fesom2(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/FESOM/fesom2/archive/refs/tags/2.1.1.tar.gz"
    git      = "https://github.com/FESOM/fesom2.git"
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('eflows4hpc', branch='eflows_hecuba_templates_update', submodules=True)
    version('eflows4hpc_y2', branch='eflows4hpc_hecuba_integration', submodules=True)
    version('2.1.1', sha256='a4c9006489f9010be11ed30b8249efc63af8125d9214e94977e2dd16c75ecc38')
    version('2.1.0', sha256='b46e8a22d160b0e34915f573f4ca1f9f08f5be121c3b814b15e0baa592490aa4')

    # FIXME: Add dependencies if required.
    depends_on('mpi')
    depends_on('netcdf-fortran')
    depends_on('blas')
    
    variant('hecuba', default=False, description='Builds a MPI version of the library')

    #def setup_build_environment(self, env):
        #env.set('CC', self.spec['mpi'].mpicc)
        #env.set('FC',self.spec['mpi'].mpifc) 
        #env.set('CXX', self.spec['mpi'].mpicxx)
        #env.set('F77', self.spec['mpi'].mpif77)
        #env.prepend_path('LD_LIBRARY_PATH', str(self.spec['blas'].libs.directories[0]))
        #env.prepend_path('C_INCLUDE_PATH', str(self.spec['blas'].headers.directories[0]))
        #env.append_flags('LD_FLAGS',self.spec['blas'].libs.ld_flags)
    
    @run_after('install')
    def copy_fesom(self):
        #pmrint("***** Calling super install ****") 
        #super().install(spec, prefix)
        print("***** Coping fesom binary to bin ****")
        mkdirp(self.prefix.bin)
        install(self.stage.source_path+'/bin/fesom.x', self.prefix.bin)
    def patch(self):
        microarch = self.spec.target
        comp = self.spec.compiler
        filter_file("-march=native", microarch.optimization_flags(comp.name, str(comp.version)),
                "Makefile.in_gnu_impi")
        filter_file("-march=native", microarch.optimization_flags(comp.name, str(comp.version)),
                "src/CMakeLists.txt")

    def cmake_args(self):
        spec = self.spec
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        if self.spec.variants['hecuba'].value == True:
            args.append('-DUSE_HECUBA=ON')
        else:
            args.append('-DUSE_HECUBA=OFF')
        args.append(self.define('CMAKE_C_COMPILER', spec['mpi'].mpicc))
        args.append(self.define('CMAKE_CXX_COMPILER', spec['mpi'].mpicxx))
        args.append(self.define('CMAKE_Fortran_COMPILER', spec['mpi'].mpifc))
        if ('^intel-mkl' in spec or '^intel-parallel-studio+mkl' in spec):
            args.extend([self.define("BLA_VENDOR", "Intel10_64ilp")])
        elif '^netlib-lapack' in spec:
            args.extend([self.define("BLA_VENDOR", "Generic")])
        elif '^openblas' in spec:
            args.extend([self.define("BLA_VENDOR", "OpenBLAS")])
        microarch = self.spec.target
        comp = self.spec.compiler
        math_libs = self.spec['blas'].libs
        args.extend([self.define("CMAKE_C_FLAGS",microarch.optimization_flags(comp.name, str(comp.version)) +" "+self.spec['blas'].headers.include_flags)])
        args.extend([self.define("CMAKE_CXX_FLAGS",microarch.optimization_flags(comp.name, str(comp.version))+ " "+self.spec['blas'].headers.include_flags)])
        args.extend([self.define("CMAKE_Fortran_FLAGS",microarch.optimization_flags(comp.name, str(comp.version))+" "+self.spec['blas'].headers.include_flags)])
        #args.append('-DBLA_VENDOR=Intel10_64ilp')
        #args.append('-DBLA_STATIC=ON')
        #args.append('-DBLA_VENDOR=OpenBLAS')
        """
        blas = self.spec['blas'].libs
        args.extend([
          '-DBLAS_LIBRARY_NAMES={0}'.format(';'.join(blas.names)),
          '-DBLAS_LIBRARY_DIRS={0}'.format(';'.join(blas.directories))])
        math_libs = self.spec['blas'].libs
        args.append(
          '-DMATH_LIBS:STRING={0}'.format(math_libs.ld_flags)
        )
        """
        
        args.append(
          '-DBLAS_LIBRARIES={0}'.format("-L"+self.spec['blas'].libs.directories[0]+" -Wl,--no-as-needed -lmkl_gf_ilp64 -lmkl_gnu_thread -lmkl_core -lgomp -lpthread -lm -ldl")
        )
        return args
        
