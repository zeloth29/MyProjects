#include <iostream>

using namespace std;
int main() {
  string Phrase;
  cout << "This is a Ceasar Cipher\n";
  cout << "Enter your sentence.\n>";
  cin >> Phrase;
  cout << "Length: " << Phrase.length() << "\n";
  int Shift = 2;
  for(int i = 0; i < Phrase.length(); i++){
    char current;
    current = Phrase[i];
    current = int(current)+Shift;
    Phrase[i] = char(current);
  }
  cout << Phrase;
}