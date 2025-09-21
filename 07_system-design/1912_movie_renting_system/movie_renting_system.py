from bisect import bisect_left, insort
from collections import defaultdict

class MovieRentingSystem(object):
    def __init__(self, n, entries):
        """
        :type n: int
        :type entries: List[List[int]]
        """
        self.price_map = {}  # (shop, movie) -> price
        self.available = defaultdict(list)  # movie -> sorted [(price, shop)]
        self.rented = []  # sorted [(price, shop, movie)]
        self.rented_set = set()  # (shop, movie)
        for shop, movie, price in entries:
            self.price_map[(shop, movie)] = price
            insort(self.available[movie], (price, shop))

    def search(self, movie):
        """
        :type movie: int
        :rtype: List[int]
        """
        # Return up to 5 shops with unrented copies sorted by price, shop
        return [shop for price, shop in self.available[movie][:5]]

    def rent(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        price = self.price_map[(shop, movie)]
        # Remove from available[movie]
        idx = bisect_left(self.available[movie], (price, shop))
        if 0 <= idx < len(self.available[movie]) and self.available[movie][idx] == (price, shop):
            self.available[movie].pop(idx)
        # Add to rented
        insort(self.rented, (price, shop, movie))
        self.rented_set.add((shop, movie))

    def drop(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        price = self.price_map[(shop, movie)]
        # Remove from rented
        idx = bisect_left(self.rented, (price, shop, movie))
        if 0 <= idx < len(self.rented) and self.rented[idx] == (price, shop, movie):
            self.rented.pop(idx)
        self.rented_set.remove((shop, movie))
        # Add back to available
        insort(self.available[movie], (price, shop))

    def report(self):
        """
        :rtype: List[List[int]]
        """
        return [[shop, movie] for price, shop, movie in self.rented[:5]]
