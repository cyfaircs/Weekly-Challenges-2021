/*  [Challenge] Print all Factors
    Created by : Tommy Tran / Python47(Discord)
    Date Created: 3/10/2020                     */

#include <iostream>

using namespace std;

int main() {
    
    int num;

    cout << "Enter an integer: ";
    cin >> num;

    cout << "The factors are: ";

    for (int i = 1;i <= num;i++){
        if(num % i == 0){
            cout << i << " ";
        }
    }
    return 0;
}
