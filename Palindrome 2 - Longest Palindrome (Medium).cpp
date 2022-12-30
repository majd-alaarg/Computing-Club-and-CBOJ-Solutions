/*PROBLEM START*/

//Given a string S, please determine the longest palindromic substring in S. A palindrome is a sequence of letters that is the same when read forwards or backwards.
//For this problem, Python users are recommended to use PYPY over CPython.

//Input Specification
//The first and only line will contain a string S consisting of lowercase letters in the English alphabet. This time, the length of S will not exceed 10^3 letters (1≤|S|≤10^3).

//Output Specification
//On a single line output an integer indicating the longest palindromic substring's length.

/*PROBLEM END*/

#include <bits/stdc++.h>
using namespace std;
 
// Function to obtain the length of
// the longest palindromic substring
int longestPalSubstr(string str)
{
    // Length of given string
    int n = str.size();
 
    // Stores the maximum length
    int maxLength = 1, start = 0;
 
    // Iterate over the string
    for (int i = 0;
         i < str.length(); i++) {
 
        // Iterate over the string
        for (int j = i;
             j < str.length(); j++) {
            int flag = 1;
 
            // Check for palindrome
            for (int k = 0;
                 k < (j - i + 1) / 2; k++)
                if (str[i + k]
                    != str[j - k])
                    flag = 0;
 
            // If string [i, j - i + 1]
            // is palindromic
            if (flag
                && (j - i + 1) > maxLength) {
                start = i;
                maxLength = j - i + 1;
            }
        }
    }
 
    // Return length of LPS
    return maxLength;
}
 
// Driver Code
int main()
{
    // Given string
    string str;
 cin >> str;
    // Function Call
    cout << longestPalSubstr(str);
    return 0;
}
