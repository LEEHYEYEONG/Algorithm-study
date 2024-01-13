#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<int> v;
int n, l, d, cnt;

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> n >> l;
  int tmp;
  for (int i = 0; i < n; i++) {
    cin >> tmp;
    v.push_back(tmp);
  }

  sort(v.begin(), v.end());

  for (int i = 0; i < n; i++) {
    d = v[i] + l - 1;
    int j = i;
    for (; j < n; j++) {
      if (v[j] > d)
        break;
    }
    i = j - 1;
    cnt++;
  }

  cout << cnt << "\n";
  return 0;
}