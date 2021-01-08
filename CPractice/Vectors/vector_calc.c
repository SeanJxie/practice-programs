#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "vector3d.h"

#define INPUT_BUFFER 10

typedef union {
    float f;
    Vector3D vec;
    char current_type;
} vec_return_type;


int main() {
    char cmd[INPUT_BUFFER], input[INPUT_BUFFER], op;
    Vector3D v1, v2;
    vec_return_type return_value;

    while (1) { // Main loop.
        printf("Enter 3D vector operation (ADD/SUB/DOT/CROSS/NORM/MAG/QUIT): ");
        fgets(cmd, INPUT_BUFFER, stdin);
        
        if (toupper(*cmd) == *"ADD" || toupper(*cmd) == *"SUB" || toupper(*cmd) == *"DOT" || toupper(*cmd) == *"CROSS") {   
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

            if (toupper(*input) == *"ADD") {
                return_value.vec = add_vec(v1, v2);
                return_value.current_type = 'F';
            } 
            
            else if (toupper(*input) == *"SUB") {
                return_value.vec = sub_vec(v1, v2);
                return_value.current_type = 'V';
            }

            else if (toupper(*input) == *"DOT") {
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

        else if (toupper(*cmd) == *"NORM" || toupper(*cmd) == *"MAG") {
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
            if (toupper(*cmd) == *"NORM") {
                printf("RESULT: ");
                print_vec(normalize(v1));    
            }

            else {
                printf("RESULT: ");
                printf("%f\n", magnitude(v1)); 
            }
        }

        else if (toupper(*cmd) == *"QUIT") {
            exit(EXIT_SUCCESS);
        }

        else {
            printf("Unrecognized command: %s\n", input);
        }
    }  

    return 0;
}