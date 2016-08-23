#include <iostream>
// #include <boost/math/special_functions/round.hpp>
#include <cmath>

using namespace std;
int main()
{
	string greeting = "Hello World\n";
	cout << greeting;
	// int test1 = boost::math::iround(0.49999999999999994);
	int test2 = round(23/(double)40/1);
	int test3 = round((float)6/5);
	//int test3 = round(test2);
	// cout << test1;
	cout << test2 << std::endl;
	cout << test3;
	//cin.get();
}
