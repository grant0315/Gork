#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <bits/stdc++.h>

class Player {
public:
    // Status effect enum class definition
    enum class StatusEffect {
        Poison,
        Starving,
        Bleeding,
        Stunned
    };

    Player(const std::string& name, const std::string& race, const std::string& gameClass)
        : name(name), gameClass(gameClass) {}
    
    // Class Methods (Player Utility)
    void displayInfo() const {
        std::cout << "Player name: " << name << std::endl;
        std::cout << "Player race: " << race << std::endl;
        std::cout << "Player class: " << gameClass << std::endl;
    }

    void displayStatus() const {
        std::cout  << "Current Status: " << std::endl;
        std::cout << "Health: " << health << std::endl;
        std::cout << "Hunger: " << hunger << std::endl;

        // Loop through applied status effects and print
        if (appliedStatusEffects.size() > 0) {
            std::cout << "Current Status Effects: ";
            for (std::size_t i = 0; i < appliedStatusEffects.size(); ++i) {
                if (appliedStatusEffects[i] == StatusEffect::Poison) {
                    std::cout << "poision" << std::endl;
                } else if (appliedStatusEffects[i] == StatusEffect::Starving) {
                    std::cout << "starving" << std::endl;
                } else if (appliedStatusEffects[i] == StatusEffect::Bleeding) {
                    std::cout << "bleeding" << std::endl;
                } else if (appliedStatusEffects[i] == StatusEffect::Stunned) {
                    std::cout << "stunned" << std::endl;
                }
            }
        } else {
            std::cout << "Currently not afflicted with status effects!" << std::endl;
        }
    }

    void addStatusEffect(StatusEffect statusEffect) {
        appliedStatusEffects.push_back(statusEffect);
    }

    void removeStatusEffect(StatusEffect statusEffect) {
        auto it = std::find(appliedStatusEffects.begin(), appliedStatusEffects.end(), statusEffect);
        if (it != appliedStatusEffects.end()) {
            appliedStatusEffects.erase(it);
        }
    }

    // Getters
    std::string getName() const {
        return name;
    }

    std::string getRace() const {
        return race;
    }

    std::string getGameClass() const {
        return gameClass;
    }

    int getHealth() const {
        return health;
    }

    int getHunger() const {
        return hunger;
    }

    std::pair<int, int> getPosition() const {
        return position;
    }

    std::vector<StatusEffect> getStatusEffects() const {
        return appliedStatusEffects;
    }

    // Setters
    void setHealth(int newHealth) {
        health = newHealth;
    }

    void setHunger(int newHunger) {
        hunger = newHunger;
    }

    void setPosition(std::pair<int, int> newPosition) {
        position = newPosition;
    }

    void setAppliedStatusEffects(std::vector<StatusEffect> newAppliedStatusEffects) {
        appliedStatusEffects = newAppliedStatusEffects;
    }
private:
    std::string name;
    std::string race;
    std::string gameClass;
    int health;
    int hunger;
    std::vector<StatusEffect> appliedStatusEffects; 
    std::pair<int, int> position = {0, 0};
};
