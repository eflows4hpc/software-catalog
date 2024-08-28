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
    version("eflows4hpc", sha256="a85efd592b85fe3392497da85d192e7543e6ac1e8333c6c3f8ca7f0777a54aaf")
    version("3.3.2", sha256="7dffd1e5c7cedf23b65b523fc4daefff3be8c04c788a0e116039d07585769a0e")
    version("3.3.1", sha256="aa4f1f0cb0efef70f8b22f9444102ca786d98c2c022aecce8c9a30bf3421f775", preferred=True)
    version("3.3.ear", sha256="84a1a0232e70a733239c9ddfde16ff6aa51a2fff6a5764098dea01f4e24667ee")
    version("3.3", sha256="9ebec2be7225bf01cf563d208434cfbaeb988a8cb439b35c3b7c1a231b7cea57")
    version("3.2", sha256="f32825d7f26bde13cd3699f0aea14da18632b30cf08f113a06ae050033efc837")
    version("3.1", sha256="53880443567269faa724d1908a6bc4d82998be3cc93c77386f620c4c8a72e60d")
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
    depends_on('py-setuptools', when="@eflows4hpc", type='build')
    
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
