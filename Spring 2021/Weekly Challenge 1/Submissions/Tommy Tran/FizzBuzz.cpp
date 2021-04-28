/*  [Challenge] Fizz Buzz
    Created by : Tommy Tran / Python47(Discord)
    Date Created: 2/24/2020                     */

#include <iostream>

using namespace std;

int main() {

    for (int i = 1; i <= 100; i++) {

        //Multiple by 3 and 5
        if (i % 15 == 0) {
            cout << i << " - FizzBuzz\n";
        }

        //Multiple by 3
        else if ((i % 3) == 0) {
            cout << i << " - Fizz\n";
        }

        //Multiple by 5
        else if ((i % 5) == 0) {
            cout << i << " - Buzz\n";
        }
    }
    return 0;
}
