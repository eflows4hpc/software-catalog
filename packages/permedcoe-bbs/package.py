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
#     spack install permedcoe-bbs
#
# You can edit this file again by typing:
#
#     spack edit permedcoe-bbs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import os
import pathlib
import site
import subprocess
import stat
import zipfile
from urllib.request import urlretrieve
from spack.package import *


class PermedcoeBbs(BundlePackage):
    """PerMedCoE: All Building Blocks"""

    homepage = "https://github.com/PerMedCoE/BuildingBlocks"
    version("main")

    depends_on('python@3.8:', type=('build', 'run'))  # depends_on('python@3.10.6:', type=('build', 'run'))
    depends_on("py-setuptools", type="build")
    depends_on("py-pip", type="build")
    depends_on("py-permedcoe", type="run")
    depends_on("py-pyyaml", type="run")

    def install(self, spec, prefix):

        # Download the BBs package
        git = "https://github.com/PerMedCoE/BuildingBlocks/archive/refs/heads/main.zip"
        mkdir(prefix.bin)
        file_name = "main.zip"
        bbs_zip, _  = urlretrieve(git, filename=file_name)
        # Decompress the BBs
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())

        # Install all BBs
        bbs_path = os.getcwd() + "/BuildingBlocks-main/"
        items = os.listdir(bbs_path)
        for item in items:
            bb_path = os.path.join(bbs_path, item)
            if os.path.isdir(bb_path) and item != "Resources":
                # First, remove all @container
                print(f"Updating BB: {item}")
                target_file = list(pathlib.Path(bb_path).rglob("main.py"))[0]
                print(f" - Path: {target_file}")
                with open(target_file, "r") as source:
                    lines = source.readlines()
                with open(target_file, "w") as source:
                    for line in lines:
                        if line.startswith("@container"):
                            print("Removed @container")
                        else:
                            source.write(line)
                # Second, install
                print(f"Installing BB: {item}")
                print(f" - Path: {bb_path}")
                launch_script = os.path.join(bb_path, "install.sh")
                st = os.stat(launch_script)
                os.chmod(launch_script, st.st_mode | stat.S_IEXEC)
                subprocess.run([launch_script], cwd=bb_path)
