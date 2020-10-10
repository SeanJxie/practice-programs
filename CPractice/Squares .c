#include <math.h>
#include <stdio.h>

int notmain3() {
    int sl;
    scanf("%d", &sl);
    printf("The largest square has side length %d.", (int) floor(sqrt(sl)));

    return 0;
}