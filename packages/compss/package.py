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

    version('2.10-riscv', sha256='04c0a7dfde86d541fee9281e588bc725e84266f7f18754d743924a584d9650f2')
    version('2.10',       sha256='0795ca7674f1bdd0faeac950fa329377596494f64223650fe65a096807d58a60', preferred=True)

    # dependencies. 
    depends_on('python@3.6:')
    depends_on('openjdk')
    depends_on('boost')
    depends_on('libxml2')
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('m4', type='build')

    def install(self, spec, prefix):
        import os
        print("Prefix: " + str(prefix))
        install_script = Executable('./install')
        install_script('-A', '--only-python-3', prefix.compss)
        print("Dirs: " +str(os.listdir(str(prefix))))


    def setup_run_environment(self, env):
        env.set('COMPSS_HOME', self.prefix.compss)
        env.prepend_path('PATH', self.prefix.compss + '/Runtime/scripts/user')
