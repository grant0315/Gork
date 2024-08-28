#include <iostream>
#include <vector>

class gork {
    public:
        void update();
        void render();
        std::string& processInput(const std::string& message);
        void gameLoop();

    private:
        bool isRunning = true;
};

void gork::update() {
    std::cout << "Updating game state..." << std::endl;
}

void gork::render() {
    std::cout << "Rendering..." << std::endl;
}

std::string& gork::processInput(const std::string& message) {
    std::string input;
    std::cout << "Processing user input..." << std::endl;
    std::cin >> input;
    return input.value;
}

void gork::gameLoop() {
    while (isRunning) {
        processInput();
        update();
        render();
    }

    // Figure out if quit was given (or save)
}
