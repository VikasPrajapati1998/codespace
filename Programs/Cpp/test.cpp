#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
    cout << "Name and Age printer."<<endl;
    string name;
    int age;

    cout << "Enter Name : ";
    cin >> name;
    cout << "Enter Age : ";
    cin >> age;

    cout << "Your name is "<<name<<" and age is "<<age<<endl;
    
    return 0;
}