#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "vector3d.h"

#define INPUT_BUFFER 100

typedef struct {
    float f;
    Vector3D vec;
    char current_type;
} vec_return_type;


void cvt_upper(char *s) {
    for (int i = 0; s[i]!='\0'; i++) { // Iterate through string until '\0' terminating null char.
      if(s[i] >= 'a' && s[i] <= 'z') { // Make sure char is a letter.
         s[i] = s[i] - 32;             // Shift ASCII value to upper case.
      }
   }
}

int main() {
    char cmd[INPUT_BUFFER], input[INPUT_BUFFER], op;
    Vector3D v1, v2;
    vec_return_type return_value;

    while (1) { // Main loop.
        printf("Enter 3D vector operation (ADD/SUB/DOT/CROSS/NORM/MAG/QUIT): ");
        fgets(cmd, INPUT_BUFFER, stdin); // Reads a '\n' on "ENTER" press. Remember this when calling strcmp.
        cvt_upper(cmd); // Convert to upper case.
        
        if (strcmp(cmd, "ADD\n") == 0 || strcmp(cmd, "SUB\n") == 0 || strcmp(cmd, "DOT\n") == 0 || strcmp(cmd, "CROSS\n") == 0) {   
            // VEC 1.
            printf("Enter x-value of first vector: ");
            fgets(input, INPUT_BUFFER, stdin);
            v1.x = atof(input);
            printf("Enter y-value of first vector: ");
            fgets(input, INPUT_BUFFER, stdin);
            v1.y = atof(input);
            printf("Enter z-value of first vector: ");
            fgets(input, INPUT_BUFFER, stdin);
            v1.z = atof(input);
            // VEC 2.
            printf("Enter x-value of second vector: ");
            fgets(input, INPUT_BUFFER, stdin);
            v2.x = atof(input);
            printf("Enter y-value of second vector: ");
            fgets(input, INPUT_BUFFER, stdin);
            v2.y = atof(input);
            printf("Enter z-value of second vector: ");
            fgets(input, INPUT_BUFFER, stdin);
            v2.z = atof(input);

            if (strcmp(cmd, "ADD\n") == 0) {
                return_value.vec = add_vec(v1, v2);
                return_value.current_type = 'V';
            } 

            else if (strcmp(cmd, "SUB\n") == 0) {
                return_value.vec = sub_vec(v1, v2);
                return_value.current_type = 'V';
            }

            else if (strcmp(cmd, "DOT\n") == 0) {
                return_value.f = dot(v1, v2);
                return_value.current_type = 'F';
            }

            else {
                return_value.vec = cross(v1, v2);
                return_value.current_type = 'V';
            }
            
            if (return_value.current_type == 'V') {
                printf("RESULT: ");
                print_vec(return_value.vec);        
            }

            else {
                printf("RESULT: ");
                printf("%f\n", return_value.f);
            }
        
        } 

        else if (strcmp(cmd, "NORM\n") == 0 || strcmp(cmd, "MAG\n") == 0) {
            printf("Enter x-value of vector: ");
            fgets(input, INPUT_BUFFER, stdin);
            v1.x = atof(input);
            printf("Enter y-value of vector: ");
            fgets(input, INPUT_BUFFER, stdin);
            v1.y = atof(input);
            printf("Enter z-value of vector: ");
            fgets(input, INPUT_BUFFER, stdin);
            v1.z = atof(input);

            // No use of vec_return_type here since there is only one of each type.
            if (strcmp(cmd, "NORM\n") == 0) {
                printf("RESULT: ");
                print_vec(normalize(v1));    
            }

            else {
                printf("RESULT: ");
                printf("%f\n", magnitude(v1));
            }
        }

        else if (strcmp(cmd, "QUIT\n") == 0) {
            exit(EXIT_SUCCESS);
        }

        else {
            printf("UNRECOGNIZED COMMAND\n");
        }
    }  

    return 0;
}