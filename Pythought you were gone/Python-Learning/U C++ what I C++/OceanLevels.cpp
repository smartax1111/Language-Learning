#include <iostream>
#include <string>
using namespace std;
int find();

int find(float a, int b) {
    cout << "In " << b << " years the ocean's level will be higher by " << a * b << " millimeters.\n";
}

int main()
{
    find(1.5, 5);
    find(1.5, 7);
    find(1.5, 10);
    return 0;
} 