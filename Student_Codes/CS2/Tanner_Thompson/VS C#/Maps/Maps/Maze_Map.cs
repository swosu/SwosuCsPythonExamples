using System;
using System.Collections.Generic;
using System.Threading;

class MazeGenerator
{
    private const int Width = 64;
    private const int Height = 32;

    private static readonly char[,] Maze = new char[Width, Height];
    private static int playerX = 1;
    private static int playerY = 1;
    private static Random random = new Random();
    private static int keysCollected = 0;
    private static List<(int, int)> keyPositions = new List<(int, int)>();

    static void Main(string[] args)
    {
        GenerateMaze();
        PrintMaze();

        while (true)
        {
            ConsoleKeyInfo keyInfo = Console.ReadKey(true); 
            Console.SetCursorPosition(playerX, playerY); 

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

    
            if (Maze[playerX, playerY] == 'K')
            {
                Maze[playerX, playerY] = ' '; 
                keysCollected++;
                Console.WriteLine($"You collected a key! Keys collected: {keysCollected}/4");
            }

            PrintMaze();

            
            if (playerX == Width - 2 && playerY == Height - 1 && keysCollected == 4)
            {
                Console.WriteLine("Congratulations! You've collected all keys and reached the exit!");
                break;
            }
        }
    }

    private static void GenerateMaze()
    {
        
        for (int i = 0; i < Width; i++)
        {
            for (int j = 0; j < Height; j++)
            {
                Maze[i, j] = '#';
            }
        }

        
        Maze[1, 0] = 'S';
        DepthFirstSearch(1, 1);

        
        Maze[Width - 2, Height - 1] = 'E';

        
        PlaceKeys();
    }

    private static void DepthFirstSearch(int x, int y)
    {
        
        Maze[x, y] = ' ';

        
        List<int[]> directions = new List<int[]>
        {
            new int[] { 0, -2 }, 
            new int[] { 0, 2 },  
            new int[] { -2, 0 }, 
            new int[] { 2, 0 }   
        };


        
        for (int i = 0; i < directions.Count; i++)
        {
            int[] temp = directions[i];
            int randomIndex = random.Next(i, directions.Count);
            directions[i] = directions[randomIndex];
            directions[randomIndex] = temp;
        }

        
        foreach (int[] dir in directions)
        {
            int nx = x + dir[0];
            int ny = y + dir[1];

            
            if (nx > 0 && ny > 0 && nx < Width && ny < Height && Maze[nx, ny] == '#')
            {
                
                Maze[nx, ny] = ' ';
                Maze[x + dir[0] / 2, y + dir[1] / 2] = ' ';

                
                DepthFirstSearch(nx, ny);
            }

            
        }
    }

    private static void PlaceKeys()
    {
        
        for (int i = 0; i < 4; i++) 
        {
            int x, y;
            do
            {
                x = random.Next(1, Width - 2);
                y = random.Next(1, Height - 2);
            } while (Maze[x, y] != ' '); 

            Maze[x, y] = 'K';
            keyPositions.Add((x, y));
        }
    }

    private static void PrintMaze()
    {
        
        Console.SetCursorPosition(0, 0);
        for (int j = 0; j < Height; j++)
        {
            for (int i = 0; i < Width; i++)
            {
                if (i == playerX && j == playerY)
                {
                    Console.Write('P');
                }
                else
                {
                    if (Maze[i, j] == 'K')
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.Write('K'); 
                        Console.ResetColor();
                    }
                    else if (Maze[i, j] == 'E')
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.Write('E'); 
                        Console.ResetColor(); 
                    }
                    else
                    {
                        Console.Write(Maze[i, j]);
                    }
                }
            }
            Console.WriteLine();
        }
        
        Console.WriteLine($"Keys collected: {keysCollected}/4");
    }
}
