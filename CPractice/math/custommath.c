#include "custommath.h"


double SquareRoot(int n, int decimalPlaces) {
    double upper, lower = (double) n / 4;

    while (1) {
        upper = n / lower;
        lower = (lower + upper) / 2;

        if (NewPrecision(lower, decimalPlaces) == NewPrecision(upper, decimalPlaces)) {
            break;
        }
    }

    return lower;
}

double exponent(double n, int e) {
    double res = 1;
    for (int _ = 0; _ < e; _++) {
        res *= n;
    }

    return res;
}


double intpart(double n) {
    int i = 0;
    while (i < n) {
        i++;
    }

    return i;
}

double NewPrecision(double n, int p) {
    return intpart(exponent(10, p) * n) / exponent(10, p);
}


int IsPrime(int n) {
    if (n <= 1) {
        return 0;
    }

    // In the case of prime searching, rounding square root to 0 decimals is fine.
    for (int i = 2; i < SquareRoot(n, 0) + 1; i++) {
        if (n % i == 0) {
            return 0;
        }
    }

    return 1;
}

int Fibonacci(int t) {
    int computed[t], curr;
    computed[0] = 0;
    computed[1] = 1;
    for (int i = 0; i < t; i++) {
        curr = computed[i] + computed[i + 1];
        computed[i + 2] = curr;
    }

    return curr;
}


double riemann_sum(double (*f)(double), int a, int b, int n) {
    double delta_x = (double) (b - a) / n, area = 0;
    for (int i = 1; i <= n; i++) {
        area = area + f(a + i * delta_x) * delta_x;
    }
    return area;
}