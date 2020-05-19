using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Codewars._7kyu
{
    using System;
    using System.Linq;

    public static class Kata
    {
        public static int GetVowelCount(string str)
        {
            return str.Count(c => "aeiou".Contains(c));
        }
    }
}
