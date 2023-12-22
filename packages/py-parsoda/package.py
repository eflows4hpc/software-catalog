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
    url = "https://github.com/eflows4hpc/parsoda/archive/refs/tags/v1.2.0.tar.gz"

    # list of GitHub accounts to notify when the package is updated.
    maintainers = ["sv-giampa", "lorisbel"]

    version("1.2.1", sha256="f0897a95801d7e3d3c4f1d76c3ba93c67b07d2e320d5eca71c1ae501fe145291")
    version("1.2.0", sha256="49e26e51a6b51fc3ae52599b380a6f027c9bafefe8d9e04886e75ce621f3f4d3")
    version("1.1.0", sha256="287ccf6fb78950217c6f5005fb71afb982e1431a75b012458ff29347082c6e59", url = "https://github.com/eflows4hpc/parsoda/archive/refs/tags/1.1.0.tar.gz")
    version("1.0.0", sha256="9d3c513f7d5e29fe6a2f286db5549c1fac469dcd3b07ca14684f9362e862a10c", url = "https://github.com/eflows4hpc/parsoda/archive/refs/tags/1.0.0.tar.gz")
   
    depends_on('python@3.8:', type=('build', 'run'))
    depends_on("py-setuptools", type="build")
