from .. import Solution, WeightSet
from ..model import Offline
from .online import NextFit as Nf_online, FirstFit as Ff_online, BestFit as Bf_online, WorstFit as Wf_online


class NextFit(Offline):

    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        '''An offline version of NextFit, ordering the weigh stream and
        delegating to the online version (avoiding code duplication)'''
        weights = sorted(weights, reverse=True)
        delegation = Nf_online()
        return delegation((capacity, weights))

class FirstFitDecreasing(Offline):
    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = Ff_online()
        return delegation((capacity, weights))

class BestFitDecreasing(Offline):
    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = Bf_online()
        return delegation((capacity, weights))

class WorstFitDecreasing(Offline):
    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = Wf_online()
        return delegation((capacity, weights))

