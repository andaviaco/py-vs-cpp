#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
	int n;

	do {
		cout << "Dame un número: ";
		cin >> n;
		if(n < 1) {
			cout << "Número inválido";
		}
	} while(n < 1);

	if (n == 1) {
		cout << n << " NO es un número primo." << endl;
	} else {
		for (int i=2; i <= n; i++) {
			if (n % i == 0) {
				if (n != i) {
					cout << n << " NO es un número primo." << endl;
					return 0;
				} else {
					cout << n << " Si es un número primo." << endl;
				}
			}
		}
	}


	return 0;
}