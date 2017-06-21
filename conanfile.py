from conans import ConanFile, CMake
import traceback

# Just replace `MySimpleProject` with your name
class MySimpleProject(ConanFile):
    name = "Learning Conan"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    requires = ("catch/1.5.0@TyRoXx/stable",
        "backward/1.3.0@Manu343726/testing",
        "Poco/1.7.5@lasote/stable",
        "Boost/1.62.0@lasote/stable",
        "easyloggingpp/9.80@memsharded/testing",
        "CppRestSdk/2.9.0@BleuGamer/stable")
    generators = "cmake"

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin") # From bin to bin
        self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin
     #   self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin



    # default_options = "Poco:shared=True", "OpenSSL:shared=True"
    # requires = "catch/1.5.0@TyRoXx/stable", "backward/1.3.0@Manu343726/testing", "Poco/1.7.2@lasote/stable", "Boost/1.60.0@lasote/stable", "sfml/2.3.2@cpbotha/stable", "easyloggingpp/9.80@memsharded/testing"

# DYLD_LIBRARY_PATH