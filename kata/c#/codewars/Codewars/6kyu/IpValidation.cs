using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Codewars._6kyu
{
    public class Kata
    {
        public static bool is_valid_IP(string ipAddress)
        {
            bool isValid = false;
            if (ipAddress.Contains('.'))
            {
                string[] ipSplit = ipAddress.Split('.');
                if (ipSplit.Length == 4)
                {
                    foreach (string str in ipSplit)
                    {
                        if (0 <= int.Parse(str) && int.Parse(str) <= 255)
                        {
                            isValid = true;
                        }
                    }
                }
            }

            return isValid;
        }
    }
}
