#include <iostream>
#include <vector>

using namespace std;

vector<int> v;
int h, w;
int ret;
int max_begin, max_end;
int max_h;

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> h >> w;

  int tmp;
  for (int i = 0; i < w; i++) {
    cin >> tmp;
    v.push_back(tmp);
  }

  for (int i = 0; i < w; i++) {
    for (int j = i; j >= 0; j--) {
      if (v[j] > max_begin)
        max_begin = v[j];
    }
    for (int k = i; k < w; k++) {
      if (v[k] > max_end) {
        max_end = v[k];
      }
    }
    max_h = max_begin > max_end ? max_end : max_begin;
    ret += max_h - v[i];
    max_begin = max_end = 0;
  }
  cout << ret << "\n";
}
