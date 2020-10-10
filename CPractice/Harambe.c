#include <stdio.h>
#include <string.h>

#define MAX 1000

int notmain2() {
    char s[MAX], t[MAX];
    int k;
    fgets(s, MAX, stdin);
    fgets(t, MAX, stdin);
    scanf("%d", &k);
    for (unsigned i = 0; i < strlen(s); i++) {
        if (s[i] != t[i]) {
            if (s[i] == ' ' || t[i] == ' ') {
                k = -1;
                break;
            }
            k--;
        }
    }
    if (k >= 0) {
        printf("Plagiarized");
    } else {
        printf("No plagiarism");
    }
    return 0;
}