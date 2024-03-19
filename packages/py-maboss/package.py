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
#     spack install py-maboss
#
# You can edit this file again by typing:
#
#     spack edit py-maboss
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyMaboss(PythonPackage):
    """PyMaBoSS: Python API for the MaBoSS software"""

    homepage = "https://github.com/colomoto/pyMaBoSS"
    url = "https://github.com/colomoto/pyMaBoSS/archive/refs/tags/v0.8.4.tar.gz"

    # List of GitHub accounts to notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version(
        "0.8.4",
        sha256="f9f4ebc95829f8eb78f3bc52ed6ddcf9a7b4cb84a6549e36dc6f390dc8a43be4",
    )

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.24.2", type="run")
    depends_on("py-pandas@1.5.3", type="run")
    depends_on("py-scikit-learn@1.2.1", type="run")
    # depends_on("py-pyparsing", type="run")  # Installed with pip.
    # depends_on("py-ipywidgets", type="run")  # triggers py-matplotlib which fails
    # depends_on("py-matplotlib@3.6.3", type=('run'))  # This fails. It is installed with pip.
    # depends_on(cmaboss)  # not available in spack. It is installed with pip (cmaboss>=1.0.0b17).
    # depends_on(colomoto_jupyter)  # not available in spack. It is installed with pip (colomoto_jupyter>=0.4.10).
    # depends_on("py-seaborn@0.12.2", type="run")  # not really used
    # depends_on("py-xlsxwriter", type="run") # not really used
