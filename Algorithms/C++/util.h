
// util.h

#include <iostream>
#include <string>
#include <vector>

// Display a 1D vector
template <class T>
void print(const std::vector<T> &arr, const std::string &endline = "\n", const bool &quote = false) {
    std::cout << "{";
    for (unsigned i = 0; i < arr.size(); i++) {
        quote ? std::cout << "\"" << arr[i] << "\"" : std::cout << arr[i];
        i < arr.size() - 1 ? std::cout << ", " : std::cout << "";
    }
    std::cout << "}" << endline;
}

// Display a 2D vector
template <class T>
void print(const std::vector<std::vector<T>> &matrix, const std::string &endline = "\n", const bool &quote = false) {
    std::cout << "{";
    for (unsigned i = 0; i < matrix.size(); i++) {
        print<T>(matrix[i], "", quote);
        i < matrix.size() - 1 ? std::cout << ", " : std::cout << "";
    }
    std::cout << "}" << endline;
}
