#include <stdio.h>
#include "custommath.h"


int main() {
    const int MAX = 40;

    for (int n = 0; n < MAX; n++) {
        printf("%u\n", Fibonacci(n));
    }

    return 0;
}
