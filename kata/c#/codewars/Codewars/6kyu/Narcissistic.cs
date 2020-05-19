using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Codewars._6kyu
{
    public class Kata
    {
        public static bool Narcissistic(int value)
        {
            string valStr = value.ToString();
            double sum = valStr.Sum(c => Math.Pow(Convert.ToInt16(c.ToString()), valStr.Length));
            return (int)sum == value;
        }
    }
}
