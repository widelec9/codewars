package kyu5;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class PaginationHelperTest {
	@Test
	public void testSomething() {
		PaginationHelper<Character> helper = new PaginationHelper<Character>(Arrays.asList('a', 'b', 'c', 'd', 'e', 'f'), 4);
		assertEquals(2, helper.pageCount()); //should == 2
		assertEquals(6, helper.itemCount()); //should == 6
		assertEquals(4, helper.pageItemCount(0)); //should == 4
		assertEquals(2, helper.pageItemCount(1)); // last page - should == 2
		assertEquals(-1, helper.pageItemCount(2)); // should == -1 since the page is invalid

		// pageIndex takes an item index and returns the page that it belongs on
		assertEquals(1, helper.pageIndex(5)); //should == 1 (zero based index)
		assertEquals(0, helper.pageIndex(2)); //should == 0
		assertEquals(-1, helper.pageIndex(20)); //should == -1
		assertEquals(-1, helper.pageIndex(-10)); //should == -1
	}
	
	@Test
	public void testSomethingElse() {
		PaginationHelper<Integer> helper = new PaginationHelper<Integer>(IntStream.rangeClosed(1, 24).boxed().collect(Collectors.toList()), 10);
		assertEquals(10, helper.pageItemCount(0));
		assertEquals(10, helper.pageItemCount(1));
		assertEquals(4, helper.pageItemCount(2));
		
		assertEquals(2, helper.pageIndex(21));
		assertEquals(2, helper.pageIndex(22));
		assertEquals(2, helper.pageIndex(23));
	}
}