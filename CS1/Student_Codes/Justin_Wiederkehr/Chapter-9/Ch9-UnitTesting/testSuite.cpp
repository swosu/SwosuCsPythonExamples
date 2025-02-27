#include <gtest/gtest.h>
#include "functions.h"

TEST(functions, d2)
{
    randomNum dice;
    dice.chooseADice("d2");
    GTEST_ASSERT_EQ(dice.min, 1);
    GTEST_ASSERT_EQ(dice.max, 2);
    dice.rollDice();
    GTEST_ASSERT_LE(dice.x, 2);
    GTEST_ASSERT_GE(dice.x, 1);



}

TEST(functions, d2Fair)
{
    randomNum dice;
    int heads = 0;
    int tails = 0;
    dice.chooseADice("d2");

    for (int i = 0; i < 1000; i++) {
        dice.rollDice();
        if (dice.x == 1) {heads++; } 
        else if (dice.x == 2) {tails++; }
        else {GTEST_FAIL();}
    }
    GTEST_ASSERT_GE(heads, 450);
    GTEST_ASSERT_GE(tails, 450);
}

TEST(functions, d4)
{
    randomNum dice;
    dice.chooseADice("d4");
    GTEST_ASSERT_EQ(dice.min, 1);
    GTEST_ASSERT_EQ(dice.max, 4);
    dice.rollDice();
    GTEST_ASSERT_LE(dice.x, 4);
    GTEST_ASSERT_GE(dice.x, 1);
}

TEST(functions, d6)
{
    randomNum dice;
    dice.chooseADice("d6");
    GTEST_ASSERT_EQ(dice.min, 1);
    GTEST_ASSERT_EQ(dice.max, 6);
    dice.rollDice();
    GTEST_ASSERT_LE(dice.x, 6);
    GTEST_ASSERT_GE(dice.x, 1);
}

TEST(functions, d8)
{
    randomNum dice;
    dice.chooseADice("d8");
    GTEST_ASSERT_EQ(dice.min, 1);
    GTEST_ASSERT_EQ(dice.max, 8);
    dice.rollDice();
    GTEST_ASSERT_LE(dice.x, 8);
    GTEST_ASSERT_GE(dice.x, 1);
}

TEST(functions, d10)
{
    randomNum dice;
    dice.chooseADice("d10");
    GTEST_ASSERT_EQ(dice.min, 1);
    GTEST_ASSERT_EQ(dice.max, 10);
    dice.rollDice();
    GTEST_ASSERT_LE(dice.x, 10);
    GTEST_ASSERT_GE(dice.x, 1);
}

TEST(functions, d12)
{
    randomNum dice;
    dice.chooseADice("d12");
    GTEST_ASSERT_EQ(dice.min, 1);
    GTEST_ASSERT_EQ(dice.max, 12);
    dice.rollDice();
    GTEST_ASSERT_LE(dice.x, 12);
    GTEST_ASSERT_GE(dice.x, 1);
}

TEST(functions, d20)
{
    randomNum dice;
    dice.chooseADice("d20");
    GTEST_ASSERT_EQ(dice.min, 1);
    GTEST_ASSERT_EQ(dice.max, 20);
    dice.rollDice();
    GTEST_ASSERT_LE(dice.x, 20);
    GTEST_ASSERT_GE(dice.x, 1);
}

TEST(functions, d100)
{
    randomNum dice;
    dice.chooseADice("d100");
    GTEST_ASSERT_EQ(dice.min, 1);
    GTEST_ASSERT_EQ(dice.max, 100);
    dice.rollDice();
    GTEST_ASSERT_LE(dice.x, 100);
    GTEST_ASSERT_GE(dice.x, 1);
}



int main(int argc, char* argv[])
{
    srand(time(NULL));
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}