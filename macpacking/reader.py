from abc import ABC, abstractmethod
from os import path
from random import shuffle, seed
from . import WeightSet, WeightStream

class DatasetReader(ABC):

    def offline(self) -> WeightSet:
        '''Return a WeightSet to support an offline algorithm'''
        (capacity, weights) = self._load_data_from_disk()
        seed(42)          # always produce the same shuffled result
        shuffle(weights)  # side effect shuffling
        return (capacity, weights)

    def online(self) -> WeightStream:
        '''Return a WeighStream, to support an online algorithm'''
        (capacity, weights) = self.offline()

        def iterator():  # Wrapping the contents into an iterator
            for w in weights:
                yield w  # yields the current value and moves to the next one

        return (capacity, iterator())

    @abstractmethod
    def _load_data_from_disk(self) -> WeightSet:
        '''Method that read the data from disk, depending on the file format'''
        pass


class BinppReader(DatasetReader):
    '''Read problem description according to the BinPP format'''

    def __init__(self, filename: str) -> None:
        if not path.exists(filename):
            raise ValueError(f'Unkown file [{filename}]')
        self.__filename = filename

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__filename, 'r') as reader:
            nb_objects: int = int(reader.readline())
            capacity: int = int(reader.readline())
            weights = []
            for _ in range(nb_objects):
                weights.append(int(reader.readline()))
            return (capacity, weights)

class JburkardtReader(DatasetReader):
    '''Read problem description according to the jburkardt format'''

    def __init__(self, pathstart: str) -> None:
        self.__pathstart = pathstart

    def _load_data_from_disk(self) -> WeightSet:
        # Read Capacity 
        with open(self.__pathstart + "_c.txt", 'r') as reader:
            line = reader.readline()
            if '\n' in line:
                line = line[:len(line) - 1]
            if len(line) > 0:
                capacity : int = int(line)

        # Read Weights
        with open(self.__pathstart + "_w.txt", 'r') as reader:
            weights = []
            for line in reader.readlines():
                if '\n' in line:
                    line = line[:len(line)-1]
                if len(line) > 0:
                    weights.append(int(line))

        # Read bin assignment per object
        with open(self.__pathstart + "_s.txt", 'r') as reader:
            assigned_bin = []
            for line in reader.readlines():
                if '\n' in line:
                    line = line[:len(line)-1]
                if len(line) > 0:
                    assigned_bin.append(int(line))
        
        return (capacity, weights)