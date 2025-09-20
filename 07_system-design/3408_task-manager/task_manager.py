import heapq

class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        # Heap: stores (-priority, -taskId, taskId)
        self.heap = []
        # Maps: taskId -> (userId, priority)
        self.task = {}
        for userId, taskId, priority in tasks:
            self.task[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        self.task[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        userId, _ = self.task[taskId]
        self.task[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        if taskId in self.task:
            del self.task[taskId]

    def execTop(self):
        """
        :rtype: int
        """
        while self.heap:
            neg_priority, neg_taskId, taskId = heapq.heappop(self.heap)
            if taskId in self.task and self.task[taskId][1] == -neg_priority:
                userId, _ = self.task[taskId]
                del self.task[taskId]
                return userId
        return -1