from two_sum import two_sum


class TestSumTwo:
    def test_two_sum_example_1(self):
        assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    def test_two_sum_example_2(self):
        assert two_sum([3, 2, 4], 6) == [1, 2]

    def test_two_sum_example_3(self):
        assert two_sum([3, 3], 6) == [0, 1]

    def test_two_sum_no_solution(self):
        assert not two_sum([1, 2, 3], 7)

    def test_two_sum_empty_list(self):
        assert not two_sum([], 5)

    def test_two_sum_single_element(self):
        assert not two_sum([1], 1)
