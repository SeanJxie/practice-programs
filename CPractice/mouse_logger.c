#include <stdio.h>
#include <windef.h>


BOOL GetCursorPos(
        LPPOINT lpPoint
);


int main() {
    POINT mPos;
    FILE *fptr;
    fptr = fopen("MOUSE_LOG.txt", "w");

    if (fptr == NULL) {
        puts("File cannot be opened.");
        exit(1);
    }

    while (GetCursorPos(&mPos))
    {
        fprintf(fptr, "(%ld, %ld)\n", mPos.x, mPos.y);
        printf("(%ld, %ld)\n", mPos.x, mPos.y);
    }

    fclose(fptr);
    puts("An error has occurred.");
    return 0;
}
