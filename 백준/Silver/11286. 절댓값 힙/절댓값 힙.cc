#include <iostream>
#include <cmath>

using namespace std;


int heap[200001];
int heapSize;

bool check(int a, int b) { //b가 a보다 앞이어야 하면
	return b!=0 && (abs(a) > abs(b) || (a == -b && b < 0));
}

void upHeap(int q) {
	heap[1 + heapSize++] = q;
	int now = heapSize;
	while (now > 1 && check(heap[now / 2], heap[now])) {
		swap(heap[now / 2], heap[now]);
		now /= 2;
	}
}

void downHeap() {
	if (!heapSize) {
		cout << 0 << '\n';
		return;
	}
	cout << heap[1] << '\n';
	heap[1] = heap[heapSize];
	heap[heapSize--] = 0;
	int now = 1;
	while (check(heap[now],heap[2*now]) || check(heap[now], heap[2 * now + 1])) {
		if (check(heap[2* now], heap[2 * now+1])) {
			swap(heap[now], heap[2 * now+1]);
			now = 2 * now + 1;
		}
		else{
			swap(heap[now], heap[2 * now]);
			now *= 2;
		}
	}
}

void showHeap() {
	cout << '\n';
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < (1 << i); j++) {
			int idx = pow(2, i) + j;
			cout << heap[idx] << ' ';
		}
		cout << '\n';
	}
}

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, q;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> q;
		if (q)
			upHeap(q);
		else
			downHeap();
		//showHeap();
	}

	return 0;
}