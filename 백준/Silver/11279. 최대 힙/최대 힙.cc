#include <iostream>
#include <cmath>

using namespace std;


int heap[200000];
int heapSize;

void upHeap(int q) {
	heap[1 + heapSize++] = q;
	int now = heapSize;
	while (now > 1 && heap[now / 2] < heap[now]) {
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
	while (!(heap[now] >= heap[2 * now] && heap[now] >= heap[2 * now + 1])) {
		if (heap[2 * now] + heap[2 * now + 1] == 0) break;
		if (heap[2 * now] > heap[2 * now + 1]) {
			swap(heap[now], heap[2 * now]);
			now *= 2;
		}
		else {
			swap(heap[now], heap[2 * now + 1]);
			now = 2 * now + 1;
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
	heap[0] = -100;

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