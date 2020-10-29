#include <stdio.h>

/*
 * p[index] == *(p + index).
 */


int *BubbleSort(int *array, int size) {
    int i, temp, swap = 1;
    while (swap) {
        swap = 0;
        for (i = 1; i < size; i++) {
            if (array[i - 1] > array[i]) {
                temp = array[i - 1];
                array[i - 1] = array[i];
                array[i] = temp;
                swap = 1;
            }
        }
    }

    return array;
}

int main() {
    int array[] = {5, 2, 8, 124, 1, 100, 212, 0, -1, 12}, *sorted = BubbleSort(array, 10);

    for (int i = 0; i < 10; i++) {
        printf("%d\n", sorted[i]);
    }

    return 0;
}