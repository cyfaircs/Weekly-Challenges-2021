/*  [Challenge] Fibonacci and Continued
    Created by : Tommy Tran / Python47(Discord)
    Date Created: 2/24/2020                     */

#include <iostream>
#include <cmath>
using namespace std;

int fibonacci(int n);
int odd_Fibonacci(int n);

int main() {

    cout << "Enter 1: Fibonacci Program\n"
        << "Enter 2: Fibonacci Continued\n \n";

    int choice = 0, n = 0;

    cout << "Choice: ";
    cin >> choice;
    switch (choice) {

    case 1:
        cout << "Fibonacci Program\n \n";

        cout << "Please enter a fibonacci position number: ";
        cin >> n;
        cout << "Fibonacci Number: " << fibonacci(n) << "\n";
        break;

    case 2:
        cout << "Fibonacci Continued (Sums all odd n between 0 to n)\n \n";

        cout << "Please enter a fibonacci position number: ";
        cin >> n;
        cout << "Fibonacci Sum: " << odd_Fibonacci(n) << "\n";
        break;
    }
    return 0;
}

 
int fibonacci(int n) {
    if (n == 0) {
        return 0;
    }
    else if (n == 1) {
        return 1;
    }
    else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int odd_Fibonacci(int n) {
    int previous = 0;
    int current = 1;
    int result = 0;
    while (current <= n) {
        if (current % 2 != 0) {
            result += current;
        }
        current += previous;
        previous = current - previous;
    }
    return result;
}
