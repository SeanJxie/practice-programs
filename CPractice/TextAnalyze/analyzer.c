#include <stdio.h>
#include <stdlib.h>
#include "analyzer.h"

uint word_count(const char *string, uint size) {
    uint sCount = 0;
    for (uint i = 0; i < size; i++) {
        if (string[i] == ' ') {
            sCount++;
        }
    }
    return sCount + 1;
}


const char *get_file_str(const char *path, const char *mode) {
    FILE *fPtr = fopen(path, mode);

    if (fPtr == NULL) {
        printf("Error reading file.");
        exit(EXIT_FAILURE);
    }

    static char buffer[BUFFERSIZE];
    fgets(buffer, BUFFERSIZE, fPtr);

    return buffer;
}