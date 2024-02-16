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
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/sysbio-curie/Invasion_model_PhysiBoSS"
    git = "https://github.com/sysbio-curie/Invasion_model_PhysiBoSS.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]
    build_directory = 'src'
    version("master", branch="master")

    # FIXME: Add dependencies if required.
    depends_on("flex", type="build")
    depends_on("bison", type="build")
    depends_on("maboss@2.5.2", type="run")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("src/myproj", prefix.bin)
        install_tree(".", prefix.bin)
        # Do some configuration
        # sed -i "s/<folder>./<folder>output/g" /usr/local/src/Invasion_model_PhysiBoSS/data/PhysiCell_settings_2D.xml
        config_file = self.prefix.bin + "/data/PhysiCell_settings_2D.xml"
        with open(config_file, "r") as source:
            lines = source.readlines()
        with open(config_file, "w") as source:
            for line in lines:
                sed_line = re.sub(r'<folder>.', '<folder>output', line)
                source.write(sed_line)
        print(f"Updated file: {config_file}")

    def setup_run_environment(self, env):
        env.prepend_path('PATH', self.prefix.bin)
