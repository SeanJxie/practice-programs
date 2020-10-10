#include <stdio.h>

#define TRUE  1
#define FALSE 0

typedef int bool;

int main() {
    int n;
    scanf("%d", &n);
    int array[n], temp;
    bool swapMade = TRUE;

    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    while (swapMade) {
        swapMade = FALSE;
        for (int i = 0; i < n - 1; i++) {
            if (array[i] > array[i + 1]) {
                temp = array[i + 1];
                array[i + 1] = array[i];
                array[i] = temp;
                swapMade = TRUE;
            }
        }
    }

    printf("Done.");
    /*
    for (int i = 0; i < n; i++) {
        printf("%d\n", array[i]);
    }
    */

    return 0;
}