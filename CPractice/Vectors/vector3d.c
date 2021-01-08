#include <math.h>
#include <stdio.h>
#include "vector3d.h"


float magnitude(Vector3D v) {
    return sqrt(v.x * v.x + v.y * v.y + v.z * v.z);
}

Vector3D add_vec(Vector3D v1, Vector3D v2) {
    Vector3D sum = {
        v1.x + v2.x,
        v1.y + v2.y,
        v1.z + v2.z
    };
    return sum;
}

Vector3D sub_vec(Vector3D v1, Vector3D v2) {
    Vector3D sum = {
        v1.x - v2.x,
        v1.y - v2.y,
        v1.z - v2.z
    };
    return sum;
}


float dot(Vector3D v1, Vector3D v2) {
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z;
}

Vector3D cross(Vector3D v1, Vector3D v2) {
    Vector3D prod = {
        v1.y * v2.z - v1.z * v2.y,
        v1.z * v2.x - v1.x * v2.z,
        v1.x * v2.y - v1.y * v2.x 
    };
    return prod;
}


Vector3D normalize(Vector3D v) {
    Vector3D unit = {
        v.x / magnitude(v),
        v.y / magnitude(v),
        v.z / magnitude(v)
    };
    return unit;
}

void print_vec(Vector3D v) {
    printf("{%f, %f, %f}\n", v.x, v.y, v.z);
}