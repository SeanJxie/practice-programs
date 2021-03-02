#include "matrix.h"


float dot(vector<float> v1, vector<float> v2)
{
    float res = 0.0;
    for (int i = 0; i < v2.size(); i++)
    {
        res += v1[i] * v2[i];
    }
    return res;
}


MxN::MxN(int m, int n)
{
    m_m = m;
    m_n = n;
    
    for (int i = 0; i < m; i++)
    {
        vector<float> col;
        for (int j = 0; j < m; j++)
        {
            col.push_back(0.0);
        }

        m_elems.push_back(col);
    }

}


void MxN::print()
{
    for (auto r : m_elems)
    {
        for (auto e : r)
        {
            std::cout << e << ' ';
        }

        std::cout << '\n';
    }

    std::cout << '\n';
}


vector<float> MxN::m_get_row(int i)
{
    return m_elems[i];
}


vector<float> MxN::m_get_col(int j)
{
    vector<float> col;
    for (auto r : m_elems)
    {
        col.push_back(r[j]);
    }

    return col;
}



MxN MxN::operator *(MxN o)
{
    if (m_n == o.m_m)
    {
        MxN resMat(m_m, o.m_n);
        for (int i = 0; i < m_n; i++)
        {
            for (int j = 0; j < o.m_n; j++)
            {
                vector<float> row = m_get_row(i);
                vector<float> col = o.m_get_col(j);
                resMat.m_elems[i][j] = dot(row, col);
            }
        }

        return resMat;
    }

    else
    {
        std::cout << "Invalid multiplicaton" << std::endl;
    }
}


MxN MxN::operator +(MxN o)
{
    MxN resMat(m_m, m_n);
    for (int i = 0; i < m_n; i++)
    {
        for (int j = 0; j < m_m; j++)
        {
            resMat.m_elems[i][j] = m_elems[i][j] + o.m_elems[i][j];
        }
    }

    return resMat;
}


MxN MxN::operator -(MxN o)
{
    // TODO Hard coded 3x1 matrix sub
  
    MxN resMat(m_m, m_n);
    for (int i = 0; i < m_m; i++)
    {
        for (int j = 0; j < m_n; j++)
        {
            resMat.m_elems[i][j] = m_elems[i][j] - o.m_elems[i][j];
        }
    }

    return resMat;
}