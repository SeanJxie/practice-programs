#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

vector<int> pcSplit(int i)
{
    int p = 2;
    while(i % p != 0)
    {
        p++;
    }

    vector<int> ret = {p, i / p};
    return ret;
}

bool isPrime(int j)
{
    bool prime = true;

    for (int div = 2; div <= pow(j, 0.5); div++)
    {
        if (j % div == 0)
        {
            prime = false;
        }
    }

    return prime;
}

vector<int> primeFactors(int n)
{
    vector<int> ends;

    if (n <= 1)
    {
        return ends;
    }

    else
    {
    while (true)
        {
            vector<int> split = pcSplit(n);
            ends.push_back(split[0]);
            n = split[1];

            if (isPrime(split[0]) && isPrime(split[1]))
            {
                ends.push_back(split[1]);
                break;
            }
        }
    }


    return ends;
}

string printVector(vector<int> vec)
{
    for(int i = 0; i < vec.size(); ++i)
        cout << vec[i] << ' ';
}

int main()
{
    int toFactor;

    cout << "Number to factor: ";
    cin >> toFactor;

    vector<int> primeFactorization = primeFactors(toFactor);
    printVector(primeFactorization);
}
