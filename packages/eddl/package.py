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
#     spack install kratos
#
# You can edit this file again by typing:
#
#     spack edit kratos
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os


class Eddl(CMakePackage):
    """Package for installing EDDL"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://deephealthproject.github.io/eddl/"
    url      = "https://github.com/deephealthproject/eddl/archive/refs/tags/v1.2c.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version("1.2c", sha256="b6af4a21b515b728aaa6af94cf4a0bcc447fa04120d79b83c3956bb21ba5d607")
    version("1.2", sha256="b16182c7344fa89ecbdd591885cfa625fe006b2de7a51daba568f449ca0b4a2d")

    # FIXME: Add dependencies if required.
    depends_on('eigen@3.3.7')
    depends_on('protobuf@3.11.4')
    depends_on('cmake@3.17.2:',type='build')

    #variant
    variant('build', default="cpu", description='Spacifies the build version of the library', values=("cpu", "cuda", "cudnn", "fpga"), multi=False)
    depends_on('cuda', when='build=cuda')
    depends_on('cudnn', when='build=cudnn')
    #variant('xilinx', default=False, description='Builds a Xilinx FPGA version of the library')
   
    def url_for_version(self, version):
        url = "https://github.com/deephealthproject/eddl/archive/refs/tags/v{0}.tar.gz"
        return url.format(version)

    """
    def setup_run_environment(self, env):
        env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib)
        env.prepend_path('PYTHONPATH', self.prefix)
    """

    def cmake_args(self):
        # Add arguments other than
        # CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        args = []
        if self.spec.variants['build'].value == 'cuda':
            args.append('-DBUILD_TARGET=GPU')
        elif self.spec.variants['build'].value == 'cudnn':
            args.append('-DDUILD_TARGET=CUDNN')
        elif self.spec.variants['build'].value == 'fpga':
            args.append('-DDUILD_TARGET=FPGA')
        else:
            args.append('-DDUILD_TARGET=CPU')
        args.append('-DBUILD_TESTS=OFF')
        args.append('-DBUILD_EXAMPLES=OFF')

        return args

