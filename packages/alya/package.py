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
#     spack install alya
#
# You can edit this file again by typing:
#
#     spack edit alya
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os

class Alya(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    #url      = "file:///alya"
    manual_download = True
    # root_cmakelists_dir = 'alya-master'
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions here.
    version('master', sha256='a6c216c18f31ca5a16315aa286ef62b340e6bf52f35f9091c0753e916363a9ad')

    # FIXME: Add dependencies if required.
    depends_on('mpi')

    def url_for_version(self, version):
        return "file://{0}/alya-{1}.tar.gz".format(
                os.getcwd(), version)
    
    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        args.extend([self.define("CMAKE_MODULE_PATH", self.stage.source_path)])
        return args
    
    def install(self, spec, prefix):
        #print("***** Calling super install ****") 
        super().install(spec, prefix)

