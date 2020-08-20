#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <math.h>

using namespace std;

bool checkValid(vector<int> C, int R)
{
    int res = 1;
    for (int i = 0; i < C.size(); i++)
    {
        res *= C[i];
    }

    if (res == R)
    {
        return true;
    }

    else
    {
        return false;
    }
}

vector<int> generateD(int n, int s)
{
    vector<int> deck;

    for (int i = 1; i <= n; i++)
    {
       for (int _ = 1; _ <= s; _++)
       {
           deck.push_back(i);
       }
    }

    return deck;
}

vector<int> generateRandomC(vector<int> D, int k)
{
    vector<int> C;

    for (int _ = 1; _ <= k; _++)
    {
        C.push_back(D[rand() % D.size()]);
    }

    return C;
}

double runTest(vector<int> D, int n, int k, int s, int R, int samples)
{
     // Test variables
    double valid = 0, total = 0;

    for (int _ = 1; _ <= samples; _++)
    {
        vector<int> randomC = generateRandomC(D, k);

        if (checkValid(randomC, R))
        {
            valid++;
        }

        total++;
    }

    return valid / total * 100;
}

int main()
{
    // Variables defined in paper.
    int n = 13, k = 4, s = 4, R = 24, testSamples = 10000, testQuantity = 10000;
    vector<int> D = generateD(n, s);

    double testSum;

    for (int testRuns = 1; testRuns <= testQuantity; testRuns++)
    {
        double result = runTest(D, n, k, s, R, testSamples);
        testSum += result;

        double testAverage = testSum / testRuns;

        cout << "Test #" << testRuns << ", Res: " << result << ", Avg: " << testAverage << "\r" << flush;
    }

    return 0;
}
