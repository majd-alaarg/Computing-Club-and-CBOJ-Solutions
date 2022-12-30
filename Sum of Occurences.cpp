/*PROBLEM START*/

//Bob was given a strange task by his teacher today:

//Given a string consisting of lowercase letters, find the sum of occurrences of each letter.

//Bob got too confused to solve this task. Can you do it for Bob instead?

//Input Specification
//The first line of the input will contain an integer N (1≤N≤107), indicating the length of the string

//The next line of the input is a string consisting of lowercase alphabet letters.

//Output Specification
//Output an integer, representing the sum of occurrences for all letters in the string.

/*PROBLEM END*/

#include <iostream>

int main() {
  std::string length;
   std::string last;
 
  getline(std::cin, length);
 
  std::cin.ignore(0,' ');   // ignore until space
  last = std::cin.get();      // get one character

   std::cout << length;
   return 0;
}
