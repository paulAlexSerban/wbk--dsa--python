import unittest
from router import Router

class TestRouter(unittest.TestCase):
    def setUp(self):
        self.router = Router(3)  # Memory limit of 3 packets

    def test_add_packet(self):
        self.assertTrue(self.router.addPacket(1, 2, 100))
        self.assertTrue(self.router.addPacket(2, 3, 200))
        self.assertTrue(self.router.addPacket(3, 4, 300))
        # Adding a duplicate packet
        self.assertFalse(self.router.addPacket(1, 2, 100))
        # Adding a new packet when at capacity should evict the oldest
        self.assertTrue(self.router.addPacket(4, 5, 400))
        # The oldest packet (1,2,100) should be evicted
        self.assertTrue(self.router.addPacket(5, 6, 500))   # Evicts (2,3,200)

    def test_forward_packet(self):
        self.router.addPacket(1, 2, 100)
        self.router.addPacket(2, 3, 200)
        self.router.addPacket(3, 4, 300)
        self.assertEqual(self.router.forwardPacket(), [1, 2, 100])
        self.assertEqual(self.router.forwardPacket(), [2, 3, 200])
        self.assertEqual(self.router.forwardPacket(), [3, 4, 300])
        self.assertEqual(self.router.forwardPacket(), [])  # No packets left

    def test_get_count(self):
        self.router.addPacket(1, 2, 100)
        self.router.addPacket(2, 2, 150)
        self.router.addPacket(3, 3, 200)
        self.assertEqual(self.router.getCount(2, 50, 200), 2)   # Two packets to dest=2 in range
        self.assertEqual(self.router.getCount(2, 100, 150), 2)   # Both packets to dest=2 in range
        self.assertEqual(self.router.getCount(2, 151, 200), 0)   # No packets to dest=2 in range
        self.assertEqual(self.router.getCount(3, 100, 250), 1)   # One packet to dest=3 in range
        self.assertEqual(self.router.getCount(4, 100, 250), 0)   # No packets to dest=4 in range

    def test_problems_case_example_one(self):
        self.assertTrue(self.router.addPacket(1, 4, 90))   # true
        self.assertTrue(self.router.addPacket(2, 5, 90))   # true
        self.assertFalse(self.router.addPacket(1, 4, 90))  # false (duplicate)
        self.assertTrue(self.router.addPacket(3, 5, 95))   # true
        self.assertTrue(self.router.addPacket(4, 5, 105))  # true (evicts (1,4,90))
        self.assertEqual(self.router.forwardPacket(), [2, 5, 90])  # [2, 5, 90]
        self.assertTrue(self.router.addPacket(5, 2, 110))   # true
        self.assertEqual(self.router.getCount(5, 100, 110), 1)  # 1 (only (4,5,105) in range)

    def test_problems_case_example_two(self):
        router2 = Router(2)
        self.assertTrue(router2.addPacket(7, 4, 90))   # true
        self.assertEqual(router2.forwardPacket(), [7, 4, 90])  # [7, 4, 90]
        self.assertEqual(router2.forwardPacket(), [])  # []