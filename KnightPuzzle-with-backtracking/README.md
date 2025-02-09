# Knight's Puzzle in Chess

Let's try to understand the knight's puzzle in chess.

The diagram below represents the knight puzzle model. The knight has to travel to each and every square on the chessboard only once. It is difficult to complete this puzzle.

![Knight Puzzle](https://github.com/user-attachments/assets/77a4d7b0-f939-4f50-be3c-2faeeb8d9e5c)

Today, let's build a code to complete this puzzle.
```console
#include <iostream>
#include <vector>
using namespace std;`
```
Let's include the libraries and the namespace .


# Task1 : List out the possible squares for the Knight next move

```console
int moveX[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int moveY[8] = {1, 2, 2, 1, -1, -2, -2, -1};`
```

This lines are used to represent the next move of the knight using x axis and y axis , there are only 8 moves possible for the knight to move . In the code you can see for movex[0] = 2 and movey[0] = 1 . Thee position of the next knight move is two steps in x axis and 1 step in y axis compared to the current position .


![image](https://github.com/user-attachments/assets/c27c4d09-0ec6-4e24-a0fa-7e2eb6072085)

# Task2 : Check if the next move is valid

```console
bool isSafe(int x, int y, vector<vector<int>>& board) {
    return (x >= 0 && x < N && y >= 0 && y < N && board[x][y] == -1);
}

```
This function checks if a given position (x, y) is within the bounds of the chessboard and has not been visited yet (indicated by -1). 
In the diagram below only 6 options are there for the knight , the other two squares are outside the board . Hence those two options are invalid .

![image](https://github.com/user-attachments/assets/7c07032c-4bda-4499-a7e2-3127f830226d)


# Task3 : A Recursive function that attempts to solve the Knight's Tour problem.

```console
bool solveKTUtil(int x, int y, int movei, vector<vector<int>>& board) {
    int next_x, next_y;
    if (movei == N * N) 
        return true;

    for (int k = 0; k < 8; k++) {
        next_x = x + moveX[k];
        next_y = y + moveY[k];
        if (isSafe(next_x, next_y, board)) {
            board[next_x][next_y] = movei;
            if (solveKTUtil(next_x, next_y, movei + 1, board))
                return true;
            else
                board[next_x][next_y] = -1; 
        }
    }
    return false;
}
```
Here a 2D vector is used to store the chess board data , and in the function argument we are referencing the chess board instead of duplicating since all the function should work on a single chess board .
movei is the current move number.
If movei equals N * N, all squares have been visited, and the function returns true.
The function tries all possible moves from the current position (x, y) using the moveX and moveY arrays.
For each valid move, it marks the next position with the current move number, calls itself recursively with the new position and incremented move number.
If a valid path is found, it returns true. Otherwise, it backtracks by resetting the current position to -1.

The recursive function calculates the result till the end meaning it does all possible recursive calls and if the result is true it updates the initial call and all the recursive call with the result else it sets as -1 to the initial number and moves on to the next possible option .
## Algorithm Overview

### Initial Call
Start from an initial position on the board.

### Recursive Calls
Try all possible knight moves from the current position.

### Base Case
If all squares on the board have been visited (i.e., `movei == N * N`), return `true`.

### Backtracking
If a move does not lead to a solution, backtrack by resetting the board position and try the next possible move.

###  when return true is executed in the base case or within the loop, it will not only exit the current recursive call but also immediately break out of the loop and propagate the true value up the call stack. This effectively stops all further processing and recursive calls.


# Task4 : Function to Initiate and Solve the Knight's Tour Problem
```console
bool solveKT() {
    
    vector<vector<int>> board(N, vector<int>(N, -1));


    int startX = 0;
    int startY = 0;

  
    board[startX][startY] = 0;


    if (!solveKTUtil(startX, startY, 1, board)) {
        cout << "Solution does not exist" << endl;
        return false;
    } else
        printSolution(board);

    return true;
}
```
This function initializes the chessboard and starts the Knight's Tour from the top-left corner (0, 0).
It calls solveKTUtil with the initial position and the first move number.
If a solution is found, it prints the board using printSolution. Otherwise, it indicates that no solution exists.


# Task5 : Print Solution function .
```console
void printSolution(vector<vector<int>>& board) {
    for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++)
            cout << board[x][y] << " ";
        cout << endl;
    }
}
```

This function is used to print the output if the solution exists .

# Task6 : main block .
```console
int main() {
    solveKT();
    return 0;
}
```

# Output :

Below is the result of the Knight's Tour:
```console
0 59 38 33 30 17 8 63
37 34 31 60 9 62 29 16
58 1 36 39 32 27 18 7
35 48 41 26 61 10 15 28
42 57 2 49 40 23 6 19
47 50 45 54 25 20 11 14
56 43 52 3 22 13 24 5
51 46 55 44 53 4 21 12
```

# More Information :
You can try and complete the knight's tour puzzle in this link , it also allows you to take more steps and complete the puzzle .
https://www.mathsisfun.com/games/knights-move-2.html .

