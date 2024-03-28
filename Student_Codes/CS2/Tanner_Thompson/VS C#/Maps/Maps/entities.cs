using System;

class MazeGame
{
    private const int Width = 10;
    private const int Height = 10;

    private static readonly char[,] Maze = new char[Width, Height];
    private static int playerX = 1;
    private static int playerY = 1;

    static void Maion(string[] args)
    {
        GenerateMaze();
        PrintMaze();

        while (true)
        {
            ConsoleKeyInfo keyInfo = Console.ReadKey();
            Console.Clear();

            switch (keyInfo.Key)
            {
                case ConsoleKey.UpArrow:
                    if (playerY - 1 >= 0 && Maze[playerX, playerY - 1] != '#')
                    {
                        playerY--;
                    }
                    break;
                case ConsoleKey.DownArrow:
                    if (playerY + 1 < Height && Maze[playerX, playerY + 1] != '#')
                    {
                        playerY++;
                    }
                    break;
                case ConsoleKey.LeftArrow:
                    if (playerX - 1 >= 0 && Maze[playerX - 1, playerY] != '#')
                    {
                        playerX--;
                    }
                    break;
                case ConsoleKey.RightArrow:
                    if (playerX + 1 < Width && Maze[playerX + 1, playerY] != '#')
                    {
                        playerX++;
                    }
                    break;
            }

            PrintMaze();
            if (playerX == Width - 2 && playerY == Height - 1)
            {
                Console.WriteLine("Congratulations! You've reached the exit!");
                break;
            }
        }
    }

    private static void GenerateMaze()
    {
        // Generating the maze (you can replace this with your maze generation logic)
        for (int i = 0; i < Width; i++)
        {
            for (int j = 0; j < Height; j++)
            {
                Maze[i, j] = (i == 0 || j == 0 || i == Width - 1 || j == Height - 1) ? '#' : ' ';
            }
        }

        // Set start and end points
        Maze[1, 0] = 'S'; // Start point
        Maze[Width - 2, Height - 1] = 'E'; // End point
    }

    private static void PrintMaze()
    {
        // Printing the maze with the player's position
        for (int j = 0; j < Height; j++)
        {
            for (int i = 0; i < Width; i++)
            {
                if (i == playerX && j == playerY)
                {
                    Console.Write('P'); // Player
                }
                else
                {
                    Console.Write(Maze[i, j]);
                }
            }
            Console.WriteLine();
        }
    }
}
