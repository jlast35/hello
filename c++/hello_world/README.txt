How to compile:

g++ hello_world.cpp -o hello_world.exe

Note: use g++ specifically to compile C++ code - not gcc (even though it can)


Easier still, for simple one file projects, you can also just do:

make hello_world

(even if there is no Makefile, as long as the arg is the same name minus extension as the cpp file)

