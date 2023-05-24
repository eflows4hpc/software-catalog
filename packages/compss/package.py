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
#     spack install compss
#
# You can edit this file again by typing:
#
#     spack edit compss
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Compss(Package):
    """COMP Superscalar programming model and runtime."""

    # Add a proper url for your package's homepage here.
    homepage = "https://compss.bsc.es"
    url      = "https://compss.bsc.es/repo/sc/stable/COMPSs_2.10.tar.gz"

    # notify when the package is updated.
    maintainers = ['jorgee', 'compsuperscalar']

    version("eflows4hpc", sha256="0251c82cdd4557ed9026f6296f7c475f3d15c3e1fc13edd04c7ff1399328d2b3")
    version("3.1", sha256="53880443567269faa724d1908a6bc4d82998be3cc93c77386f620c4c8a72e60d", preferred=True)
    version("3.0", sha256="3a84e0c6cd84aea155abf08370b1ad5bf5f65c99d4b17d70346c6457e7d0b215")
    version("2.10.1", sha256="0a983a85b53c3a1c82ea63aedf54e353c5627ba25b85c1cda1bbea5a35ba08af")
    version("2.10-riscv", sha256="2170abfc484234b1384a4ec698acfe045ffca56806624e6237f5dab39bfe86bf")
    version("2.10", sha256="0795ca7674f1bdd0faeac950fa329377596494f64223650fe65a096807d58a60")

    # dependencies. 
    depends_on('python@3.6:')
    depends_on('openjdk')
    depends_on('boost')
    depends_on('libxml2')
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('m4', type='build')
    depends_on('py-setuptools', when="@3.1:", type='build')

    def install(self, spec, prefix):
        import os
        print("Prefix: " + str(prefix))
        install_script = Executable('./install')
        if spec.satisfies("@2.10"):
            install_script('-A', '--only-python-3', prefix.compss)
        else: 
            install_script(prefix.compss)
        print("Dirs: " +str(os.listdir(str(prefix))))


    def setup_run_environment(self, env):
        env.set('COMPSS_HOME', self.prefix.compss)
        env.prepend_path('PATH', self.prefix.compss + '/Runtime/scripts/user')
