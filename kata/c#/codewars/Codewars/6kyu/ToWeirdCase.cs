using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Codewars._6kyu
{
    using System.Linq;
    public class Kata
    {
        public static string ToWeirdCase(string s)
        {
            //List<string> outList = new List<string>();

            //foreach (string word in s.Split(' '))
            //{
            //    outList.Add(string.Join("", word.Select((c, i) => i % 2 == 0 ? Char.ToUpper(c) : Char.ToLower(c))));
            //}

            //return string.Join(" ", outList);

            return string.Join(" ", s.Split(' ').Select(word => string.Concat(word.Select((c, i) => i % 2 == 0 ? char.ToUpper(c) : char.ToLower(c)))));
        }
    }
}