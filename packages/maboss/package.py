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
#     spack install maboss
#
# You can edit this file again by typing:
#
#     spack edit maboss
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import os
from urllib.request import urlretrieve
from spack.package import *


class Maboss(MakefilePackage):
    """MaBoSS Spack package."""

    homepage = "https://maboss.curie.fr/"
    url = (
        "https://github.com/sysbio-curie/MaBoSS-env-2.0/archive/refs/tags/v2.5.2.tar.gz"
    )

    # Add a list of GitHub accounts to notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]
    build_directory = "engine/src"
    version(
        "2.5.2",
        sha256="ab77f592c36cee9a78561b0838ec7322d2ab50229f9fc0584262da205a7414a7",
    )

    # Dependencies
    depends_on("flex", type="build")
    depends_on("bison", type="build")
    # # R requires apt install libbz2-dev and liblzma-dev before
    # depends_on("r@4.1.2:", type=("build", "run"))
    # # Perl from spack fails with bzip2 and lzma even doing apt install libbz2-dev and liblzma-dev
    # # So using system installed perl 5.30
    # depends_on("perl@5.34.0", type="build")
    depends_on("py-maboss@0.8.4", type="run")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("engine/src/MaBoSS", prefix.bin)
        install_tree("engine", prefix.bin)
        # Download BINOM.jar and VDAOEengine.jar
        mkdir(prefix.bin + "/jar")
        binom_jar, _ = urlretrieve(
            "https://b2drop.bsc.es/index.php/s/SRWPNAkKL73oaRw/download",
            filename="BINOM.jar",
        )
        vdao_jar, _ = urlretrieve(
            "https://github.com/auranic/VDAOEngine/raw/master/jar/VDAOEngine.jar",
            filename="VDAOEngine.jar",
        )
        install(binom_jar, os.path.join(prefix.bin, "jar", binom_jar))
        install(vdao_jar, os.path.join(prefix.bin, "jar", vdao_jar))
        system_path = "/usr/local/jar"
        mkdir(system_path)
        install(binom_jar, os.path.join(system_path, binom_jar))
        install(vdao_jar, os.path.join(system_path, vdao_jar))

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)
