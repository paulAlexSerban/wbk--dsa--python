# Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.
- You must implement a solution with O(1) time complexity for each function.

 

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:
- -231 <= val <= 231 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 104 calls will be made to push, pop, top, and getMin.

# Practical Applications
1. **Data Structures**: Min stacks are useful in scenarios where you need to keep track of the minimum value in a collection of elements, such as in priority queues or heaps.
2. **Algorithm Optimization**: They can be used to optimize algorithms that require frequent retrieval of the minimum element, such as in graph algorithms or dynamic programming problems.
3. **Memory Management**: In systems where memory allocation and deallocation are frequent, a min stack can help manage the minimum memory usage efficiently
4. **Game Development**: In games, min stacks can be used to track the minimum score or health of a player, allowing for quick access to the lowest value during gameplay.
5. **Financial Applications**: In financial applications, min stacks can be used to track the minimum stock price or investment value over time, enabling quick decision-making based on historical data.
6. **Data Analysis**: Min stacks can be used in data analysis tasks where you need to find the minimum value in a dataset efficiently, such as in statistical analysis or machine learning preprocessing.
7. **Real-time Systems**: In real-time systems, min stacks can help maintain the minimum value of a stream of data, such as sensor readings or user inputs, allowing for quick responses to changes in the data.
8. **Web Development**: In web applications, min stacks can be used to manage user inputs or form validations, ensuring that the minimum value entered by a user is tracked and validated efficiently.
9. **Database Management**: Min stacks can be used in database systems to efficiently retrieve the minimum value from a set of records, such as in query optimization or indexing.
10. **Machine Learning**: In machine learning, min stacks can be used to track the minimum loss or error during model training, allowing for quick adjustments to the model parameters based on the minimum performance observed.