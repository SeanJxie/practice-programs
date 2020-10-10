#include <stdio.h>

int smain() {
    unsigned a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if (a == b) {
        printf("%d", c - a);
    } else {
        printf("%d", (a - b) * (1 - 2 * (b > a))); // absolute value func is for the weak
    }


    return 0;
}