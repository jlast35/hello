# SHELL = /bin/sh
# Not sure the shell variable even gets used - nope, it doesn't.

# Comments in a Makefile begin with a hash tag

# We can store stuff like the C++ compiler to use in macro variables like so:
# (Note: there's nothing syntactically special about the variable names themselves other than convention)
# Compiler to use:
CXX = g++

# We're going to keep our .h and .o files in separate folders from the source
IDIR = ../include
ODIR = obj

# Compiler flags:  ( -I. means to look in the current folder for .h files )
# Use the syntax $(macro_variable) to expand a macro.
# https://www.gnu.org/software/make/manual/html_node/Reference.html#Reference

CXXFLAGS = -I$(IDIR)

SOURCES = hello_world.cpp
EXECUTABLE = hello_world

# Dependencies:  ( putting .o files in the dependency causes make to compile the corresponding .cpp files individually before creating the .exe

# https://www.gnu.org/software/make/manual/html_node/Substitution-Refs.html#Substitution-Refs
# We can use substitution references $(var:original=substitute) 
# and even pattern substitution references $(var:%original=%substitute)
# when expanding variables.
# The first % expands to any matching nonempty substring in the variable
# The second % expands to the value of the first %.

# All .cpp files in sources have a corresponding .h file
_DEPS = $(SOURCES:.cpp=.h)
# Prefix every corresponding .h file with the relative path to the include directory
DEPS = $(_DEPS:%=$(IDIR)/%)
# Same as the previous line, but more awkward syntax:
# DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

# All .cpp files in sources have a corresponding .o file after they are compiled
_OBJ = $(SOURCES:.cpp=.o)
# Prefix every corresponding .o file with the relative path to the objects directory
OBJ = $(_OBJ:%=$(ODIR)/%)
# Same as the previous line, but more awkward syntax:
# OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))

# https://www.gnu.org/software/make/manual/html_node/Pattern-Rules.html#Pattern-Rules
# The use of exactly one % in a target creates a pattern rule.  In the target, % matches any non-empty substring.
# When it is also used in the dependencies list, % refers to the same string as the target matched

# Then we use the syntax $(macro_variable) to dereference their values

# The rule says that:
# All .o files depend upon the .cpp version of the same file and the .h files included in the DEPS macro. 
# To generate the .o file, make needs to compile the .cpp file using the compiler defined in the CC macro
# The -c flag says to generate the object file, 
# the -o $@ says to put the output of the compilation in the file named on the left side of the :, 
# the $< is the first item in the dependencies list

# https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html#Automatic-Variables
# Defines special variables like:  $@  $<  $^

# Rules have the following general form:
#
# BUILD_TARGET: BUILD_DEPENDENCIES
# 	RECIPE
#
# Note that all recipe lines must start with a tab. 
# Recipe lines will be executed by the shell (Bash) following any necessary Makefile macro expansion.
# "If the target file does not exist, or any of the build dependencies are newer than it, run the recipe"

# The recipes for all prerequisites of a target will be completed before the recipe for the target is run. 
# If any prerequisite is newer than the target, then the target is considered out-of-date and must be rebuilt.
# All dependencies listed to the right of a | are "order only" dependencies.
# This means their timestamps are not checked to see whether a newer version exists - only that it already exists.
# In the example below, "don't start compiling cpp files to objects until an objects directory exists"

# $@ and $^ are the left and right sides of the : respectively

# The first recipe encountered is the "default goal".  
# The default goal is the recipe that builds when you invoke "make" with no parameters
# Other recipes do not build unless they are dependencies of the "default goal".

# Dependencies get resolved recursively.  
# If a dependency file is in turn listed as the build target of another rule, that rule's dependencies are also processed.
# So, generally, you want to start with the final executable and recurse down from there.

# The default goal:
# --------------------------------------
$(EXECUTABLE): $(OBJ)
	$(CXX) -o $@ $^ $(CXXFLAGS)
# --------------------------------------
$(ODIR)/%.o: %.cpp $(DEPS) | $(ODIR)
	$(CXX) -c -o $@ $< $(CXXFLAGS)

# create a separate object directory
$(ODIR):
	mkdir $(ODIR)

# This means that "clean" is not the name of a file, so don't check for a file named "clean" when passed this build target.
# The only way a PHONY target should be able to be processed is if it is passed as a command line argument to "make"
# For example, "make clean"
.PHONY: clean

clean:
	rm -rf $(ODIR)
	if [ -f $(EXECUTABLE) ]; then rm $(EXECUTABLE); fi
