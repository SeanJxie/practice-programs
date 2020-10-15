#include <stdio.h>
#include <string.h>
#include "analyzer.h"

int main() {
    TextFile myFile;
    const char *fPath;
    myFile.text = get_file_str(fPath, "r");
    myFile.wordCount = word_count(myFile.text, strlen(myFile.text));
    printf("Text: %s\nWord Count: %d", myFile.text, myFile.wordCount);

    return 0;
}
