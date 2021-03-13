/*  [Challenge] Sort a List of Numbers
    Created by : Tommy Tran / Python47(Discord)
    Date Created: 3/10/2020                  
    
    This one was difficult
    It can only do 0-9 integers
                                                 */


#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
  
    string num;

    cout << "Enter Numbers: ";
    cin >> num;

    //Convert string to array
    int n = num.length();
    char array[n+1];
    strcpy(array, num.c_str());

    //sort array (assending)
    sort(array, array+n);
    cout << array;

    return 0;
}
