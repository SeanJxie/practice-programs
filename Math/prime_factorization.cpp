#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

vector<unsigned long long> pcSplit(unsigned long long i)
{
    int p = 2;
    while(i % p != 0)
    {
        p++;
    }

    vector<unsigned long long> ret = {p, i / p};
    return ret;
}

//18446744073709551615
bool isPrime(unsigned long long j)
{
    bool prime = true;

    for (unsigned long long div = 2; div <= pow(j, 0.5); div++)
    {
        if (j % div == 0)
        {
            prime = false;
        }
    }

    return prime;
}

vector<int> primeFactors(unsigned long long n)
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
            vector<unsigned long long> split = pcSplit(n);
            ends.push_back(split[0]);
            n = split[1];

            if (isPrime(split[1]))
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
    unsigned long long toFactor;

    cout << "Number to factor: ";
    cin >> toFactor;

    vector<int> primeFactorization = primeFactors(toFactor);
    printVector(primeFactorization);

    return 0;
}
