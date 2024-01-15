#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
int n;
vector<pair<int, int> > v;
priority_queue<int, vector<int>, greater<int> > pq;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> n;
  for (int i = 0, s, t; i < n; i++) {
    cin >> s >> t;
    v.push_back({s, t});
  }
  sort(v.begin(), v.end());

  for(int i = 0; i < n; i++) {
    pq.push(v[i].second);
    if (pq.top() <= v[i].first) 
      pq.pop();
  }
  cout << pq.size() << "\n";
}
