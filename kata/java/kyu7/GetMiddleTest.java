package kyu7;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import static org.junit.Assert.assertEquals;

public class GetMiddleTest {
  @Test
  public void evenTests() {
    assertEquals("es", Kata.GetMiddle("test"));
    assertEquals("dd", Kata.GetMiddle("middle"));
  }
  
  @Test
  public void oddTests() {
    assertEquals("t", Kata.GetMiddle("testing"));
    assertEquals("A", Kata.GetMiddle("A"));
  }
}