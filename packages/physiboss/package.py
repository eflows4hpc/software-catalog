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
#     spack install physiboss
#
# You can edit this file again by typing:
#
#     spack edit physiboss
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Physiboss(MakefilePackage):
    """PhysiBoSS: a sustainable integration of stochastic Boolean and agent-based modelling frameworks."""

    homepage = "https://github.com/vincent-noel/COVID19"
    git = "https://github.com/vincent-noel/COVID19.git"

    # List of GitHub accounts to notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    build_directory = "PhysiCell"
    version("0.6.0", branch="v6")

    # FIXME: Add dependencies if required.
    depends_on("flex", type="build")
    depends_on("bison", type="build")
    depends_on("maboss@2.5.2", type="run")

    def setup_build_environment(self, env):
        env.prepend_path(
            "LD_LIBRARY_PATH",
            self.stage.source_path
            + "/PhysiCell/addons/PhysiBoSS/MaBoSS-env-2.0/engine/src/",
        )
        env.prepend_path(
            "LD_LIBRARY_PATH",
            self.stage.source_path
            + "/PhysiCell/addons/PhysiBoSS/MaBoSS-env-2.0/engine/include/",
        )

    def install(self, spec, prefix):
        # destination = "/usr/local/scm/COVID19/PhysiCell/"
        # # Folder not found - there will be a ln -s in post-install
        # # /opt/view/physiboss -> ln -s /opt/view/physiboss /usr/local/scm/COVID19/PhysiCell/
        destination = prefix.physiboss
        mkdir(destination)
        # Copy the entire folder (which contains the binary and files)
        install_tree("PhysiCell", destination)

    def setup_run_environment(self, env):
        # destination = "/usr/local/scm/COVID19/PhysiCell/"
        destination = self.prefix.physiboss
        env.prepend_path("PATH", destination)
