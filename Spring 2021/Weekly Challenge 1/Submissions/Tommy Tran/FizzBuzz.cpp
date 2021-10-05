/*  [Challenge] Fizz Buzz
    Created by : Tommy Tran / Python47(Discord)
    Date Created: 2/24/2020                     */

#include <iostream>
using namespace std;

int main(){

    for (int i = 1; i <= 100; i++){

        if (i % 15 == 0){ //Multiple by 3 and 5
            cout << i << " - FizzBuzz\n";
        }
        else if ((i % 3) == 0){ //Multiple by 3
            cout << i << " - Fizz\n";
        }
        else if ((i % 5) == 0){ //Multiple by 5
            cout << i << " - Buzz\n";
        }
        else{ //Return i if not divisible
            cout << i << " \n";
        }
    }
return 0;
}
