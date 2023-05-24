from spack.package import *


class PyHecuba(PythonPackage):
    git = "https://github.com/bsc-dd/hecuba.git"
    
    version("master", branch="master")
    version("1.2.4", tag="v1.2.4")

    depends_on("python@3.6:", type=("build", "link", "run"))
    depends_on("py-setuptools", type=("build"))
    depends_on("cmake@3.14:")
    depends_on("py-numpy")
    depends_on("cassandra")
    depends_on("kafka")

