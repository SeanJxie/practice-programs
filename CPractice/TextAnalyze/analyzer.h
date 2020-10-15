#include <stdio.h>

#ifndef TEXTANALYZE_ANALYZER_H
#define TEXTANALYZE_ANALYZER_H

#define BUFFERSIZE 1000

typedef unsigned uint;

typedef struct {
    const char *text;
    uint wordCount;
} TextFile;


// Assumes anything separated by space is a word.
uint word_count(const char *string, uint size);

const char *get_file_str(const char *path, const char *mode);


#endif //TEXTANALYZE_ANALYZER_H
