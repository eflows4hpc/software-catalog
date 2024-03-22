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
#     spack install py-dislib
#
# You can edit this file again by typing:
#
#     spack edit py-dislib
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyDislib(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://dislib.bsc.es"

    # FIXME: ensure the package is not available through PyPI. If it is,
    # re-run `spack create --force` with the PyPI URL.
    url      = "https://github.com/bsc-wdc/dislib/archive/refs/tags/v0.7.1.tar.gz"
    git = "https://github.com/bsc-wdc/dislib.git"
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('master', branch='master', submodules=True)
    version("0.9.0", sha256="2bd3ef6eb3fa14d224f6ae5496f9a28ac2f2821b992a6d7e615637bb89092c9a")
    version("0.8.0", sha256="76dde752ce681e0ffa852fd44c9fc7957502382be05a2f0174382de95e3bc593")
    version('0.7.1', sha256='29f4ad4fe76c42c206c465cc77db38bb86c2bee3aac340266df58352538311e5')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    depends_on('compss', type='run')
    depends_on('python@3.6:', type=('build', 'run'))
    #depends_on('py-setuptools', type='build')
    depends_on('py-scikit-learn@1.0.2^py-scipy@1.5.0^py-numpy@1.23.1', type=('run'))
    #depends_on('py-scikit-learn', type=('run'))
    #depends_on('py-cvxpy', type=('run'))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
