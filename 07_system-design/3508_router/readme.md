# Implement Router
Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:

- source: A unique identifier for the machine that generated the packet.
- destination: A unique identifier for the target machine.
- timestamp: The time at which the packet arrived at the router.

Implement the Router class:
- `Router(int memoryLimit)`: Initializes the Router object with a fixed memory limit.
- `memoryLimit` is the maximum number of packets the router can store at any given time.
- If adding a new packet would exceed this limit, the oldest packet must be removed to free up space.
- `bool addPacket(int source, int destination, int timestamp)`: Adds a packet with the given attributes to the router.
- A packet is considered a duplicate if another packet with the same source, destination, and timestamp already exists in the router.
- Return true if the packet is successfully added (i.e., it is not a duplicate); otherwise return false.
- `int[] forwardPacket()`: Forwards the next packet in FIFO (First In First Out) order.

Remove the packet from storage.
- Return the packet as an array [source, destination, timestamp].
- If there are no packets to forward, return an empty array.
- `int getCount(int destination, int startTime, int endTime)`:

Returns the number of packets currently stored in the router (i.e., not yet forwarded) that have the specified destination and have timestamps in the inclusive range [startTime, endTime].
Note that queries for addPacket will be made in increasing order of timestamp.

Example 1:
Input:
["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]
[[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]

Output:
[null, true, true, false, true, true, [2, 5, 90], true, 1]

Explanation
-  Router router = new Router(3); // Initialize Router with memoryLimit of 3.
- router.addPacket(1, 4, 90); // Packet is added. Return True.
- router.addPacket(2, 5, 90); // Packet is added. Return True.
- router.addPacket(1, 4, 90); // This is a duplicate packet. Return False.
- router.addPacket(3, 5, 95); // Packet is added. Return True
- router.addPacket(4, 5, 105); // Packet is added, [1, 4, 90] is removed as number of packets exceeds memoryLimit. Return True.
- router.forwardPacket(); // Return [2, 5, 90] and remove it from router.
- router.addPacket(5, 2, 110); // Packet is added. Return True.
- router.getCount(5, 100, 110); // The only packet with destination 5 and timestamp in the inclusive range [100, 110] is [4, 5, 105]. Return 1.


Example 2:
Input:
["Router", "addPacket", "forwardPacket", "forwardPacket"]
[[2], [7, 4, 90], [], []]

Output:
[null, true, [7, 4, 90], []]

Explanation
- Router router = new Router(2); // Initialize Router with memoryLimit of 2.
- router.addPacket(7, 4, 90); // Return True.
- router.forwardPacket(); // Return [7, 4, 90].
- router.forwardPacket(); // There are no packets left, return [].
 

Constraints:

- 2 <= memoryLimit <= 10^5
- 1 <= source, destination <= 2 * 10^5
- 1 <= timestamp <= 10^9
- 1 <= startTime <= endTime <= 10^9
- At most 10^5 calls will be made to addPacket, forwardPacket, and getCount methods altogether.
queries for addPacket will be made in increasing order of timestamp.

## Algorithmic Patterns Behind the Solution

### 1. **Sliding Window / Bounded Buffer Pattern**

**Pattern Description:**  
The Router problem fundamentally relies on the **Sliding Window** (or **Bounded Buffer**) pattern. This pattern manages a "window" or buffer of a fixed size over a stream of input. As new items enter and the window is full, the oldest items are evicted. In this solution, the `deque` structure represents the window, maintaining the FIFO order and enforcing the memory limit.

**Best Use Cases:**  
Use the Sliding Window pattern when you must process or retain only a fixed number of recent items from a stream, such as:
- Rate limiting network requests (e.g., allow up to N actions in the last T seconds)
- Real-time analytics over recent events (e.g., moving average/maximum)
- Buffering data with resource constraints (e.g., limited memory or queue size)


### 2. **Hash Set for Deduplication Pattern**

**Pattern Description:**  
The solution uses a **Hash Set for Deduplication** to ensure no duplicate packets are added. When each incoming packet’s `(source, destination, timestamp)` tuple is checked against the set, the deduplication operation is O(1) on average.

**Best Use Cases:**  
Use a hash set for deduplication when you need to efficiently check for existence or uniqueness among a dynamic set of items, such as:
- Removing duplicates in a stream of data
- Caching results or objects for quick lookup
- Ensuring idempotency in APIs or workflows


### 3. **Indexed Search with Sorted Lists and Binary Search (Bisect) Pattern**

**Pattern Description:**  
To count packets with a destination and timestamp in a range, the solution maps each destination to a sorted list of timestamps. Using Python’s `bisect` module, it performs fast binary searches for efficient range queries.

**Best Use Cases:**  
This pattern is ideal when you need to perform fast range or interval queries, such as:
- Time-series analytics (e.g., events within a given time window)
- Finding all records in a database within a certain range (price, date, etc.)
- Scheduling and calendar applications


### Variations of the Pattern with Different Problem Types

### Variation 1: Sliding Window Maximum (LeetCode 239)

**Problem:**  
Given an array and a window size k, return the maximum value in each window as it slides through the array.

**Pattern:**  
Sliding Window with a double-ended queue (deque) to maintain max candidates.


### Variation 2: LRU Cache (LeetCode 146)

**Problem:**  
Design a data structure that supports O(1) get and put methods for a fixed-size cache, evicting the least recently used item when full.

**Pattern:**  
Bounded buffer with a combination of a doubly-linked list for recency order and a hash map for O(1) lookup.


### Variation 3: Distinct Elements in Window

**Problem:**  
Given a stream or array, find the number of distinct elements in every window of size k.

**Pattern:**  
Sliding Window + Hash Map/Set for fast lookup and count of unique elements.


### Summary

The Router problem elegantly combines the **Sliding Window/Bounded Buffer**, **Deduplication with a Hash Set**, and **Indexed Search with Binary Search** patterns. These patterns are best used for stream processing, caches, deduplication, real-time analytics, and efficient range queries.  
By understanding these patterns, you can adapt solutions to a wide variety of software engineering challenges, from network systems to analytics and beyond.

## Real-World Engineering Scenarios for the Router Algorithm Pattern

### 1. **Network Hardware Routers & Switches (Packet Buffers)**
- **Scenario:**  
  Commercial routers and switches use hardware buffers (typically FIFO queues) to temporarily store incoming packets. Buffers have a strict memory limit (dictated by chip cost, energy, and latency). When the buffer is full, the oldest packets are dropped (tail drop) or overwritten—mirroring the memoryLimit/ejection logic in your Router.
- **Duplicate Detection:**  
  While hardware rarely checks for exact duplicates (due to speed constraints), some high-level network appliances or custom software routers may filter out retransmits or duplicate frames using hash tables, similar to your `set` for packet keys.
- **Trade-off:**  
  - **Coding Problem:** You have perfect, O(1) duplicate checks and clean eviction.
  - **Real World:** Hardware often trades off duplicate detection for raw speed and deterministic latency; software routers (e.g., Linux tc, DPDK) may implement deduplication as a best-effort, sometimes with probabilistic structures (like Bloom filters) for speed.

### 2. **Message Queues (Kafka, RabbitMQ, etc.)**
- **Scenario:**  
  Distributed message brokers maintain a bounded queue (topic partition, buffer) per consumer or topic. When the queue is full, the oldest messages are dropped or moved to slower storage, matching your FIFO packet eviction.
- **Duplicate Detection:**  
  Some systems track unique message IDs to prevent re-processing, using sets or indexes—directly analogous to your deduplication logic.
- **Trade-off:**  
  - **Coding Problem:** Memory is fixed; eviction is exact and immediate.
  - **Real World:** Many brokers allow for tuning (e.g., time-based retention, disk spill, dead-letter queues) and must handle persistence, replication, and crash recovery, adding complexity.

### 3. **API Rate Limiting and Quota Enforcement**
- **Scenario:**  
  API gateways often store a rolling window of requests per user to enforce quotas or rate limits. They keep only the most recent N requests, evicting old ones—using a deque or FIFO structure.
- **Trade-off:**  
  - **Coding Problem:** All operations are in-memory and fast.
  - **Real World:** Systems often shard or hash across distributed caches (Redis, Memcached), may use approximate algorithms (leaky bucket, sliding window logs), and must handle distributed consistency.

### 4. **Database Write-Ahead Logs & Caches**
- **Scenario:**  
  In-memory caches (like LRU caches) and write-ahead logs (WALs) maintain a capped buffer of recent entries. When the buffer is full, they evict the oldest data, similar to your router. Deduplication can be crucial in caches (to avoid stale data)—done with sets or hash tables.
- **Trade-off:**  
  - **Coding Problem:** Buffer fits entirely in memory.
  - **Real World:** Large systems spill to disk, use checkpoints, and may deal with partial failures and recovery.

### 5. **Event Stream Processors (Apache Flink, Storm, etc.)**
- **Scenario:**  
  Streaming engines must process and sometimes store a window of recent events for stateful computations or windowed joins. They use memory-capped buffers, deduplicate on event keys/timestamps, and support efficient range queries (for analytics)—just like your getCount.
- **Trade-off:**  
  - **Coding Problem:** Single-threaded, all in-process.
  - **Real World:** Systems must scale horizontally, checkpoint state, handle backpressure, and tolerate node failures.


## Trade-Offs: Coding Problem vs. Real Engineering

**1. Memory Management**  
- *Problem:* Memory is perfectly bounded and managed by Python structures.
- *Reality:* Real systems must handle unbounded input, often relying on paging, disk spill, or distributed memory. Hardware constraints and OS limits also play a role.

**2. Deduplication**
- *Problem:* O(1) set-based deduplication.
- *Reality:* At scale, deduplication across billions of events requires distributed hashes, probabilistic data structures, and tuning for false positives/negatives.

**3. Query Efficiency**
- *Problem:* Fast range queries with bisect; no contention.
- *Reality:* Production systems may index timestamps for fast analytics but must balance write amplification, index maintenance, and multi-tenant access.

**4. Reliability and Concurrency**
- *Problem:* Single-threaded, always available.
- *Reality:* Systems face crashes, network splits, and concurrent access. Engineering solutions include locks, atomic ops, sharding, and recovery protocols.

**5. Latency vs. Throughput**
- *Problem:* All ops are instant.
- *Reality:* Real routers must optimize for latency (for real-time) and throughput (bulk processing), sometimes making tradeoffs between the two.


## Conclusion

The Router class is a microcosm of patterns that are deeply embedded in real-world engineering: bounded buffers, deduplication, FIFO eviction, and efficient querying. Whether you’re designing a hardware router, a distributed message queue, or a streaming analytics engine, the same core ideas apply—though at scale, you must adapt data structures, add fault tolerance, and optimize for distributed environments. Understanding these trade-offs prepares you for the leap from coding interviews to robust, production engineering.


**Visuals that could help:**  
{/*  
- A diagram showing FIFO buffer with evictions and deduplication in a network device.  
- A flowchart of distributed cache or message queue, showing sharding and eviction.  
- An overlay comparing in-memory vs. distributed deduplication.  
*/}

## Knowledge Base Entry: Efficient Memory-Limited Network Packet Router


### 1. Problem Summary

The task is to design a data structure (Router) that efficiently manages data packets in a networked environment, subject to a fixed memory limit. Each packet is uniquely identified by its source, destination, and timestamp. The router must support:
- Efficient insertion of new packets, while evicting the oldest when at capacity (FIFO order).
- Prevention of duplicate packets (same source, destination, timestamp).
- Fast forwarding (removal) of the oldest packet.
- Efficient querying for the number of packets with a specific destination within a timestamp range.


### 2. Algorithmic Pattern Name

- **Sliding Window with Indexed Search**
- Uses a combination of FIFO buffer (queue), hash set for uniqueness, and sorted index per destination for range queries.


### 3. Step-by-Step Reasoning

1. **Initialization**:
   - Maintain a `deque` for FIFO packet storage.
   - Use a `set` for O(1) duplicate detection.
   - Use a `defaultdict(list)` to map each destination to a sorted list of packet timestamps (enabling fast range queries via binary search).

2. **Adding a Packet (`addPacket`)**:
   - Reject the packet if it is a duplicate (already in the set).
   - If at memory limit, evict the oldest packet from the deque, remove from the set, and update the destination's timestamp list.
   - Add the new packet to the deque and set, and insert its timestamp into the destination’s sorted list (using `bisect.insort` for O(log n) insertion).

3. **Forwarding a Packet (`forwardPacket`)**:
   - Remove the oldest packet from the deque and set.
   - Remove the corresponding timestamp from the destination’s sorted list (using `bisect.bisect_left` for O(log n) removal).
   - Return packet details or an empty list if none exist.

4. **Counting Packets (`getCount`)**:
   - For the given destination, use binary search to find the count of timestamps within the provided range (`bisect_left` and `bisect_right`).
   - Return the count difference.


### 4. Big O Complexity

- **addPacket**:  
  - O(1) for set/queue operations
  - O(log n) for sorted list insertion/removal (n = packets per destination)
- **forwardPacket**:  
  - O(1) for set/queue operations
  - O(log n) for sorted list removal
- **getCount**:  
  - O(log n) for each query (binary search on sorted list)

*Amortized complexities assume average-case for set operations and bisect, and n is the number of timestamps for a given destination.*


### 5. Real-World Analogy/Application

**Analogy:**  
Imagine a limited-size conveyor belt (the router) in a warehouse. Each box (packet) must have a unique identifier (source, destination, timestamp). When the belt is full, the oldest box falls off to make space for a new one. Workers (queries) may need to count how many boxes are destined for a specific location within certain time intervals.

**Applications:**  
- Network hardware routers or firewalls preventing duplicate packets and maintaining fast throughput.
- Event processing systems or message brokers with sliding windows and deduplication.
- IoT gateways buffering and filtering sensor data.


### 6. Optimizations or Alternative Approaches

- **Optimize per-destination timestamps:**  
  For destinations with many packets, maintaining a sorted list may become slow. Alternatives include balanced BSTs, skip lists, or segment trees for faster range queries and updates.
- **Batch Eviction:**  
  If frequent evictions occur, batch removals or periodic cleanup can amortize cost.
- **Space Optimization:**  
  Replace tuples with compact struct representations or IDs to save memory.
- **Concurrency:**  
  For multi-threaded environments, use thread-safe data structures or locks.
- **External Storage:**  
  For very large scales, replace in-memory structures with lightweight databases or persistent queues.
- **Alternative Deduplication:**  
  Use Bloom filters for approximate deduplication where strict accuracy is not essential.
- **Time Bucketing:**  
  For high-volume, time-centric queries, bucket timestamps to speed up range counting.

## How Mastering the "Router" Algorithm Accelerates Your Software Engineering Career

Designing and implementing a memory-efficient, duplicate-free, and high-throughput router, like the one above, goes far beyond passing an interview. Mastery of such algorithms maps directly to a wide spectrum of skills crucial at every stage of a software engineering career—from daily development to system architecture and technical leadership.

### 1. Daily Engineering Work: Building Reliable, Efficient Systems

- **Data Structure Fluency:**  
  Implementing this router requires a solid grasp of Python’s `deque`, `set`, `defaultdict`, and `bisect` modules. In day-to-day work, this translates into the ability to select the best data structure for each job—leading to more maintainable, performant code whether you’re handling caching, analytics, queues, or resource management.

- **Edge Case and Error Handling:**  
  The router solution has to handle full buffers, duplicate packets, and empty states gracefully. Developing this mindset helps you build robust components that don’t fail under real-world workloads, a hallmark of a dependable engineer.

### 2. System Design & Architecture: Thinking at Scale

- **Resource Constraints and Scalability:**  
  The router’s memory limit mimics real-world constraints—RAM caps, disk quotas, or throughput ceilings. Learning to design for these boundaries is essential when architecting microservices, distributed systems, or cloud-native platforms.

- **Algorithmic Thinking:**  
  The use of efficient insertions, lookups, evictions, and range queries (via bisect) demonstrates the importance of algorithmic complexity (O(1), O(log N), etc.) in building scalable systems. This thinking is key when designing APIs, databases, or any latency-sensitive component.

- **Statistical and Real-Time Querying:**  
  Supporting fast queries (like `getCount`) over large, changing datasets is core to analytics, monitoring, and operational dashboards. Understanding how to maintain real-time indexes, and how such queries impact system design, is highly transferable.

### 3. Technical Leadership and Mentoring

- **Code Quality and Best Practices:**  
  The solution’s structure—clear method responsibilities, in-sync data structures, and careful mutation—models best practices for clean, maintainable code. As a tech lead or mentor, you’ll guide others in writing such code, reviewing PRs, and enforcing standards.

- **Explaining Design Decisions:**  
  Discussing why a `set` is used for deduplication or why a `deque` is ideal for FIFO buffering is great practice for technical communication. Leaders must justify architectural choices in design docs, code reviews, and cross-team discussions.

- **Scaling Knowledge:**  
  Understanding the trade-offs in the router’s design (e.g., when sorted lists might become a bottleneck) prepares you to evaluate and recommend more advanced solutions (like sharding, LSM-trees, or concurrent data structures) as your team’s needs grow.

### 4. Interviewing and Problem Solving

- **Algorithm Interviews:**  
  This type of problem is common in technical interviews, testing data structure mastery, edge case awareness, and O(N) vs O(log N) reasoning. Being fluent in such designs helps you stand out in interviews and explain your thought process with confidence.

- **Whiteboarding & Prototyping:**  
  The ability to rapidly model a problem, choose the right abstractions, and iterate on solutions is invaluable—whether on a whiteboard, in a design meeting, or while prototyping a new feature.

### 5. Real-World Applications and Technical Breadth

- **Networking & Distributed Systems:**  
  Routers, caches, and message brokers all use variations of this pattern. Mastery helps you understand and troubleshoot production issues in tools like Kafka, Redis, or even cloud load balancers.

- **Cross-Language Skills:**  
  The principles here—efficient FIFO, deduplication, range queries—apply in any language or stack. Mastering them in Python translates to rapid upskilling in Java, Go, or C++ when needed.

#### In Summary

Mastering the router algorithm teaches you much more than how to move packets. It hones your ability to:
- Build robust, high-performance components
- Architect scalable and resource-efficient systems
- Communicate and mentor effectively on complex topics
- Prepare for and excel in technical interviews

These skills are the foundation of engineering growth, from individual contributor all the way to system architect or engineering manager. Tackling such challenges ensures you can deliver value at every level of your software engineering career.
