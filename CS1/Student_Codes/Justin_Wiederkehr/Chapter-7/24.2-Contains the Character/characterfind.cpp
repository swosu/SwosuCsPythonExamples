#include <iostream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

vector<string> split(const string &s, char delimiter) {
    vector<string> tokens;
    string token;
    istringstream tokenStream(s);
    while (getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

bool contains(const string &word, const string &chars) {
    return word.find(chars) != string::npos;
}

int main() {
    string input;
    string searchChars;
FirstInput:
    cout << "Enter a sentence or a comma separated list of words: ";
    getline(cin, input);
    if (cin.fail()) {
        cin.clear();
        cin.ignore(32767, '\n');
        cout << "Invalid input. Please try again." << endl;
        goto FirstInput;
    }
SecondInput:
    cout << "Enter the character(s) to search for: ";
    getline(cin, searchChars);
    if (cin.fail()) {
        cin.clear();
        cin.ignore(32767, '\n');
        cout << "Invalid input. Please try again." << endl;
        goto FirstInput;
    }

    vector<string> words = split(input, ' ');

    cout << "Words containing \"" << searchChars << "\":" << endl;
    for (const auto &word : words) {
        if (contains(word, searchChars)) {
            cout << word << ", " << endl;
        }
    }

    return 0;
}