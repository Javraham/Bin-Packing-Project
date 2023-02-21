from macpacking.algorithms.online import NextFit as NFOnline, BestFit, WorstFit, FirstFit, RefinedFirstFit
from macpacking.algorithms.offline import NextFit as NFOffline, BestFitDecreasing, WorstFitDecreasing, FirstFitDecreasing

def test_next_fit_online():

    test_capacity = 10
    test_weights = iter([1,2,3,4,5,6])
    assert NFOnline()._process(test_capacity, test_weights) == [[1,2,3,4],[5],[6]]

def test_first_fit_online():
    test_capacity = 10
    test_weights = iter([3, 8, 4, 2, 2, 1])

    assert FirstFit()._process(test_capacity, test_weights) == [[3, 4, 2, 1],[8, 2]]

def test_best_fit_online():
    test_capacity = 10
    test_weights = iter([5, 6, 3, 7, 2, 4, 1])

    assert BestFit()._process(test_capacity, test_weights) == [[5, 4, 1],[6, 3], [7, 2]]

def test_worst_fit_online():
    test_capacity = 10
    test_weights = iter([5, 6, 3, 7, 2, 4, 1])

    assert WorstFit()._process(test_capacity, test_weights) == [[5, 3],[6, 2], [7], [4, 1]]

def test_refined_first_fit_online():
    test_capacity = 10
    test_weights = iter([5, 6, 3, 7, 2, 4, 1, 3, 4])
    assert RefinedFirstFit()._process(test_capacity, test_weights) == [[5], [6], [3, 2, 1, 3], [7], [4, 4]]

def test_next_fit_offline():
    test_capacity = 10
    test_weights = iter([1, 4, 5, 2, 3, 6])

    assert NFOffline()._process(test_capacity, test_weights) == [[6],[5, 4], [3, 2, 1]]

def test_first_fit_offline():
    test_capacity = 10
    test_weights = iter([1, 4, 5, 2, 3, 6])

    assert FirstFitDecreasing()._process(test_capacity, test_weights) == [[6, 4],[5, 3, 2], [1]]

def test_best_fit_offline():
    test_capacity = 10
    test_weights = iter([3, 6, 1, 7, 5, 2, 2])

    assert BestFitDecreasing()._process(test_capacity, test_weights) == [[7, 3],[6, 2, 2], [5, 1]]

def test_worst_fit_offline():
    test_capacity = 10
    test_weights = iter([3, 6, 1, 7, 5, 2, 2])

    assert WorstFitDecreasing()._process(test_capacity, test_weights) == [[7, 2],[6, 2, 1], [5, 3]]

test_next_fit_online()
test_first_fit_online()
test_best_fit_online()
test_worst_fit_online()
test_next_fit_offline()
test_first_fit_offline()
test_best_fit_offline()
test_worst_fit_offline()
test_refined_first_fit_online()
print("All Tests Passed")
