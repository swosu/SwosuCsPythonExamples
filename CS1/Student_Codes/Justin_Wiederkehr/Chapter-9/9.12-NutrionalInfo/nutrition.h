#include <iostream>
#include <string>
using namespace std;

class Nutrition {
    public:
        double fat;
        double carbs;
        double protien;

        Nutrition(){};

        double getCalories(double numServings) {
            return (this->fat * 9 + this->carbs * 4 + this->protien * 4) * numServings;
        }

        void printNutritionInfo(string foodName) {
            cout << "Nutrition Information per serving of " << foodName << endl;
            cout << "     " << "Fat: " << this->fat << "g" << endl;
            cout << "     " << "Carbs: " << this->carbs << "g" << endl;
            cout << "     " << "Protien: " << this->protien << "g" << endl;
            cout << "Number of Calories for 1 serving(s): " << this->getCalories(1) << endl;
            cout << "Number of Calories for 3 serving(s): " << this->getCalories(3) << endl;
        }
};