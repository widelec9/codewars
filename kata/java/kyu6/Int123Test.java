package kyu6;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;


public class Int123Test {

  private void doIntTest(final int a) {
    final long b = Int123.int123(a);
    System.out.println("" + a + " + " + b + " = " + (int)(a+b));
    assertTrue("B must be >= 0", b >= 0);
    assertEquals("A + B must give 123", 123, (int)(a+b));
  }
  
  @Test
  public void testLess() {
    doIntTest(0);
  }
  
  @Test
  public void testSame() {
    doIntTest(123);
  }

  @Test
  public void testGreater() {
    doIntTest(500);
  }
  
  @Test
  public void testMax() {
    doIntTest(2147483647);
  }
  
  @Test
  public void testMin() {
    doIntTest(-2147483648);
  }
  
  @Test
  public void testRandom1() {
    doIntTest(1494);
  }
  
  @Test
  public void testRandom2() {
    doIntTest(-7390);
  }
  
}