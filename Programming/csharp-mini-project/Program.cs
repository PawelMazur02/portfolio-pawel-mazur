using System;

namespace Lista1
{
    class Program
    {
        // ZADANIE 1A
        static void Hello(string s)
        {
            Console.WriteLine("Hello " + s);
        }

        // ZADANIE 1B
        static void PrintLegalAge(int age)
        {
            if (age > 18)
            {
                Console.WriteLine("Jesteś pełnoletni!");
            }
            else
            {
                Console.WriteLine("Jesteś nieletni!");
            }
        }

        // ZADANIE 1C
        static void Dzien_tygodnia(int numer_dnia)
        {
            switch (numer_dnia)
            {
                case 1:
                    Console.WriteLine("Poniedziałek");
                    break;
                case 2:
                    Console.WriteLine("Wtorek");
                    break;
                case 3:
                    Console.WriteLine("Środa");
                    break;
                case 4:
                    Console.WriteLine("Czwartek");
                    break;
                case 5:
                    Console.WriteLine("Piątek");
                    break;
                case 6:
                    Console.WriteLine("Sobota");
                    break;
                case 7:
                    Console.WriteLine("Niedziela");
                    break;
                default:
                    Console.WriteLine("Podaj liczbę z przedziału 1-7!");
                    break;
            }
        }

        // ZADANIE 1D
        static void Choroba(bool goraczka, bool suchy_kaszel, bool katar, bool zmeczenie)
        {
            if (!goraczka && !suchy_kaszel && !katar && !zmeczenie)
            {
                Console.WriteLine("Jesteś zdrowy!");
            }
            else if (katar && !goraczka)
            {
                Console.WriteLine("Jesteś przeziębiony!");
            }
            else if (zmeczenie && !goraczka && !suchy_kaszel && !katar)
            {
                Console.WriteLine("Odpocznij!");
            }
            else if (goraczka && suchy_kaszel && katar && zmeczenie)
            {
                Console.WriteLine("Podejrzenie grypy!");
            }
            else if ((goraczka && suchy_kaszel) || (suchy_kaszel && zmeczenie) || (goraczka && suchy_kaszel && zmeczenie))
            {
                Console.WriteLine("Podejrzenie koronawirusa!");
            }
            else
            {
                Console.WriteLine("Nieudana diagnoza!");
            }
        }

        // ZADANIE 2
        public class Bitwise
        {
            public static byte Bitwise_or(byte a, byte b)
            {
                return (byte)(a | b);
            }


            public static byte Bitwise_nand(byte a, byte b)
            {
                return (byte)~(a & b);
            }

            public static byte Bitwise_impl(byte a, byte b)
            {
                return (byte)(~a | b);
            }

            public static string Convert2bit(byte b)
            {
                string result = "";
                while (b > 0)
                {
                    result = (b % 2).ToString() + result;
                    b /= 2;
                }
                return result;
            }
        }

        // ZADANIE 3
        public class SimpleOperations
        {
            public static double Add(double a, double b)
            {
                return a + b;
            }

            public static double Sub(double a, double b)
            {
                return a - b;
            }

            public static double Mult(double a, double b)
            {
                return a * b;
            }

            public static double Div(double a, double b)
            {
                if (a == 0 || b == 0)
                {
                    return double.NaN;
                }

                return a / b;
            }

            public static bool Eq(double n, double k)
            {
                return n == k;
            }
        }

        // ZADANIE 4


        public static class Algorithms
        {
            public static int factorial(int n)
            {
                int result = 1;
                for (int i = 2; i <= n; i++)
                {
                    result *= i;
                }
                return result;
            }

            public static int factorial_rek(int n)
            {
                if (n == 0)
                {
                    return 1;
                }
                else
                {
                    return n * factorial_rek(n - 1);
                }
            }

            public static int gcd(int a, int b)
            {
                while (b != 0)
                {
                    int temp = b;
                    b = a % b;
                    a = temp;
                }
                return a;
            }

            public static string dec2bin(int dec)
            {
                string result = "";
                while (dec > 0)
                {
                    int bit = dec % 2;
                    result = bit + result;
                    dec /= 2;
                }
                return result;
            }
        }

        // ZADANIE 5
        public class ConsoleDraw
        {
            public static void Triangle(int n, bool upside = false)
            {
                int height = upside ? n : 1;
                int step = upside ? -1 : 1;
                for (int i = 1; i <= n; i++)
                {
                    for (int j = 1; j <= height; j++)
                    {
                        Console.Write("*");
                    }
                    Console.WriteLine();
                    height += step;
                    if (height == 0)
                    {
                        break;
                    }
                }
            }

            public static void diamond(int n)
            {
                Triangle(n / 2 + 1);
                Triangle(n / 2, true);
            }
        }


        static void Main(string[] args)
        {
            // ZADANIE 1A
            Hello("Paweł");

            // ZADANIE 1B
            PrintLegalAge(21);

            // ZADANIE 1C
            Dzien_tygodnia(5);

            // ZADANIE 1D
            Choroba(true, true, true, true);

            // ZADANIE 2
            Console.WriteLine(Bitwise.Convert2bit(Bitwise.Bitwise_or(0b11000000, 0b00000011)));

            // ZADANIE 3
            double wynik2 = SimpleOperations.Add(1.23, 4.56);
            Console.WriteLine(wynik2);

            // ZADANIE 4
            int wynik3 = Algorithms.factorial(6);
            Console.WriteLine(wynik3);

            // ZADANIE 5
            ConsoleDraw.Triangle(5, true);
            ConsoleDraw.Triangle(5);
            ConsoleDraw.diamond(10);

            //CZEKAJ
            Console.ReadKey();
        }
    }
}

