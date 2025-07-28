from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import get
from conan.tools.cmake import CMakeToolchain
import os
import subprocess
required_conan_version = ">=1.51.1"


class ModernDurakUnrealCxx(ConanFile):
    name = "modern_durak_game"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False],"disable_multiplayer": [True, False]}
    default_options = {"shared": False, "fPIC": True, "disable_multiplayer": False}
    generators = "CMakeDeps"

    def generate(self):
        tc = CMakeToolchain(self)
        tc.user_presets_path = False #workaround because this leads to useless options in cmake-tools configure
        tc.variables["MODERN_DURAK_GAME_DISABLE_MULTIPLAYER"] = self.options.disable_multiplayer
        tc.generate()

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        self.options["catch2"].with_main = True
        self.options["catch2"].with_benchmark = True

    def requirements(self):
        self.requires("durak/1.2.0",force=True,transitive_headers=True)
        self.requires("magic_enum/0.9.6")
        self.requires("boost/1.86.0",force=True,transitive_headers=True)
        self.requires("confu_json/[>=1.1.1 <2]@modern-durak",force=True)
        self.requires("confu_soci/1.0.0",force=True)
        self.requires("sml/1.1.8") #DO NOT CHANGE THIS. starting with version 1.1.9 process_event returns ins some cases false where before it returned true
        self.requires("durak_computer_controlled_opponent/2.2.2")
        self.requires("corrade/2025.06")
        self.requires("modern_durak_game_shared/latest",transitive_headers=True)
        self.requires("my_web_socket/1.0.0",transitive_headers=True)


    def source(self):
        token = os.getenv("GIT_TOKEN_MODERN_DURAK_GAME")
        if not token:
            raise Exception("Missing GIT_TOKEN_MODERN_DURAK_GAME environment variable")

        user = "werto87"
        repo_name = "modern_durak_game"
        tag = f"v{self.version}"  # Add 'v' prefix to version
        url = f"https://{token}@github.com/{user}/{repo_name}.git"
        self.output.info(f"Cloning tag '{tag}' from {user}/{repo_name}")
        subprocess.run([
            "git", "clone", "--branch", tag, "--depth", "1", url, "."
        ], check=True)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def layout(self):
        cmake_layout(self, src_folder=self.name + "-" + str(self.version))

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.components[self.name].requires = ["durak::durak","modern_durak_game_shared::modern_durak_game_shared","corrade::corrade","durak_computer_controlled_opponent::durak_computer_controlled_opponent","sml::sml","my_web_socket::my_web_socket", "boost::headers","boost::json","boost::filesystem","confu_soci::confu_soci","confu_json::confu_json","magic_enum::magic_enum"]
        self.cpp_info.components[self.name].libs = [self.name]
        
