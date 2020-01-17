package kyu5;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class CountDeafRatsTest {

  @Test
  public void ex1() {
    assertEquals(0, CountDeafRats.countDeafRats("~O~O~O~O P"));
  }
  
  @Test
  public void ex2() {
    assertEquals(1, CountDeafRats.countDeafRats("P O~ O~ ~O O~"));
  }
  
  @Test
  public void ex3() {
    assertEquals(2, CountDeafRats.countDeafRats("~O~O~O~OP~O~OO~"));
  }
  
}