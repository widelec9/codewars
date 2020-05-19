using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
//using Codewars._8kyu;
//using Codewars._7kyu;
using Codewars._6kyu;

namespace CodewarsTests
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using NUnit.Framework;

    namespace Solution
    {
        using System;
        using NUnit.Framework;

        [TestFixture]
        public class Tests
        {
            [Test]
            public static void ShouldWorkForSomeExamples()
            {
                Assert.AreEqual("ThIs", Kata.ToWeirdCase("This"));
                Assert.AreEqual("Is", Kata.ToWeirdCase("is"));
                Assert.AreEqual("ThIs Is A TeSt", Kata.ToWeirdCase("This is a test"));
            }
        }
    }
}
