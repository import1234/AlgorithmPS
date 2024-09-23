#include <iostream>
#include <cmath>
using namespace std;

#define MAX 100000000
bool p[MAX];
unsigned long long mod = pow(2, 32);
unsigned long long ans = 1;

int main(void) {
	int n;
	cin >> n;

	for (int i = 2; i < MAX; i++)
		p[i] = 1;
	for (int i = 2; i * i < MAX; i++)
		if (p[i])
			for(int j = i * i; j < MAX; j += i)
				p[j] = 0;

	for (int i = 2; i < MAX; i++)
		if (p[i]) {
			unsigned long long exponent = log(n) / log(i);
			for (int j = 0; j < exponent; j++)
				ans = (ans * i) % mod;
		}

	cout << ans << endl;

	return 0;
}