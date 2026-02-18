#include <iostream>
#include <cmath>

using namespace std;

double f(float x) {
    return x * x * x * x - 18 * x - 10;
}

double dihotomi(double a, double b, double eps) 
{
    double c = 0;
    int count_iter = 0;
    do
    {
        c = (a + b) / 2;

        if (f(a) * f(c) < 0)
        {
            b = c;
        }
        if (f(b) * f(c) < 0)
        {
            a = c;
        }
        count_iter++;
        //cout << "a: " << a << "\nb: " << b << "\nc: " << c << "\nf: " << f(c) << endl; 
    } while (fabs(f(c)) > eps);

    cout << "Метод дихотомии: x0 = "<< c << ", f(x0) = " << f(c) << endl << "Количество итераций: " << count_iter << endl << endl;

    return c;
}

double dotOfLine(double x_1, double x_2)
{
    double y_1 = f(x_1);
    double y_2 = f(x_2);

    double x_0 = x_1 - y_1 * (x_2 - x_1) / (y_2 - y_1);

    return x_0;
}

double MethodHords(double a, double b, double eps) 
{
    double c = 0;
    int count_iter = 0;
    do
    {
        c = dotOfLine(a, b);

        if (f(a) * f(c) < 0)
        {
            b = c;
        }
        if (f(b) * f(c) < 0)
        {
            a = c;
        }
        count_iter++;
        //cout << "a: " << a << "\nb: " << b << "\nc: " << c << "\nf: " << f(c) << endl; 
    } while (fabs(f(c)) > eps);

    cout << "Метод хорд: x0 = "<< c << ", f(x0) = " << f(c) << endl << "Количество итераций: " << count_iter << endl << endl;

    return c;
}

int main()
{
    double a = -5.0, b = 0.0, eps = 0.0001;

    cout << "Отрезок: (" << a << ", " << b << ")" << endl << endl;

    double x_dih = dihotomi(a, b, eps);
    double x_hord = MethodHords(a, b, eps);

    cout << "Дельта методов: по x = " << fabs(f(x_dih) - f(x_hord)) << endl;

    return 0;
}
