// Comments begin with double slashes in C++

//      Multi-line comments are surrounded by /*  */

/* 
    This is a multi-line
    comment.
 */

// All statements must end in a semi-colon. (except comments)

// Statement blocks are surronded by curly braces 
// {
//    statement1
//    statement2
//    ...  
// }

// You have to include iostream.h to be able to use std::cout
// -In the new style C++ you don't need to put the .h in the #include  
// The angle brackets cause the pre-compiler to search all paths in the PATH environment variable 
// for a matching header file
#include <iostream>

// You can do this to avoid having to type std::cout 
// every time you want to use cout
using namespace std;

// There must be a function named main in order to be executable
// main must return an integer
int main () 
{
	cout << "Hello World!\n"; // We are sending the string literal "Hello World!" as input to the special console output file std::cout

	// The exit code of the last statement is returned implicitly if you omit an explicit 'return 0;' statement.
	// This only applies to main()
	// return 0;
}
// end main
