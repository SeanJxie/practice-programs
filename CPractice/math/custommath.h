#ifndef MATH_CUSTOMMATH_H
#define MATH_CUSTOMMATH_H


double SquareRoot(int n, int decimalPlaces);

double exponent(double n, int e);

double intpart(double n);

double NewPrecision(double n, int p);

int IsPrime(int n);

int Fibonacci(int t); // MAX 2147483647

double riemann_sum(double (*f)(double), int a, int b, int n);

#endif //MATH_CUSTOMMATH_H
