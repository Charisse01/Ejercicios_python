/*hacer un programa que simule un cajero automatico con un saldo inicial de 1000 dólares*/

#include <iostream>
#include <conio.h>
using namespace std;

int main(){
    float saldoInicial = 1000, ingresoDinero, montoRetirar, saldoActual;
    int opcion;

    cout << "-----------------------------" << endl;
    cout << "Bienvenido a tu banca virtual" << endl;
    cout << "-----------------------------" << endl;
    cout << "Seleccione una Opcion" << endl;
    cout << "   1. Concultar Saldo" << endl;
    cout << "   2. Ingresar Dinero" << endl;
    cout << "   3. Retirar Dinero"  << endl;
    cout << "   4. Salir" << endl;
    cin >> opcion;
    system("cls");

    switch(opcion){
        case 1:
            cout << "-- CONSULTA DE SALDO --" << endl;
            cout << "Saldo Actual:  " << saldoInicial;
            break;

        case 2:
            cout << "-- INGRESO DE DINERO --" << endl;
            cout << "ingrese el monto: " << ingresoDinero;
            saldoInicial = saldoInicial + ingresoDinero;
            cout << "Saldo Actual: " << saldoInicial;
            break;

        case 3: 
            cout << "-- RETIRAR DINERO --" << endl;
            cout << "Ingrese monto a retirar: " << montoRetirar;
            if (montoRetirar > saldoInicial){
                cout << "No tiene esa cantidad de dinero ";
            }else {
                saldoActual = saldoInicial - montoRetirar;
                cout << "Saldo Actual: " << saldoInicial;
            }
            break;

        case 4:
            break;
            default:
                cout << "ALERTA: Opcion Incorrecta "<< endl;
    }


    system("pause");
    return 0;
}