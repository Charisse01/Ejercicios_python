#include <iostream>

using namespace std;

int main() {
    int opcion;
    double num1, num2;

    cout << "Operaciones disponibles:" << endl;
    cout << "1. Suma" << endl;
    cout << "2. Resta" << endl;
    cout << "3. Multiplicacion" << endl;
    cout << "4. Division" << endl;

    cout << "Selecciona una operacion (1/2/3/4): ";
    cin >> opcion;

    cout << "Ingresa el primer numero: ";
    cin >> num1;

    cout << "Ingresa el segundo numero: ";
    cin >> num2;

    if (opcion == 1) {
        cout << num1 + num2 << endl;
        } else if (opcion == 2) {
            cout << num1 - num2 << endl;
        } else if (opcion == 3) {
            cout << num1 * num2 << endl;
        } else if (opcion == 4) {
            cout << num1 / num2 << endl;
        } else {
            cout << "Entrada inválida" << endl;
        }

    return 0;
}
