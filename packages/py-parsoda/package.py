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
#     spack install py-parsoda
#
# You can edit this file again by typing:
#
#     spack edit py-parsoda
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyParsoda(PythonPackage):
    """ParSoDA: Parallel Social Data Analytics library"""

    homepage = "https://github.com/eflows4hpc/parsoda"
    url = "https://github.com/eflows4hpc/parsoda/archive/refs/tags/1.1.0.tar.gz"

    # list of GitHub accounts to notify when the package is updated.
    maintainers = ["sv-giampa", "lorisbel"]

    version("1.1.0", sha256="16d5bdab98dea3a176d809e60c43250461371e9bd58fc9be60930b6298907ba4")
    
    depends_on('python@3.8:', type=('build', 'run'))
    depends_on("py-setuptools", type="build")