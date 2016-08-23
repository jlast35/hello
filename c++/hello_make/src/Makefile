SHELL = /bin/sh
# Comments in a Makefile begin with a hash tag

# We can store stuff like the compiler to use and compiler flags in macro variables like so:

# Compiler to use:
CXX = g++

# We're going to keep our .h and .o files in separate folders from the source
IDIR = ../include
ODIR = obj

# Compiler flags:  ( -I. means to look in the current folder for .h files )
CXXFLAGS = -I$(IDIR)

SOURCES = hello_world.cpp
EXECUTABLE = hello_world

# Dependencies:  ( putting .o files in the dependency causes make to compile the corresponding .cpp files individually before creating the .exe
_DEPS = $(SOURCES:.cpp=.h)
DEPS = $(_DEPS:%=$(IDIR)/%)
# DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

_OBJ = $(SOURCES:.cpp=.o)
# OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))
OBJ = $(_OBJ:%=$(ODIR)/%)


# Then we use the syntax $(macro_variable) to dereference their values

# The rule says that:
# All .o files depend upon the .cpp version of the same file and the .h files included in the DEPS macro. 
# To generate the .o file, make needs to compile the .cpp file using the compiler defined in the CC macro
# The -c flag says to generate the object file, 
# the -o $@ says to put the output of the compilation in the file named on the left side of the :, 
# the $< is the first item in the dependencies list
$(ODIR)/%.o: %.cpp $(DEPS)
	$(CXX) -c -o $@ $< $(CXXFLAGS)

# $@ and $^ are the left and right sides of the : respectively
$(EXECUTABLE): $(OBJ) 
	$(CXX) -o $@ $^ $(CXXFLAGS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o 
