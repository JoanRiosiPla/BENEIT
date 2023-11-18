#include <iostream>
#include <fstream>
#include "nlohmann/json.hpp"

using json = nlohmann::json;

std::string lower(std::string string) {
    std::transform(string.begin(), string.end(), string.begin(),
        [](unsigned char c) { return std::tolower(c); });
    return string;
}

int main(void) {
    // Open the file stream
    std::string filePath;
    std::cout << "Introdueix el camí complet al fitxer: ";
    std::cin >> filePath;
    std::ifstream inputFile(filePath);

    // Add this before attempting to open the file
    std::cout << "Current working directory: " << std::filesystem::current_path() << std::endl;

    // Check if the file is opened successfully
    if (!inputFile.is_open()) {
        std::cerr << "Failed to open the JSON file." << std::endl;
        return 1;
    }

    // Parse the JSON from the file stream
    json jsonData;
    inputFile >> jsonData;
    inputFile.close();

    // Access the data in the JSON object
    json insults = jsonData["insults"];
    while (true)
    {
        /*
        {
        "insults": [
            {
                "paraula": "Aixafaguitarres",
                "definicio": "Persona que fa anar malament un pla precist",
                "tags": [
                    "despectiu"
                ],
                "font": {
                    "nom": "Viccionari",
                    "url": "https://ca.m.wiktionary.org/wiki/aixafaguitarres"
                }
            },
            ...
        }
        */
        std::string paraula;
        std::string definicio;
        std::string tags;
        std::string nom;
        std::string url;
        std::cout << "Introdueix la paraula: ";
        std::cin >> paraula;
        if (paraula == "STOP" || paraula == "FI") break;
        for (auto& insult : insults) {
            if (lower(insult["paraula"]) == lower(paraula)) {
                std::cout << "La paraula ja existeix" << std::endl;
                continue;
            }
        }
        std::cout << "Introdueix la definicio: ";
        std::getline(std::cin, definicio);
        std::cout << "Introdueix els tags separats per comes: ";
        std::cin >> tags;
        std::cout << "Introdueix el nom de la font: ";
        std::cin >> nom;
        std::cout << "Introdueix la url de la font: ";
        std::cin >> url;
        json insult;
        insult["paraula"] = paraula;
        insult["definicio"] = definicio;
        // Split tags by comma
        std::vector<std::string> tagsVector;
        std::string delimiter = ",";
        size_t pos = 0;
        std::string token;
        while ((pos = tags.find(delimiter)) != std::string::npos) {
            token = tags.substr(0, pos);
            tagsVector.push_back(token);
            tags.erase(0, pos + delimiter.length());
        }
        tagsVector.push_back(tags);
        insult["tags"] = tagsVector;
        json font;
        font["nom"] = nom;
        font["url"] = url;
        insult["font"] = font;
        insults.push_back(insult);
    }

    // Save changes to the JSON file
    jsonData["insults"] = insults;

    // Open the file stream in write mode
    std::ofstream outputFile(filePath);

    // Check if the file is opened successfully
    if (!outputFile.is_open()) {
        std::cerr << "Failed to open the JSON file for writing." << std::endl;
        return 1;
    }

    // Write the modified JSON data back to the file
    outputFile << jsonData.dump(4);

    // Close the output file stream
    outputFile.close();

    std::cout << "Afegit insults a insults.json, Fes un commit per a realitzar els canvis" << std::endl;

    return 0;
}