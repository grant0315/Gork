// Gork main.cpp
// Author: Grant Hopkins

#include <iostream>
#include <chrono>
#include <thread>

// Constants for frame rate control
const int FRAME_RATE = 60;
const int FRAME_TIME = 1000 / FRAME_RATE;

bool isRunning = true;

char getPlayerInput(const std::string& message) {
    std::cout << message;
    char userInput;
    std::cin >> userInput;  
    return userInput; 
}

void processInput(const char& input) {
    if (input == 'q' || input == 'Q') {
        isRunning = false;
    }
}

void updateGame() {
    // Update game state here
    std::cout << "Updating game state..." << std::endl;
}

void renderGame() {
    // Render game objects here
    std::cout << "Rendering game..." << std::endl;
}

void licenseNotice() {
    std::cout << "<program>  Copyright (C) <year>  <name of author>" << std::endl;
    std::cout << "This program comes with ABSOLUTELY NO WARRANTY;" << std::endl;
    std::cout << "This is free software, and you are welcome to redistribute it" << std::endl;
    std::cout << "under certain conditions;" << std::endl;
}

int main() {
    while (isRunning) {
        auto frameStart = std::chrono::high_resolution_clock::now();

        // Test example of getPlayerInput()
        char userInput = getPlayerInput("Please enter any char: [Q]uit [q]uit");

        // Process input
        processInput(userInput);

        // Update game state
        updateGame();

        // Render the game
        renderGame();

        // Frame rate control
        auto frameEnd = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::milli> elapsed = frameEnd - frameStart;

        if (elapsed.count() < FRAME_TIME) {
            std::this_thread::sleep_for(std::chrono::milliseconds(FRAME_TIME) - elapsed);
        }
    }

    std::cout << "Game over!" << std::endl;
    return 0;
}
