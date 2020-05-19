using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Codewars._7kyu
{
    public class Kata
    {
        public static IEnumerable<string> OpenOrSenior(int[][] data)
        {
            return data.Select(player => player[0] >= 55 && player[1] > 7 ? "Senior" : "Open").ToList();
        }
    }
}
