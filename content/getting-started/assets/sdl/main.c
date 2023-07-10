#include <SDL2/SDL.h>
#include <stdbool.h>
#include <stdio.h>

static void err(const char *format, ...)
{
    fprintf(stderr, "(error) ");
    va_list args;
    va_start(args, format);
    vfprintf(stderr, format, args);
    va_end(args);
    fprintf(stderr, "\n");
    fflush(stderr);
}

int main(void)
{
    SDL_Renderer* renderer;
    SDL_Surface* imgSurface;
    SDL_Texture* imgTexture;
    SDL_Window* window;

    if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_EVENTS) < 0) {
        err("sdl2 init: %s", SDL_GetError());
        return 1;
    }

    window = SDL_CreateWindow("releng-tool",
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        1280, 640, SDL_WINDOW_OPENGL);
    if (window == NULL) {
        err("failed to create window");
        return 1;
    }

    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (renderer == NULL) {
        err("failed to create renderer");
        return 1;
    }

    // read the image into a texture
    imgSurface = SDL_LoadBMP("releng-tool.bmp");
    if (imgSurface == NULL) {
        err("failed to load image: %s", SDL_GetError());
        return 1;
    }

    imgTexture = SDL_CreateTextureFromSurface(renderer, imgSurface);
    if (imgTexture == NULL) {
        err("failed to create texture");
        return 1;
    }

    SDL_FreeSurface(imgSurface);

    while (true) {
        // wait until a quit is issued
        SDL_Event e;
        if (SDL_PollEvent(&e)) {
            if (e.type == SDL_QUIT) break;
        }

        // render the image
        SDL_RenderClear(renderer);
        SDL_RenderCopy(renderer, imgTexture, NULL, NULL);
        SDL_RenderPresent(renderer);
    }

    // cleanup
    SDL_DestroyTexture(imgTexture);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
