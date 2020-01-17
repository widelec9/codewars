package kyu5;

import java.util.ArrayList;
import java.util.List;

public class PaginationHelper<I> {
	private List<List<I>> pagesList = new ArrayList<List<I>>();
	private int itemsPerPage = 0;
	
	/**
	* The constructor takes in an array of items and a integer indicating how many
	* items fit within a single page
	*/
	public PaginationHelper(List<I> collection, int itemsPerPage) {
		this.itemsPerPage = itemsPerPage;
		int collectionSize = collection.size();
		for (int i = 0; i < collectionSize; i += itemsPerPage) {
			pagesList.add(collection.subList(i, Math.min(i + itemsPerPage, collectionSize)));
		}
	}
	
	/**
	* returns the number of items within the entire collection
	*/
	public int itemCount() {
		int itemCounter = 0;
		for (List<I> page : pagesList) {
			itemCounter += page.size();
		}
		return itemCounter;
	}
	
	/**
	* returns the number of pages
	*/
	public int pageCount() {
		return pagesList.size();
	}
	
	/**
	* returns the number of items on the current page. page_index is zero based.
	* this method should return -1 for pageIndex values that are out of range
	*/
	public int pageItemCount(int pageIndex) {
		if (pageIndex >= pagesList.size()) {
			return -1;
		}
		return pagesList.get(pageIndex).size();
	}
	
	/**
	* determines what page an item is on. Zero based indexes
	* this method should return -1 for itemIndex values that are out of range
	*/
	public int pageIndex(int itemIndex) {
		if (itemIndex > itemCount()-1 || itemIndex < 0) {
			return -1;
		}
		return itemIndex / itemsPerPage;
	}
}