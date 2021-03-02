#ifndef MATRIX_H
#define MATRIX_H

#include <vector>
#include <stdlib.h>
#include <iostream>
#include <math.h>

using namespace std;

float dot(vector<float> v1, vector<float> v2);

class MxN
{
public:
    MxN(int m, int n);

    vector<vector<float>> m_elems;

    void print();
    vector<float> m_get_row(int i);
    vector<float> m_get_col(int j);
    
    MxN operator *(MxN o);
    MxN operator +(MxN o);
    MxN operator -(MxN o);

    int m_m; // Row
    int m_n; // Col
};



#endif