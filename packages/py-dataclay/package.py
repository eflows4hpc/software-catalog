from spack.package import *


class PyDataclay(PythonPackage):
    """dataClay active object store."""

    homepage = "https://dataclay.bsc.es"
    pypi = "dataclay/dataclay-3.0.1.tar.gz"

    maintainers = ["alexbarcelo", "support-dataclay"]

    version("3.0.1", sha256="0cb7fb53eb7196d8e18bf11fcb85c5a0f8f09643e739c1be6b2ecceb3f7303a4")

    # Python 3.10 required
    depends_on("python@3.10:", type=("build", "run"))

    # This project uses setuptools
    depends_on("py-setuptools", type="build")

    # Other dataclay dependencies
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-grpcio", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-protobuf", type=("build", "run"))
    depends_on("py-redis", type=("build", "run"))
    depends_on("py-bcrypt", type=("build", "run"))
