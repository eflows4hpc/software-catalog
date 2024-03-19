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
#     spack install physiboss_invasion
#
# You can edit this file again by typing:
#
#     spack edit physiboss_invasion
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import re
from spack.package import *


class PhysibossInvasion(MakefilePackage):
    """PhysiBoSS for invasion analysis."""

    homepage = "https://github.com/sysbio-curie/Invasion_model_PhysiBoSS"
    git = "https://github.com/sysbio-curie/Invasion_model_PhysiBoSS.git"

    # List of GitHub accounts to notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    build_directory = "src"
    version("master", branch="master")

    depends_on("flex", type="build")
    depends_on("bison", type="build")
    depends_on("maboss@2.5.2", type="run")

    def install(self, spec, prefix):
        # destination = "/usr/local/scm/Invasion_model_PhysiBoSS/"
        # # Folder not found - there will be a ln -s in post-install
        # # /opt/view/physiboss_invasion -> ln -s /opt/view/physiboss_invasion /usr/local/scm/Invasion_model_PhysiBoSS
        destination = prefix.physiboss_invasion
        mkdir(destination)
        install_tree(".", destination)
        # Do some configuration
        # sed -i "s/<folder>./<folder>output/g" /usr/local/src/Invasion_model_PhysiBoSS/data/PhysiCell_settings_2D.xml
        config_file = destination + "/data/PhysiCell_settings_2D.xml"
        with open(config_file, "r") as source:
            lines = source.readlines()
        with open(config_file, "w") as source:
            for line in lines:
                sed_line = re.sub(r"<folder>.", "<folder>output", line)
                source.write(sed_line)
        print(f"Updated file: {config_file}")

    def setup_run_environment(self, env):
        # destination = "/usr/local/scm/Invasion_model_PhysiBoSS/"
        destination = self.prefix.physiboss_invasion
        env.prepend_path("PATH", destination)
        env.prepend_path("PATH", destination + "/src/")
