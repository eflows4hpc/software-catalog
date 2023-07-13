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
#     spack install hicma
#
# You can edit this file again by typing:
#
#     spack edit hicma
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Hicma(CMakePackage):
    """FIXME: Put a proper description of your package here."""


    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/ecrc/hicma/archive/refs/tags/v0.1.3.tar.gz"
    git      = "https://github.com/ecrc/hicma"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
        #git submodule update --init --recursive?
    version('master', branch='master',submodules = True)
    version('exageostat', commit='28bb2239427dd25a23fd63d43d605aeda0e98218', submodules=True)
    version('0.1.3', sha256='556013d00139ebe7961d7d4f6ac0fadc6fc6c1b58c70ee49345fad2a881fd1a7')
    version('0.1.1', sha256='f5ccc69e22644c4ff0559e2af02dcc1dfd40d73e825b17eac119d807642e7fdb')

    # chameleon's specific
    variant(
        "runtime",
        default="starpu",
        description="Runtime support",
        values=("openmp", "starpu"),
        multi=False,
    )
    variant("mpi", default=True, when="runtime=starpu", description="Enable MPI")
    variant("cuda", default=False, when="runtime=starpu", description="Enable CUDA")
    variant(
        "fxt",
        default=False,
        when="runtime=starpu",
        description="Enable FxT tracing support through StarPU",
    )
    variant(
        "simgrid",
        default=False,
        when="runtime=starpu",
        description="Enable simulation mode through StarPU+SimGrid",
    )

       # dependencies
    depends_on("pkgconfig", type="build")
    depends_on("stars-h@exageostat")
    depends_on("chameleon-ecrc@default+mpi", when="+mpi") 

    with when("runtime=starpu"):
        depends_on("starpu")
        depends_on("starpu~mpi", when="~mpi")
        depends_on("starpu+mpi", when="+mpi")
        depends_on("starpu~cuda", when="~cuda")
        depends_on("starpu+cuda", when="+cuda")
        #with when("+simgrid"):
            #depends_on("simgrid+msg")
            #depends_on("starpu+simgrid")
            #depends_on("starpu+mpi~shared+simgrid", when="+mpi")
            #conflicts("^simgrid@:3.31", when="@:1.1.0")
            #conflicts("+shared", when="+simgrid")
        #with when("~simgrid"):
            #depends_on("mpi", when="+mpi")
            #depends_on("cuda", when="+cuda")
        #with when("+fxt"):
            #depends_on("fxt")
            #depends_on("starpu+fxt")

    with when("~simgrid"):
        depends_on("blas")
        depends_on("lapack")

    def cmake_args(self):

        spec = self.spec
        args = [
            "-Wno-dev",
            self.define("CMAKE_COLOR_MAKEFILE", "ON"),
            self.define("CMAKE_VERBOSE_MAKEFILE", "ON"),
            self.define("HICMA_ENABLE_EXAMPLE", "ON"),
            self.define("HICMA_ENABLE_TESTING", "ON"),
            #self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("HICMA_USE_MPI", "mpi"),
            #self.define_from_variant("HICMA_USE_CUDA", "cuda"),
            #self.define_from_variant("HICMA_SIMULATION", "simgrid"),
        ]

        if spec.satisfies("runtime=openmp"):
            args.extend([self.define("HICMA_SCHED", "OPENMP")])
        if spec.satisfies("runtime=starpu"):
            args.extend([self.define("HICMA_SCHED", "STARPU")])

        if spec.satisfies("+mpi"):
            print("hihihih")
            print(self.spec["mpi"].mpicc)
            args.extend(
                [
                    self.define("MPI_C_COMPILER", self.spec["mpi"].mpicc),
                    self.define("MPI_CXX_COMPILER", self.spec["mpi"].mpicxx),
                    self.define("MPI_Fortran_COMPILER", self.spec["mpi"].mpifc),
                ]
            )

        if spec.satisfies("~simgrid"):
            if "^intel-mkl" in spec or "^intel-parallel-studio+mkl" in spec:
                if "threads=none" in spec:
                    args.extend([self.define("BLA_VENDOR", "Intel10_64lp_seq")])
                else:
                    args.extend([self.define("BLA_VENDOR", "Intel10_64lp")])
            elif "^netlib-lapack" in spec:
                args.extend([self.define("BLA_VENDOR", "Generic")])
            elif "^openblas" in spec:
                args.extend([self.define("BLA_VENDOR", "OpenBLAS")])

        return args


