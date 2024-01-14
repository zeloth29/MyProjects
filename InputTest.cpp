#include <iostream>
using namespace std;
int main() {
  int x;
  string Name;
  cout << "What is your name?\n";
  cin >> Name;
  cout << "Type a number: "; // Type a number and press enter
  cin >> x; // Get user input from the keyboard
  cout << Name << " your number is: " << x; // Display the input value
}