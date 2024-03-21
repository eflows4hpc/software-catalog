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
#     spack install py-permedcoe
#
# You can edit this file again by typing:
#
#     spack edit py-permedcoe
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyPermedcoe(PythonPackage):
    """PyPermedcoe: Personalized Medicine Center of Excellence Building Block base package."""

    homepage = "https://permedcoe.eu/"
    url = "https://pypi.org/packages/source/p/permedcoe/permedcoe-0.0.12.tar.gz"

    # List of GitHub accounts to notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version(
        "0.0.12",
        sha256="e385234b3aa5986c724f33b4323d46d0e9fdc6ce3f01ced6d0d657a57ba07503",
    )

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pyyaml", type="run")
