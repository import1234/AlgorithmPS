#include <iostream>
#include <unordered_set>
#include <string>

using namespace std;

int gcd(int a, int b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}

int main(void) {

	unordered_set<string> m;
	
	int a, b;
	cin >> a >> b;
	for (int i = a; i <= b; i++) {
		for (int j = 0; j < i; j++) {
			int g = gcd(j, i);
			m.insert(to_string(j / g) + "/" + to_string(i / g));
		}
	}

	std::cout << m.size() << endl;
	return 0;
}