/*  [Challenge] Is Prime?
    Created by : Tommy Tran / Python47(Discord)
    Date Created: 3/10/2020                     */

#include <iostream>

using namespace std;

int main() {
    
    int num;

    cout << "Enter an integer: ";
    cin >> num;

    //Check for 0 and 1
    if (num == 0 || num == 1){
        cout << num << " is not prime";
        return 0;
    }
    else{
        //check if divisible by i
        for (int i = 2; i<= num; i++){
            if (num % i == 0){
                cout << num << " is not prime";
                break;
            }
            else{
                // else prime
                cout << num << " is prime";
            }
        break;
        }
    }
    return 0;
}
