# C++ Conan Demo

## Setup and configure

```bash
brew install conan
mkdir build && cd build
conan install .. -s compiler=apple-clang -s compiler.version=8.1 -s compiler.libcxx=libc++ --build=missing
cmake ..
cmake --build .


# TO test:
ctest -V
```

Note that there is now an `init.sh` file that I'm using for quick testing

## Alternatives

```
conan install .. -s compiler=clang -s compiler.version=3.6 -s compiler.libcxx=libstdc++ --build=missing
conan install -s compiler=gcc -s compiler.version=5.3 -s compiler.libcxx=libstdc++11 --build=missing
```

Base example drawn from multiple sources online:

* [MS C++ ReST SDK](https://github.com/Microsoft/cpprestsdk)
* [A Timer using POCO libraries](http://docs.conan.io/en/latest/getting_started.html#a-timer-using-poco-libraries)
* [Learning Poco GET with HTTP](https://www.codeproject.com/Articles/252566/Learning-Poco-GET-with-HTTP)
* [Backward Stack Trace Library](https://github.com/bombela/backward-cpp)
* [Conan: C++ Package manager](https://www.conan.io/)
* [Conan and CLion Setup](http://blog.conan.io/2016/05/10/Programming-C++-with-the-4-Cs-Clang,-CMake,-CLion-and-Conan.html)
* [Conan: Setting up a simple conan project](http://chaosteil.gitlab.io/2016/04/12/Setting-up-a-simple-Conan-project/)
* [Catch: C++ Test Framework](https://github.com/philsquared/Catch/blob/master/docs/tutorial.md)
