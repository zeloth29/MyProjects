#include <iostream>
#include <cmath>
#include <cstdlib>

/*
THIS MUST BE RAN IN DEBUGGER IN ORDER TO WORK!
*/

int main() {
  int Number;
  int Binary;
  //std::cout<< pow(2,4);
  std::cout << "Enter a Denary number to be converted to Binary\n";
  std::cin >> Number;
  for(int i = 7; i >= 0; i=i-1)
    {
      // std::cout<< i << "\n";
      if(Number >= pow(2,i)){
        Number = Number - pow(2,i);
        // std::cout<< Number<< "\n";
        Binary = Binary + pow(10,i);
        // std::cout<< Binary << "\n";
      }
      else{
        
      }
    }
  std::cout<<Binary;
}