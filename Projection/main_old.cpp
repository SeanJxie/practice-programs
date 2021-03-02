#include <SDL.h>
#include <iostream>

#include "matrix.h"
#include "projection.h"
#include "obj_loader.h"


const int inputWinWt = 3840, inputWinHt = 2160;
const char* WINTT = "Perspective Projection in C++";


int main(int argc, char* argv[])
{
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window* hWin = SDL_CreateWindow(WINTT, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, inputWinWt / 2, inputWinHt / 2, SDL_WINDOW_SHOWN);
    SDL_Renderer* hRend = SDL_CreateRenderer(hWin, -1, SDL_RENDERER_ACCELERATED);

    vector<float> camPos = { -2.05, -1.18, -3.24 };
    vector<float> camRot = { 0.0, 0.0, 0.0 };
    vector<float> imgPlane = { 0.0, 0.0, 1500.0 };
    
    vector<float> point2d1;
    vector<float> point2d2;

    vector<vector<vector<float>>> axis = {
        {{-1.0, 0.0, 0.0},
        {1.0, 0.0, 0.0}},
        {{0.0, -1.0, 0.0},
        {0.0, 1.0, 0.0}},
        {{0.0, 0.0, -1.0},
        {0.0, 0.0, 1.0}},
    };

    vector<vector<float>> object = load_obj_from_fname("Handgun_obj.obj");
    std::cout << object.size() << std::endl;

    bool run = true;

    bool up = false;
    bool down = false;
    bool left = false;
    bool right = false;
    bool in = false;
    bool out = false;

    bool yaw = false;
    bool pitch = false;
    bool roll = false;
 
    float speed = 0.01;
    float rspeed = 0.01;

    MxN proj1(3, 3);
    MxN proj2(3, 3);

    SDL_Rect point;

    SDL_Event event;


    while (run)
    {
        while (SDL_PollEvent(&event))
        {
            switch (event.type)
            {
            case SDL_QUIT:
                run = false;
                break;
            case SDL_KEYDOWN:
                switch (event.key.keysym.sym)
                {
                case SDLK_RIGHT: right = true; break;
                case SDLK_LEFT: left = true; break; 
                case SDLK_UP: up = true; break;  
                case SDLK_DOWN: down = true; break;  
                case SDLK_w: in = true; break;
                case SDLK_s: out = true; break;
                case SDLK_z: yaw = true; break;  
                case SDLK_x: pitch = true;  break; 
                case SDLK_c: roll = true; break;
                }
                break;
            case SDL_KEYUP:
                switch (event.key.keysym.sym)
                {
                case SDLK_RIGHT: right = false; break;
                case SDLK_LEFT: left = false; break;
                case SDLK_UP: up = false; break;
                case SDLK_DOWN: down = false; break;
                case SDLK_w: in = false; break;
                case SDLK_s: out = false; break;
                case SDLK_z: yaw = false; break;
                case SDLK_x: pitch = false;  break;
                case SDLK_c: roll = false; break;
                }
                break;
            }
        }

        if (right) camPos[0] += speed;
        if (left)  camPos[0] -= speed;
        if (up)    camPos[1] -= speed;
        if (down)  camPos[1] += speed;
        if (in)    camPos[2] += speed;
        if (out)   camPos[2] -= speed;
        if (yaw)   camRot[0] += speed;
        if (pitch) camRot[1] += speed;
        if (roll)  camRot[2] += speed;

        SDL_SetRenderDrawColor(hRend, 0, 0, 0, 255); // Clear black
        SDL_RenderClear(hRend);

        SDL_SetRenderDrawColor(hRend, 255, 255, 255, 255);
        for (auto v : object)
        {
            //proj1 = camera_transform(v, camPos, camRot);
            point2d1 = project_point_ortho(v);
            
            SDL_RenderDrawPointF(hRend, point2d1[0] * 500 + 500, point2d1[1] * 500 + 500);
        }
        
        SDL_RenderPresent(hRend);

        //std::cout << camPos[0] << ' ' << camPos[1] << ' ' << camPos[2] << std::endl;
    }


    SDL_DestroyRenderer(hRend);
    SDL_DestroyWindow(hWin);
    SDL_Quit();
    return 0;
}