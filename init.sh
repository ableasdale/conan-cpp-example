mkdir build && cd build
conan install .. -s compiler=apple-clang -s compiler.version=8.1 -s compiler.libcxx=libc++ --build=missing
cmake ..
cmake --build .
ctest -V
