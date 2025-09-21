from collections import deque, defaultdict
import bisect

class Router(object):

    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.memoryLimit = memoryLimit
        self.packets = deque()  # FIFO queue of packets: (source, destination, timestamp)
        self.packet_set = set()  # To check for duplicates: (source, destination, timestamp)
        # For getCount: destination -> sorted list of timestamps of packets currently in router
        self.dest_to_timestamps = defaultdict(list)

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        key = (source, destination, timestamp)
        if key in self.packet_set:
            return False

        # If at capacity, evict oldest
        if len(self.packets) == self.memoryLimit:
            old_source, old_dest, old_time = self.packets.popleft()
            self.packet_set.remove((old_source, old_dest, old_time))
            # Remove old_time from dest_to_timestamps[old_dest]
            idx = bisect.bisect_left(self.dest_to_timestamps[old_dest], old_time)
            if idx < len(self.dest_to_timestamps[old_dest]) and self.dest_to_timestamps[old_dest][idx] == old_time:
                self.dest_to_timestamps[old_dest].pop(idx)
            if not self.dest_to_timestamps[old_dest]:
                del self.dest_to_timestamps[old_dest]

        self.packets.append((source, destination, timestamp))
        self.packet_set.add(key)
        # Insert timestamp in sorted order for the destination
        bisect.insort(self.dest_to_timestamps[destination], timestamp)
        return True

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if not self.packets:
            return []
        source, destination, timestamp = self.packets.popleft()
        self.packet_set.remove((source, destination, timestamp))
        # Remove timestamp from dest_to_timestamps[destination]
        idx = bisect.bisect_left(self.dest_to_timestamps[destination], timestamp)
        if idx < len(self.dest_to_timestamps[destination]) and self.dest_to_timestamps[destination][idx] == timestamp:
            self.dest_to_timestamps[destination].pop(idx)
        if not self.dest_to_timestamps[destination]:
            del self.dest_to_timestamps[destination]
        return [source, destination, timestamp]

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        # get all timestamps for this destination
        timestamps = self.dest_to_timestamps.get(destination, [])
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        return right - left