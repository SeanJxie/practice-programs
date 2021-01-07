#include <stdio.h>
#include "vector3d.h"

int main() {
    Vector3D vec1 = {2, 1, 5}, vec2 = {5, 1, 5};
    print_vec(cross(vec1, vec2));
    printf("%f\n", dot(vec1, vec2));
    print_vec(normalize(vec1));
    printf("%f\n", magnitude(vec1));

    return 0;
}