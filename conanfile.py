from conans import ConanFile, CMake
import traceback

# Just replace `MySimpleProject` with your name
class MySimpleProject(ConanFile):
    name = "Learning Conan"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    requires = "catch/1.3.0@TyRoXx/stable", "backward/1.3.0@Manu343726/testing", "Poco/1.7.2@lasote/stable", "Boost/1.60.0@lasote/stable", "sfml/2.3.2@cpbotha/stable"
    # requires = "catch/1.3.0@TyRoXx/stable", "Poco/1.7.2@lasote/stable", "Boost/1.60.0@lasote/stable"
    generators = "cmake"
