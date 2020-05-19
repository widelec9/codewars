using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Codewars._6kyu
{
    using System.Net;
    public class Kata
    {
        public static bool is_valid_IP(string ipAddress)
        {
            IPAddress ipAddr;
            bool isValid = IPAddress.TryParse(ipAddress, out ipAddr);
            return isValid && ipAddr.ToString().Equals(ipAddress);
        }
    }
}
