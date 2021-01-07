#ifndef VECTOR3D_H
#define VECTOR3D_H

typedef struct {
    float x, y, z;
} Vector3D;


float magnitude(Vector3D);

Vector3D add_vec(Vector3D, Vector3D);

Vector3D sub_vec(Vector3D, Vector3D);

float dot(Vector3D, Vector3D);

Vector3D cross(Vector3D, Vector3D);

Vector3D normalize(Vector3D);

void print_vec(Vector3D);

#endif