from compare_version_numbers import VersionComparator
from unittest import TestCase

class TestVersionComparator(TestCase):
    def setUp(self):
        self.comparator = VersionComparator()

    def test_compare_versions(self):
        self.assertEqual(self.comparator.compareVersion("1.0", "1"), 0)
        self.assertEqual(self.comparator.compareVersion("1.0.1", "1"), 1)
        self.assertEqual(self.comparator.compareVersion("1", "1.0.1"), -1)

    def test_leading_zeros(self):
        self.assertEqual(self.comparator.compareVersion("1.01", "1.001"), 0)
        self.assertEqual(self.comparator.compareVersion("1.0", "1.0.0"), 0)
        self.assertEqual(self.comparator.compareVersion("1.0.0", "1.0"), 0)

    def test_different_lengths(self):
        self.assertEqual(self.comparator.compareVersion("1.0", "1.0.0.0"), 0)
        self.assertEqual(self.comparator.compareVersion("1.0.0", "1.0"), 0) 
        self.assertEqual(self.comparator.compareVersion("1.0.1", "1.0.0"), 1)
        self.assertEqual(self.comparator.compareVersion("1.0.0", "1.0.1"), -1)
        self.assertEqual(self.comparator.compareVersion("1.2", "1.10"), -1)
        self.assertEqual(self.comparator.compareVersion("1.10", "1.2"), 1)