// In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>
#include <complex>

using namespace std;

#define rep(i, a, b) for (int i = (a), i##_end_ = (b); i < i##_end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
template<typename T> inline bool smin(T &a, const T &b)   { return a > b ? a = b : a;    }
template<typename T> inline bool smax(T &a, const T &b)   { return a < b ? a = b : a;    }

typedef long long LL;

const int N = (int) 0, mod = (int) 0;
int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
map<pair<int, int>, pair<int, int>> go[4];
map<pair<int, int>, int> mark;
pair<int, int> find(int x, int y, int d) {
	if (mark.find(mp(x, y)) == mark.end()) return mp(x, y);
	if (go[d].find(mp(x, y)) == go[d].end()) {
		go[d][mp(x, y)] = mp(x + dx[d], y + dy[d]);
	}
	auto &nxt = go[d][mp(x, y)];
	nxt = find(nxt.first, nxt.second, d);
	return nxt;
}
int main() {
	srand(time(0));
	int tc = 100;
	cin >> tc;
	for (int tt = 1; tt <= tc; ++tt) {
		cout << "Case #" << tt << ": ";
		mark.clear();
		for (int j = 0; j < 4; ++j) go[j].clear();
		int k = 400000, n = 400000, m = 400000, sr = n / 2, sc = m / 2;
		cin >> k >> n >> m >> sr >> sc;
		--sr;
		--sc;
		mark[mp(sr, sc)] = 1;
		string s;
		cin >> s;
		for (auto c : s) {
			int dir = 0;
			if (c == 'N') {
				dir = 3;
			} else if (c == 'W') {
				dir = 2;
			} else if (c == 'S') {
				dir = 1;
			}
			auto res = find(sr, sc, dir);
			sr = res.first;
			sc = res.second;
			mark[mp(sr, sc)] = 1;
		}
		cout << sr + 1 << ' ' << sc + 1 << '\n';

	}
}

















