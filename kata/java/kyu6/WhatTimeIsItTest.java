package kyu6;

import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class WhatTimeIsItTest {

//  @Test
//  public void test1200() {
//    assertEquals("12:00", WhatTimeIsIt.whatTimeIsIt(0));
//    assertEquals("12:00", WhatTimeIsIt.whatTimeIsIt(360));
//  }
//
//  @Test
//  public void test0300() {
//    assertEquals("03:00", WhatTimeIsIt.whatTimeIsIt(90));
//  }
//
//  @Test
//  public void test0600() {
//    assertEquals("06:00", WhatTimeIsIt.whatTimeIsIt(180));
//  }
//
//  @Test
//  public void test0900() {
//    assertEquals("09:00", WhatTimeIsIt.whatTimeIsIt(270));
//  }
//  
  @Test
  public void testRandom() {
	  assertEquals("06:19", WhatTimeIsIt.whatTimeIsIt(189.853d));
  }
    
}