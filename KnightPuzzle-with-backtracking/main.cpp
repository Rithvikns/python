#include <iostream>
#include <vector>

using namespace std;

#define N 8


int moveX[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int moveY[8] = {1, 2, 2, 1, -1, -2, -2, -1};

bool isSafe(int x, int y, vector<vector<int>>& board) {
    return (x >= 0 && x < N && y >= 0 && y < N && board[x][y] == -1);
}

void printSolution(vector<vector<int>>& board) {
    for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++)
            cout << board[x][y] << " ";
        cout << endl;
    }
}

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

int main() {
    solveKT();
    return 0;
}
