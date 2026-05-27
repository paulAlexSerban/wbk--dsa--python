# Food Rating System

Design a food rating system that can do the following:
- Modify the rating of a food item listed in the system.
- Return the highest-rated food item for a type of cuisine in the system.

Implement the FoodRatings class:
- `FoodRatings(String[] foods, String[] cuisines, int[] ratings)` Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
- `foods[i]` is the name of the ith food
- `cuisines[i]` is the type of cuisine of the ith food
- `ratings[i]` is the initial rating of the ith food
- `void changeRating(String food, int newRating)` Changes the rating of the food item with the name food.
- `String highestRated(String cuisine)` Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.

> Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

 

Example 1:
**Input**
`["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]`

`[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]`
**Output**
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]
**Explanation**
FoodRatings 

`foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);`

`foodRatings.highestRated("korean"); // return "kimchi" => "kimchi" is the highest rated korean food with a rating of 9.`
`foodRatings.highestRated("japanese"); // return "ramen" => "ramen" is the highest rated japanese food with a rating of 14.`
`foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.`
`foodRatings.highestRated("japanese"); // return "sushi" => "sushi" is the highest rated japanese food with a rating of 16.`
`foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.`
`foodRatings.highestRated("japanese"); // return "ramen" => Both "sushi" and "ramen" have a rating of 16. - However, "ramen" is lexicographically smaller than "sushi".`
 

Constraints:
- 1 <= n <= 2 * 10^4
- `n == foods.length == cuisines.length == ratings.length`
- `1 <= foods[i].length`, `cuisines[i].length <= 10`
- `foods[i]`, `cuisines[i]` consist of lowercase English letters.
- 1 <= `ratings[i]` <= 10^8
- All the strings in foods are distinct.
- food will be the name of a food item in the system across all calls to changeRating.
- cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated.
- At most 2 * 10^4 calls in total will be made to changeRating and highestRated.

### Solution Breakdown & Deepdive
Break down of the **computer science concepts, algorithms, principles, and practices** used to solve the **Food Rating System** problem (like LeetCode 2353):

### 1. **Data Structures**

#### a. **Hash Maps (Dictionaries)**
- Used for **constant time** lookup and update.
- **food_info:** Maps food name → (cuisine, rating)
- **food_rating:** Maps food name → current rating
- **cuisine_heap:** Maps cuisine → heap (priority queue) of available foods for that cuisine

#### b. **Priority Queue / Heap**
- Used to **quickly retrieve the highest-rated** food for each cuisine.
- In Python, `heapq` is a min-heap, so we store ratings as **negative numbers** to simulate a max-heap.
- Each cuisine has its own heap: **cuisine → [(-rating, food_name), ...]**
- Heap allows O(1) access to the top-rated food and O(log n) insertion/removal.

---

### 2. **Algorithmic Principles**

#### a. **Heap with Lazy Deletion (Stale Entries)**
- When a food’s rating changes, **push the new entry** to the heap, but don’t remove the old one.
- On retrieval (`highestRated`), **pop entries** until the top entry matches the current rating.
- This avoids O(n) time to find and update heap entries.

#### b. **Lexicographical Ordering**
- For tie-breaking: If multiple foods have the same rating, the one with the alphabetically smallest name is chosen.
- Heap stores tuples: `(-rating, food_name)`; Python’s tuple comparison ensures correct ordering.

---

### 3. **Time Complexity**
- **Initialization:** O(n log n) (heap insertions)
- **changeRating:** O(log n) (heap insertion)
- **highestRated:** O(log n) (potentially more if popping stale entries, but each entry is only popped once)

---

### 4. **Best Practices**

#### a. **Separation of Concerns**
- Data is cleanly separated: food info, ratings, cuisine heaps.

#### b. **Efficient Updates**
- No need to search and remove old heap entries; just let them become stale and skip them during retrieval.

#### c. **Scalability**
- All operations are efficient enough for large n (up to 2×10⁴ foods and operations).

---

### 5. **Summary of Concepts Used**
- **Hash maps** for fast lookups and updates.
- **Heaps** for efficient max/min retrieval.
- **Lazy deletion** to keep updates efficient.
- **Tuple ordering** for lexicographical tie-breaking.
- **Amortized efficiency** via heap operations.
