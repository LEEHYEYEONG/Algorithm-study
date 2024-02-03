#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, SUM, result;
vector<int> v;

void binarySearch(int start, int end) {
  // 중앙값 찾기
  int mid = (start + end) / 2;
  // 중앙인덱스 찾기
  int idx = lower_bound(v.begin(), v.end(), mid) - v.begin();
  int sum = 0;

  if (start > end) return ;
  
  for (int i = 0; i < idx; i++)
    sum += v[i];
  sum += (mid * (N - idx));
  
  if (sum > M)
    binarySearch(start, mid - 1);
  else {
    result = mid;
    binarySearch(mid + 1, end);
  }
}

int main(void)
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N;
  int tmp;
  for(int i = 0; i < N; i++){
    cin >> tmp;
    v.push_back(tmp);
    SUM += tmp;
  }
  cin >> M;
  sort(v.begin(), v.end());

  if (SUM < M)
    cout << v[N - 1] << "\n";
  else {
    binarySearch(0, v[N-1]);
    cout << result << "\n";
  }
}