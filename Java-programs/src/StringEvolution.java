import java.util.Random;
import java.util.Scanner;

/*
A program that takes an input string, creates a random-character string of the same length, then proceeds to "evolve"
the random string back to the original input string.
*/

public class StringEvolution {
    public static void main(String[] args) {
        System.out.print("Enter a target string: ");
        Scanner input = new Scanner(System.in);
        String targetString = input.nextLine().toLowerCase();

        char[] alphabet = {
                'a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', ' ', '.',
                ',', '?', '!', '(', ')', '—', '"',
                '/'
        };

        // Create random string with same length as input.
        StringBuilder buildString = new StringBuilder();
        Random randomIndex = new Random();
        int length = targetString.length();
        for (int c = 0; c < length; c++) {
            buildString.append(alphabet[randomIndex.nextInt(alphabet.length)]);
        }

        // Begin "evolution".
        String currentString = buildString.toString();
        while (!currentString.equals(targetString)) {
            for (int i = 0; i < length; i++) {

                if (currentString.charAt(i) != targetString.charAt(i)) {
                    currentString = replaceIndex(currentString, i, alphabet[randomIndex.nextInt(alphabet.length)]);
                }
            }

            System.out.println(currentString);
        }
    }

    public static String replaceIndex(String str, int idx, char chr) {
        char[] arrayString = str.toCharArray();
        arrayString[idx] = chr;

        return String.valueOf(arrayString);
    }
}
