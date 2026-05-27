import heapq

class FoodRatings(object):
    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        # Map food -> (cuisine, rating)
        self.food_info = {}
        # Map cuisine -> heap of (-rating, food)
        self.cuisine_heap = {}
        # Map food -> current rating (for quick lookup/validation)
        self.food_rating = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = (cuisine, rating)
            self.food_rating[food] = rating
            if cuisine not in self.cuisine_heap:
                self.cuisine_heap[cuisine] = []
            heapq.heappush(self.cuisine_heap[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        cuisine, _ = self.food_info[food]
        self.food_info[food] = (cuisine, newRating)
        self.food_rating[food] = newRating
        heapq.heappush(self.cuisine_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        heap = self.cuisine_heap[cuisine]
        while heap:
            rating_neg, food = heap[0]
            # Is it current?
            if self.food_rating[food] == -rating_neg:
                return food
            # Otherwise, pop and continue
            heapq.heappop(heap)