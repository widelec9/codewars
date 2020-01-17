class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.coll = collection
        self.ipp = items_per_page
        self.pc = 0

    def item_count(self):
        return len(self.coll)

    def page_count(self):
        self.pc = len(self.coll) // self.ipp
        if len(self.coll) % self.ipp > 0:
            self.pc += 1
        return self.pc

    def page_item_count(self, page_index):
        if page_index >= self.pc:
            return -1
        if page_index < self.pc-1:
            return self.ipp
        return len(self.coll) % self.ipp

    def page_index(self, item_index):
        if item_index > len(self.coll)-1 or item_index < 0:
            return -1
        return item_index // self.ipp
