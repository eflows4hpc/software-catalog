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


class PyEddl(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://deephealthproject.github.io/pyeddl/"

    url      = "https://github.com/deephealthproject/pyeddl/archive/refs/tags/1.3.1.tar.gz"
    git = "https://github.com/deephealthproject/pyeddl.git"
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('master', branch='master', submodules=True)
    version("1.3.1", sha256="97d1f263320ba3522904a29650ca9cfdb247510583a7ca4a8bc5312c7415405d")

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    depends_on('eddl')
    depends_on('python@3.8:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-pybind11@:2.5.9', type='build')
    depends_on('py-pytest', type='build')
    depends_on('py-numpy')

    """
    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
    """
