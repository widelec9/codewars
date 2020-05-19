using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Codewars._6kyu
{
    public class SumDigPower
    {

        public static long[] SumDigPow(long a, long b)
        {
            List<long> outValues = new List<long>();

            for (var x = a; x <= b; ++x)
            {
                double sum = x.ToString().Select((ch, i) => Math.Pow(Char.GetNumericValue(ch), i + 1)).Sum();
                if ((int)sum == x)
                {
                    outValues.Add(x);
                }
            }

            return outValues.ToArray();
        }
    }
}
