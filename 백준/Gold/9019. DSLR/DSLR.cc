#include <iostream>
#include <vector>
#include <string>
using namespace std;

class intString {
public:
	int num;
	string query;
};

int v[10000] = { 0, };

int main() {
	int loop;
	cin >> loop;
	for (int i = 0; i < loop; i++) {
		for (int j = 0; j < 10000; j++)v[j] = 0;
		int A, B;
		cin >> A >> B;
		vector<intString> s;
		s.push_back({ A,"" });
		v[A] = 1;

		int finish = 0;
		while (!finish) {
			vector<intString> t;
			for (int i = 0; i < s.size(); i++) {
				int n = s[i].num;
				string q = s[i].query;

				int D = (2 * n) % 10000;
				if (D == B) {
					cout << q + "D" << '\n';
					finish = 1;
					break;
				}
				if (!v[D]) {
					v[D] = 1;
					t.push_back({ D,q + "D" });
				}

				int S = (n + 9999) % 10000;
				if (S == B) {
					cout << q + "S" << '\n';
					finish = 1;
					break;
				}
				if (!v[S]) {
					v[S] = 1;
					t.push_back({ S,q + "S" });
				}

				int L = n / 1000 + (n % 1000) * 10;
				if (L == B) {
					cout << q + "L" << '\n';
					finish = 1;
					break;
				}
				if (!v[L]) {
					v[L] = 1;
					t.push_back({ L,q + "L" });
				}

				int R = (n % 10) * 1000 + n / 10;
				if (R == B) {
					cout << q + "R" << '\n';
					finish = 1;
					break;
				}
				if (!v[R]) {
					v[R] = 1;
					t.push_back({ R,q + "R" });
				}
			}
			s = t;
		}
	}
}