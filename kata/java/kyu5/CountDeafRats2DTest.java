package kyu5;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class CountDeafRats2DTest {

  @Test
  public void ex1() {
    assertEquals(1, CountDeafRats2D.countDeafRats(
      new char[][] {            
        "↗ P     ".toCharArray(),
        "  ↘    ↖".toCharArray(),
        "  ↑     ".toCharArray(),
        "↗       ".toCharArray(),
      }
    ));
  }

  @Test
  public void ex2() {
    assertEquals(7, CountDeafRats2D.countDeafRats(
      new char[][] {
        "        ↗".toCharArray(),
        "P ↓   ↖ ↑".toCharArray(),
        "    ←   ↓".toCharArray(),
        "  ↖ ↙   ↙".toCharArray(),
        "↓ ↓ ↓    ".toCharArray()
      }
    ));
  }

  @Test
  public void ratsComing() {
    assertEquals(0, CountDeafRats2D.countDeafRats(
      new char[][] {            
        "↘ ↓ ↙".toCharArray(),
        "→ P ←".toCharArray(),
        "↗ ↑ ↖".toCharArray()
      }
    ));
  }

  @Test
  public void ratsGoing() {
    assertEquals(8, CountDeafRats2D.countDeafRats(
      new char[][] {            
        "↖ ↑ ↗".toCharArray(),
        "← P →".toCharArray(),
        "↙ ↓ ↘".toCharArray()
      }
    ));
  }

}