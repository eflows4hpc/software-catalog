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
    version('eflows4hpc', branch='eflows4hpc_hecuba_integration', submodules=True)
    version('2.1.1', sha256='a4c9006489f9010be11ed30b8249efc63af8125d9214e94977e2dd16c75ecc38')
    version('2.1.0', sha256='b46e8a22d160b0e34915f573f4ca1f9f08f5be121c3b814b15e0baa592490aa4')

    # FIXME: Add dependencies if required.
    depends_on('mpi')
    depends_on('netcdf-fortran')
    depends_on('blas')
    
    variant('hecuba', default=False, description='Builds a MPI version of the library')
    def setup_build_environment(self, env):
        env.set('CC', self.spec['mpi'].mpicc)
        env.set('FC',self.spec['mpi'].mpifc) 
        env.set('CXX', self.spec['mpi'].mpicxx)
        env.set('F77', self.spec['mpi'].mpif77)
    
    @run_after('install')
    def copy_fesom(self):
        #print("***** Calling super install ****") 
        #super().install(spec, prefix)
        print("***** Coping fesom binary to bin ****")
        mkdirp(self.prefix.bin)
        install(self.stage.source_path+'/bin/fesom.x', self.prefix.bin)

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        if self.spec.variants['hecuba'].value == True:
            args.append('-DUSE_HECUBA=ON')
        else:
            args.append('-DUSE_HECUBA=OFF')
        return args
