#!/usr/bin/env bash
rm -rf build
mkdir build && cd build
# export DYLD_LIBRARY_PATH=.:$DYLD_LIBRARY_PATH
# export DYLD_FALLBACK_LIBRARY_PATH=.:$DYLD_FALLBACK_LIBRARY_PATH
conan install .. -s compiler=apple-clang -s compiler.version=8.1 -s compiler.libcxx=libc++ --build=missing
cmake ..
cmake --build .
ctest -V
