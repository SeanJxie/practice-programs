/*

An implementation of bubble sort in Java.

 */

public class BubbleSort {
    public static void main(String[] args) {
        int[] array = {5, 1, 3, 5, 1, 4, 5, 1, 234234, 2873423, 0}; // Input array.

        boolean sorted = false;

        while (!sorted) {
            printArray(array);

            sorted = true; // Assume the array is sorted.
            for (int i = 0; i < array.length - 1; i++) { // Iterate through the entire array.
                if (array[i] > array[i + 1]) { // If the current value is less than the next value,
                    int tempValue = array[i];  // Set a temporary value equal to the current one.
                    array[i] = array[i + 1];   // Set the current value to the next value.
                    array[i + 1] = tempValue;  // Set the next value to the temporary value.

                    sorted = false; // The array is not sorted yet because a swap has been made.
                }
            }
        }
    }

    public static void printArray(int[] arr) { // Print an integer array.
        for (int value : arr) {
            System.out.print(value);
            System.out.print(' ');
        }

        System.out.print('\n');
    }
}
