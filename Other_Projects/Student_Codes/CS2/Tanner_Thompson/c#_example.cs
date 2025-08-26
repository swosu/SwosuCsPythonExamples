using System;
using System.Collections.Generic;

namespace WompusGame
{
    class Program
    {
        static void Main(string[] args)
        {
            // Define the maze size
            const int mazeSize = 20;

            // Create the maze
            char[,] maze = new char[mazeSize, mazeSize];

            // Initialize the maze with blocked cells
            for (int i = 0; i < mazeSize; i++)
            {
                for (int j = 0; j < mazeSize; j++)
                {
                    maze[i, j] = '#';
                }
            }

            // Set the start and finish positions
            int startX = 0;
            int startY = 0;
            int finishX = mazeSize - 1;
            int finishY = mazeSize - 1;

            // Set the player's initial position
            int playerX = startX;
            int playerY = startY;

            // Game loop
            while (true)
            {
                // Print the maze
                PrintMaze(maze, playerX, playerY);

                // Prompt the user for input
                Console.WriteLine("Enter a direction (4, 8, 6, 2), 'l' to look, or 'm' to move:");

                // Read the user's input
                string input = Console.ReadLine();

                // Process the user's input
                if (input == "l")
                {
                    // TODO: Implement the logic for looking in a direction
                }
                else if (input == "m")
                {
                    // TODO: Implement the logic for moving in a direction
                }
                else if (input == "4" || input == "8" || input == "6" || input == "2")
                {
                    // TODO: Implement the logic for navigating in a direction
                }
                else
                {
                    Console.WriteLine("Invalid input. Please try again.");
                }
            }
        }

        static void PrintMaze(char[,] maze, int playerX, int playerY)
        {
            int mazeSize = maze.GetLength(0);

            for (int i = 0; i < mazeSize; i++)
            {
                for (int j = 0; j < mazeSize; j++)
                {
                    if (i == playerY && j == playerX)
                    {
                        Console.Write('P'); // Player's position
                    }
                    else
                    {
                        Console.Write(maze[i, j]);
                    }
                }
                Console.WriteLine();
            }
        }
    }
}
