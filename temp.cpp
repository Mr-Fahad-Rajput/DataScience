#include <iostream>

using namespace std;

int main()
{
    float litres, producingCost, profit;
    int cartons;

    cout << "Enter Total amount of milk produced in Litres: "; 
    cin >> litres;
    cartons = litres/5.28;
    cout << "Total Number of Cartons Is :" << cartons << endl; 
    producingCost = litres*1.18;
    cout << "Total Producing Cost of milk produced is: $"<< producingCost << endl; 
    profit = cartons*(0.95);
    cout << "Total Profit on the Produced Milk is: $"<< profit << endl; 

    return 0;
}
