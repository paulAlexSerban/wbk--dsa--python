# Movie Renting System

You have a movie renting company consisting of n shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the currently rented movies.

Each movie is given as a 2D integer array entries where entries[i] = [shopi, moviei, pricei] indicates that there is a copy of movie moviei at shop shopi with a rental price of pricei. Each shop carries at most one copy of a movie moviei.

The system should support the following functions:

- Search: Finds the cheapest 5 shops that have an unrented copy of a given movie. The shops should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopi should appear first. If there are less than 5 matching shops, then all of them should be returned. If no shop has an unrented copy, then an empty list should be returned.
- Rent: Rents an unrented copy of a given movie from a given shop.
- Drop: Drops off a previously rented copy of a given movie at a given shop.
- Report: Returns the cheapest 5 rented movies (possibly of the same movie ID) as a 2D list res where res[j] = [shopj, moviej] describes that the jth cheapest rented movie moviej was rented from the shop shopj. The movies in res should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopj should appear first, and if there is still tie, the one with the smaller moviej should appear first. If there are fewer than 5 rented movies, then all of them should be returned. If no movies are currently being rented, then an empty list should be returned.


Implement the MovieRentingSystem class:
- MovieRentingSystem(int n, int[][] entries) Initializes the MovieRentingSystem object with n shops and the movies in entries.
- List<Integer> search(int movie) Returns a list of shops that have an unrented copy of the given movie as described above.
- void rent(int shop, int movie) Rents the given movie from the given shop.
- void drop(int shop, int movie) Drops off a previously rented movie at the given shop.
- List<List<Integer>> report() Returns a list of cheapest rented movies as described above.
Note: The test cases will be generated such that rent will only be called if the shop has an unrented copy of the movie, and drop will only be called if the shop had previously rented out the movie.

Example 1:
Input
["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
[[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]
Output
[null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]
Explanation
MovieRentingSystem movieRentingSystem = new MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]);
movieRentingSystem.search(1);  // return [1, 0, 2], Movies of ID 1 are unrented at shops 1, 0, and 2. Shop 1 is cheapest; shop 0 and 2 are the same price, so order by shop number.
movieRentingSystem.rent(0, 1); // Rent movie 1 from shop 0. Unrented movies at shop 0 are now [2,3].
movieRentingSystem.rent(1, 2); // Rent movie 2 from shop 1. Unrented movies at shop 1 are now [1].
movieRentingSystem.report();   // return [[0, 1], [1, 2]]. Movie 1 from shop 0 is cheapest, followed by movie 2 from shop 1.
movieRentingSystem.drop(1, 2); // Drop off movie 2 at shop 1. Unrented movies at shop 1 are now [1,2].
movieRentingSystem.search(2);  // return [0, 1]. Movies of ID 2 are unrented at shops 0 and 1. Shop 0 is cheapest, followed by shop 1.

Constraints:
1 <= n <= 3 * 10^5
1 <= entries.length <= 10^5
0 <= shopi < n
1 <= moviei, pricei <= 10^4
Each shop carries at most one copy of a movie moviei.
At most 10^5 calls in total will be made to search, rent, drop and report.

## Algorithmic Patterns Behind the Solution

Let's break down and deepdive into the provided solution for the Movie Renting System, explaining the underlying computer science concepts, algorithms, principles, and design patterns involved.

---

## 1. **Core Data Structures and Concepts**

### a) **Hash Maps (Dictionaries)**
- **`self.price_map = {}`**  
  This dictionary stores the price for each (shop, movie) pair.  
  - **Key**: Tuple `(shop, movie)`
  - **Value**: `price`
  - **Purpose**: Fast O(1) lookup of price for any shop/movie.

### b) **Sorted Lists**
- **`self.available = defaultdict(list)`**  
  For each movie, this maps the movie ID to a sorted list of `(price, shop)` pairs representing the unrented copies available, sorted first by price, then by shop.
- **`self.rented = []`**  
  A single global sorted list of `(price, shop, movie)` for all currently rented movies, sorted by price, shop, movie (the report order).

### c) **Sets**
- **`self.rented_set = set()`**  
  Tracks which (shop, movie) pairs are currently rented.
  - **Purpose**: O(1) membership checks to prevent duplicates and facilitate quick `drop` operations.

---

## 2. **Algorithmic Operations**

### a) **Insertion and Deletion in Sorted Lists**
- Uses the `bisect` module:
  - **`insort(list, value)`**: Inserts `value` in the correct sorted position in `list` (O(n) time).
  - **`bisect_left(list, value)`**: Finds the position to insert or locate `value` in `list`.

**Why sorted lists?**
- They guarantee the order required by the `search` and `report` functions, making it easy to pick the top 5 results efficiently.

### b) **Operations**

#### **Initialization**
- For each entry, insert `(price, shop)` into the corresponding movie's available list in sorted order.
- This ensures initial search queries can be answered efficiently.

#### **Search**
- Retrieve the sorted list of available copies for the movie, and return up to 5 shop IDs, ordered as required.

#### **Rent**
- Remove the chosen `(price, shop)` from the available list (O(n) via bisect).
- Insert `(price, shop, movie)` into the rented list (O(n) via insort).
- Add `(shop, movie)` to the rented set for quick lookups.

#### **Drop**
- Remove `(price, shop, movie)` from the rented list (O(n) via bisect).
- Remove `(shop, movie)` from the rented set.
- Re-insert `(price, shop)` back into the available list for that movie.

#### **Report**
- Return the first 5 entries from the sorted rented list as `[shop, movie]`.

---

## 3. **Computer Science Principles and Practices**

### a) **Encapsulation**
- The class encapsulates all data and operations related to the movie renting system.
- Each method has a clear, single responsibility.

### b) **Separation of Concerns**
- Renting and returning are clearly separated.
- Data for available vs. rented copies are kept separate, avoiding inconsistent state.

### c) **Efficient Search and Update**
- Sorted lists allow for efficient (O(1) or O(5)) retrieval of top results for `search` and `report`.
- Dictionaries and sets allow for O(1) access and updates.

### d) **Correctness in Concurrent State**
- By moving entries between available and rented lists/sets, the system avoids duplicates or missing records even with interleaved rent/drop/search/report calls.

---

## 4. **Design Patterns**

### a) **Command Pattern**
- Each public method (`search`, `rent`, `drop`, `report`) acts as a "command" that can be invoked by the client.

### b) **Data Access Object (DAO)**
- The class acts as a DAO for the movie rental business, abstracting all storage/retrieval logic from the client.

### c) **Flyweight**
- The use of (shop, movie) as keys avoids storing unnecessary data and allows efficient sharing of information.

---

## 5. **Algorithmic Complexity**

- `search(movie)`: O(1) to O(5), since it only inspects the first 5 elements of a sorted list.
- `rent(shop, movie)` and `drop(shop, movie)`: O(n), where n is the number of available or rented copies for a movie (due to list insertion/removal by bisect). For small lists, this is fast, but with many shops, this could be a bottleneck.
- `report()`: O(5), as it just slices the first 5 elements.

**Space Complexity:**  
- O(E), where E is the number of entries, since every `(shop, movie)` appears once in the available list initially and possibly in the rented list during operations.

---

## 6. **Tradeoffs and Alternatives**

- **Alternatives:**
  - Using `SortedList` from `sortedcontainers` (3rd-party lib) would provide O(log n) insertion/removal.
  - A heap could be used, but would require additional tracking to handle duplicates/stale entries.
- **Tradeoff:**  
  - The solution is simple and clear, but insertion/removal in Python built-in lists is O(n), which could be slow for very large n. For the given constraints (1e5 entries), it's acceptable.

---

## 7. **Summary Table**

| Operation | Data Structure      | Complexity | Purpose                           |
|-----------|--------------------|------------|-----------------------------------|
| search    | Sorted List        | O(1..5)    | Top-5 unrented shops for a movie  |
| rent      | Sorted List, Set   | O(n)       | Move from available to rented     |
| drop      | Sorted List, Set   | O(n)       | Move from rented to available     |
| report    | Sorted List        | O(5)       | Top-5 rented movies               |

---

## 8. **Best Practices Highlighted**
- Use of standard library modules (`bisect`, `collections`) for clean code.
- Data normalization: always keeping lists sorted for fast retrieval.
- Clean separation of business logic from data storage.
- Robust state tracking with sets to avoid bugs in state transitions.

---

## 9. **Conclusion**

This design leverages fundamental data structures (dict, set, sorted list), classic search/sort algorithms, and sound OOP principles to deliver a robust, efficient, and correct movie rental system as specified by the problem.  
For very large datasets or higher performance, a more advanced sorted list or tree structure could be used.

## Algorithmic Patterns in the Movie Renting System Solution

### 1. **Algorithmic Patterns Used**
- **Ordered Set / Sorted List Maintenance**:  
  Both the available and rented movies are maintained as sorted lists, allowing efficient insertions, deletions, and range queries.
- **Binary Search (via `bisect`)**:  
  Used for fast insert and search operations in sorted lists, enabling O(log n) complexity for updates and queries.
- **Hash Map for Fast Lookup**:  
  The `price_map` and `rented_set` dictionaries provide fast O(1) access for price lookups and membership checks.

---

### 2. **When is This Pattern Best Used?**
This pattern is best used when you need:
- To frequently insert, delete, and query elements in a sorted order.
- To support retrieval of the k smallest/largest items efficiently.
- To maintain state that changes dynamically but must always be accessed in sorted order.
- When element uniqueness and fast membership checks are also important.

Typical scenarios:
- Order book in trading systems (bid/ask sorted by price).
- Scheduling systems (jobs sorted by priority or time).
- Real-time leaderboards or top-k queries.

---

### 3. **Variations of the Pattern**

**Variation 1: Top-k Elements in a Sliding Window (Heap/SortedList)**
- **Problem Example**:  
  Find the k largest/smallest numbers in the last N elements of a stream.
- **Pattern**:  
  Maintain a min-heap (for top largest) or max-heap (for smallest), or use a balanced BST/SortedList for arbitrary k.
- **Use-case**:  
  Real-time analytics, online event monitoring.

---

**Variation 2: Real-time Leaderboard (Balanced BST/SortedList + Hash Map)**
- **Problem Example**:  
  Design a system to support:  
  - Add or update a player's score.
  - Query the top-k players.
  - Remove a player.
- **Pattern**:  
  SortedList (or TreeMap) for scores; Hash Map for player lookups.
- **Use-case**:  
  Gaming platforms, contest rankings, live competition scoring.

---

**Variation 3: Order Book (Buy/Sell Orders with Price/Time Priority)**
- **Problem Example**:  
  Manage buy/sell orders with price-time priority for a stock exchange.
- **Pattern**:  
  Two balanced BSTs (one for buy, one for sell) sorted by price, with tie-breaker by timestamp.
- **Use-case**:  
  Financial trading platforms, inventory matching, logistics.

---

### **Summary Table**

| Problem Type            | Data Structure Used      | Key Operations             | Example Use-case         |
|-------------------------|-------------------------|----------------------------|--------------------------|
| Top-k in Sliding Window | Heap/SortedList         | Insert, Remove, Top-k      | Stream analytics         |
| Real-time Leaderboard   | SortedList + Hash Map   | Update, Remove, Top-k      | E-sports, contests       |
| Stock Order Book        | Two SortedLists         | Add, Remove, Match, Top-k  | Financial exchanges      |
| Rental System           | SortedList + Hash Map   | Rent, Drop, Search, Report | Movie/library rentals    |

---

### **Why This Pattern Works**
- Sorted structures + auxiliary hash maps allow you to efficiently maintain dynamically changing datasets while always providing the correct answer for top-k (or similar) queries.
- Using `bisect` and `insort` from the Python standard library provides O(log n) operations, which is optimal for these scenarios without external dependencies.

## Bridge Algorithms to Real Engineering

Here are some real-world engineering scenarios where the **algorithmic ideas and patterns** from this Movie Renting System solution are directly applicable, especially in system design, APIs, distributed systems, and databases.

---

### 1. **Booking Systems (Hotels, Cars, Tickets, etc.)**

**Pattern Used:**  
- **Sorted availability pools**: Keep available resources (rooms/cars/seats) sorted by price (and possibly other parameters).
- **Active bookings**: Maintain a sorted/ordered list of current bookings for fast reporting and management.

**How the pattern is applied:**  
- When a user searches for rooms or cars, the system returns the cheapest available options.
- When a booking is made, the resource is atomically moved from the available pool to the booked pool.
- When a booking is cancelled or expired, the resource is moved back to the available pool.
- Reporting (e.g., the list of currently booked rooms by price) is a common admin operation.

**Trade-offs vs. the coding problem:**  
- **Scalability:** In real systems, data is often sharded or distributed, so atomicity and consistency across nodes become a challenge. The coding solution assumes single-threaded, in-memory, atomic operations.
- **Concurrency:** Race conditions must be handled with locks or transactions.
- **Persistence:** Real systems store state in databases, not just memory, so the sorted lists would be implemented as indexed DB queries.
- **Indexing:** Databases use B-trees or similar indexes to maintain sorted order efficiently, analogous to Python’s insort/bisect logic.

---

### 2. **Distributed Job Queues**

**Pattern Used:**  
- **Prioritized scheduling**: Jobs/resources are ordered by priority (e.g., price, urgency) and dequeued in sorted order.

**How the pattern is applied:**  
- Distributed job queues (like Celery, RabbitMQ with priorities, or Kubernetes with resource quotas) often maintain a sorted queue of jobs, selecting the next N jobs for execution based on priority/criteria.
- Jobs that are "rented" (being processed) are moved to an in-progress/reported pool.

**Trade-offs:**  
- **Fairness and starvation:** Real systems must prevent low-priority jobs from being starved.
- **Consistency:** Ensuring a job isn’t picked up by two workers simultaneously is more complex in distributed environments.
- **Failure recovery:** If a process crashes during "renting", the job must be returned to the available pool, similar to "drop".

---

### 3. **Inventory Management Systems in E-Commerce**

**Pattern Used:**  
- **Inventory pools**: For each SKU, maintain a list of available stock sorted by attributes (e.g., oldest expiration, lowest cost).
- **Order processing**: When an order is placed, items are reserved (removed from available), and on cancellation/return, put back.

**How the pattern is applied:**  
- Search for the “best” available inventory for an order.
- Move reserved inventory to a “committed” pool until the transaction completes.
- Reporting: List of committed (but not yet shipped) items.

**Trade-offs:**  
- High concurrency and multi-user edits require DB-level transactions or optimistic concurrency control.
- System must handle partial fulfillment, batch operations, and distributed consistency.

---

### 4. **Online Marketplaces (e.g., booking.com, AirBnB, stock trading)**

**Pattern Used:**  
- **Order books**: Buy/sell/booking offers are kept in price/time order, and matched accordingly.
- **Atomic swaps**: When an offer is accepted, both sides are atomically removed from order books and placed in a “matched” or “executed” pool for reporting.

**How the pattern is applied:**  
- Searching for the best offer is like the `search` operation.
- Accepting an offer is like `rent`, moving from available to matched.
- Cancelling a booking or order returns it to the available pool, akin to `drop`.
- Reporting gives the best matches, similar to `report`.

**Trade-offs:**  
- Matching engines in exchanges must be extremely fast and consistent, often implemented in low-level languages with lock-free data structures.
- Consistency, fairness, and latency are critical.

---

## **Comparing Trade-offs: Coding Problem vs. Real-world System**

| Aspect                   | Coding Problem                             | Real-world System Example         |
|--------------------------|--------------------------------------------|-----------------------------------|
| **Atomicity**            | Implicit (single-threaded, in-memory)      | Explicit (DB transactions, locks) |
| **Concurrency**          | Not a concern                              | Must handle multi-user access     |
| **Persistence**          | In-memory                                  | Persistent storage (DB, disk)     |
| **Scalability**          | Moderate data size                         | Can be huge, distributed          |
| **Indexing**             | Simple sorted list with bisect/insort      | DB indexes, distributed caches    |
| **Consistency**          | Trivial                                    | Complex (eventual/strong)         |
| **Reporting**            | Fast, in-memory slice                      | May require multi-table joins     |
| **Failure Recovery**     | Not needed                                 | Required (crash, rollback)        |
| **Audit/History**        | Not tracked                                | Often logged                      |

---

## **Summary Table: Algorithmic Pattern Mapping**

| Movie Renting System Concept | Real-world Analogue                | Data Structure/Pattern           |
|-----------------------------|-------------------------------------|----------------------------------|
| `available[movie]`          | Inventory pool/Order book/Queue     | Sorted index, priority queue     |
| `rented`                    | Booked/committed/in-progress pool   | Sorted index, join table         |
| `search`                    | List available (by best price)      | Sorted select query              |
| `rent`                      | Reserve/commit/execute              | Atomic move between pools        |
| `drop`                      | Cancel/return/release               | Atomic move between pools        |
| `report`                    | Admin reporting, best matches       | Top-N select/join                |

---

**In short:**  
The core pattern—maintaining two sorted pools and atomically moving items between them—maps directly to booking, inventory, and order-matching systems. The trade-offs in real-world engineering revolve around concurrency, persistence, distributed consistency, and performance at scale. The algorithmic pattern, however, is foundational and widely used!

## Programming Challenge to Career Growth

Mastering this type of algorithm/pattern directly maps to valuable skills for software engineering career growth across several dimensions:

---

## 1. **Daily Engineering Work**

- **Data Structures Mastery:**  
  - You must choose the right data structures for the job (here: sorted lists, sets, efficient search/insertion/removal with `bisect`).
  - Real-world tasks often require you to maintain dynamically changing collections with efficient lookups, insertions, and deletions.
- **Efficiency & Scalability:**  
  - Handling up to 10^5 operations and large datasets trains you to think in terms of time and space complexity.
  - Writing code that remains fast under real workload is a crucial engineering skill.
- **Correctness Under Mutation:**  
  - Handling concurrent-like mutations (rent/drop/search/report) requires careful attention to data consistency.
  - This is common in production systems where state changes rapidly (bookings, reservations, inventory, etc.).

---

## 2. **System Design & Architecture**

- **Modeling Real-World Domains:**  
  - Translating a business process (movie renting) into clean API contracts and stateful logic is a fundamental system design skill.
  - Similar patterns arise in hotel reservations, car rentals, e-commerce stock, etc.
- **State Management and Consistency:**  
  - You learn to separate available and rented states, mirroring how distributed systems must track resource allocation.
  - Understanding how to keep "views" (search, report) consistent with underlying state helps in designing robust services.
- **Extensibility and Maintainability:**  
  - This solution is modular: you can swap in better data structures (`SortedList`, DB-backed indices) or extend for new features (e.g., add user accounts, late fees).
  - Clean separation of concerns prepares you for contributing to and designing larger systems.

---

## 3. **Technical Leadership & Mentoring**

- **Teaching Algorithmic Thinking:**  
  - You can explain why naive approaches (e.g., scanning lists) don’t scale, and teach others to analyze and improve code performance.
- **Evaluating and Reviewing Code:**  
  - Recognizing anti-patterns (e.g., excessive full scans, duplicate state) and suggesting better approaches is a core leadership skill.
- **Guiding Architectural Decisions:**  
  - You will mentor others on state management, when to use in-memory vs. persistent data, and how to design for concurrent access.
- **Translating Business Requirements to Code:**  
  - This exercise is a microcosm of taking requirements from product/business and mapping them into concrete, testable, and maintainable code and APIs—a key leadership responsibility.

---

### **Summary Table**

| Skill Area                | How This Problem/Pattern Helps                        |
|---------------------------|------------------------------------------------------|
| Data Structures/Algorithms| Choosing, using, and teaching efficient containers   |
| Scalability & Complexity  | Writing code that works for large n                  |
| State Management          | Keeping multiple views/indices in sync               |
| Domain Modeling           | Designing APIs & data flow for real-world use cases  |
| Code Review Leadership    | Identifying, explaining, and correcting inefficiencies|
| Mentoring                 | Coaching on best practices and design decisions      |

---

**Mastering this algorithm prepares you to:**
- Build and scale real-world systems.
- Design APIs that reflect business logic.
- Lead teams in writing efficient, robust, and maintainable code.
- Mentor others and perform higher-level architectural reviews.
