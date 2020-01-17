package kyu5;

import static org.junit.Assert.*;
import java.util.HashMap;
import java.util.Map;
import org.junit.Test;

public class TourTest {

//	@Test
//	public void test1() {
//		String[] friends1 = new String[] { "A1", "A2", "A3", "A4", "A5" };
//		String[][] fTowns1 = { new String[] {"A1", "X1"}, new String[] {"A2", "X2"}, new String[] {"A3", "X3"}, 
//			new String[] {"A4", "X4"} };
//		Map<String, Double> distTable1 = new HashMap<String, Double>();
//			distTable1.put("X1", 100.0); distTable1.put("X2", 200.0); distTable1.put("X3", 250.0); 
//			distTable1.put("X4", 300.0);
//		assertEquals(889, Tour.tour(friends1, fTowns1, distTable1));
//	}
	
	@Test
	public void test3() {
		String[] friends3 = new String[] { "B1", "B2" };
		String[][] fTowns3 = { new String[] {"B1", "Y1"}, new String[] {"B2", "Y2"}, new String[] {"B3", "Y3"}, 
			new String[] {"B4", "Y4"}, new String[] {"B5", "Y5"} };
		Map<String, Double> distTable3 = new HashMap<String, Double>();
			distTable3.put("Y1", 50.0); distTable3.put("Y2", 70.0); distTable3.put("Y3", 90.0); 
			distTable3.put("Y4", 110.0); distTable3.put("Y5", 150.0);
		assertEquals(168, Tour.tour(friends3, fTowns3, distTable3));
	}
}
  