#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
	int t,cont=0;
	char c;

	do {
		cout << "Qué tamaño de triángulo quieres?: ";
		cin >> t;
	} while (t > 80 or t < 1);
	cout << "Qué caractér quieres que use?: ";
	cin >> c;


	for (int i=0; i < t; i++) {
		for (int j=0; j < i; j++) {
			cout << c;
		}
		cout << endl;
	}

	for (int k=0; k < t; k++) {
		for (int m=t; m > k; m--) {
			cout << c;
		}
		cout << endl;
	}
	
	return 0;
}