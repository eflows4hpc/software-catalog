from spack.package import *



class PyHecuba(PythonPackage):
    """Hecuba package"""
    #git = "https://github.com/bsc-dd/hecuba.git"
    git = "https://github.com/eflows4hpc/hecuba.git"
    homepage = "https://github.com/bsc-dd/hecuba"
    url = "https://github.com/bsc-dd/hecuba"
    version("master", branch="master")
    #version("1.2.4", tag="v1.2.4")
    depends_on("python@3.6:", type=("build", "link", "run"))
    depends_on("py-setuptools", type=("build"))
    depends_on("cmake@3.14:")
    depends_on("py-numpy")
    depends_on("boost")

    def install(self, spec, prefix):
        import os
        # Ensure that the Python interpreter used for the build is in the PATH
        python_exe = which('python')

        ## Run the installation command using python setup.py install
        os.environ['CMAKE_BUILD_PARALLEL_LEVEL']=str(32)
        setup_cmd = ['setup.py', 'install', '--prefix={0}'.format(prefix)]
        python_exe(*setup_cmd)

        #self.stage.source_path
        install_cmd = Executable('./cassandra4slurm/install.sh')
        dirname_cmd =which('dirname')
        install_cmd(prefix)


    def setup_run_environment(self, env):
        env.set('HECUBA_ROOT', self.prefix)
        env.set('STORAGE_HOME', self.prefix+'/compss')
        env.prepend_path('LD_LIBRARY_PATH', self.prefix+'/lib')
        env.prepend_path('PYTHONPATH', self.prefix+'/lib/python3.10/site-packages')
        env.prepend_path('CLASSPATH', self.prefix+'/compss/ITF/StorageItf-1.0-jar-with-dependencies.jar')
        env.prepend_path('CPATH', self.prefix+'/include')
