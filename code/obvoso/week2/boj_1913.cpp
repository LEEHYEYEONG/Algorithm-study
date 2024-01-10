#include <iostream>
#include <vector>

using namespace std;

int n, findN;
enum {
  DOWN,
  RIGHT,
  UP,
  LEFT,
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> n >> findN;

  int arr[n][n];
  int grid = n - 1;
  int curN = n * n;
  int i = 0, j = 0;
  int direction = DOWN;
  int findX, findY;

  while (curN > 0) {

    if (curN == findN) {
      findX = i + 1;
      findY = j + 1;
    }
    arr[i][j] = curN--;

    if (i == grid && direction == DOWN) {
      direction = RIGHT;
    } else if (j == grid && direction == RIGHT) {
      direction = UP;
    } else if (i + j == n - 1 && direction == UP) {
      grid--;
      direction = LEFT;
    } else if (i - j == -1 && direction == LEFT) {
      direction = DOWN;
    }

    switch (direction) {
    case DOWN:
      i++;
      break;
    case RIGHT:
      j++;
      break;
    case UP:
      i--;
      break;
    case LEFT:
      j--;
      break;
    }
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cout << arr[i][j] << " ";
    }
    cout << "\n";
  }
  cout << findX << " " << findY << "\n";
}