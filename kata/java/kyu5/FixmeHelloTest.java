package kyu5;

import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class FixmeHelloTest {
  
  @Test
  public void testBob27Male() {
    FixmeHello dm = new FixmeHello().setName("Bob").setAge(27).setSex('M');
    String expected = "Hello. My name is Bob. I am 27. I am male.";
    assertEquals(expected, dm.hello());
  }  
  
  @Test
  public void test27MaleBob() {
    FixmeHello dm = new FixmeHello().setAge(27).setSex('M').setName("Bob");
    String expected = "Hello. I am 27. I am male. My name is Bob.";
    assertEquals(expected, dm.hello());
  }    
  
  @Test
  public void testAliceFemale() {
    FixmeHello dm = new FixmeHello().setName("Alice").setSex('F');
    String expected = "Hello. My name is Alice. I am female.";
    assertEquals(expected, dm.hello());
  }   
  
  @Test
  public void testBatman() {
    FixmeHello dm = new FixmeHello().setName("Batman");
    String expected = "Hello. My name is Batman.";
    assertEquals(expected, dm.hello());
  }    
  
  @Test
  public void testMultipleAge() {
	  FixmeHello dm = new FixmeHello().setAge(25).setName("Sally").setAge(39);
	  String expected = "Hello. I am 39. My name is Sally.";
	  assertEquals(expected, dm.hello());
  }
  
}