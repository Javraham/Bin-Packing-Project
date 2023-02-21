from .. import Solution, WeightStream
from ..model import Online


class NextFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bin_index = 0
        solution = [[]]
        remaining = capacity
        for w in stream:
            if remaining >= w:
                solution[bin_index].append(w)
                remaining = remaining - w
            else:
                bin_index += 1
                solution.append([w])
                remaining = capacity - w
        return solution

class TerribleFit(Online):

    def _process(self, stream: WeightStream) -> Solution:
        solution = []
        for w in stream:
            solution.append([w])
        return solution

class BestFit(Online):
    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        num_bins = 0
        rem_space = []
        solution = []

        for w in stream:
            min = capacity + 1
            bin_index = 0

            for j in range(num_bins):
                if rem_space[j] >= w and rem_space[j] - w < min:
                    bin_index = j
                    min = rem_space[j] - w
        
            if min == capacity + 1:
                rem_space.append(capacity - w)
                num_bins += 1
                solution.append([w])
            else:
                rem_space[bin_index] -= w
                solution[bin_index].append(w)
        
        return solution

class WorstFit(Online):
    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        num_bins = 0
        rem_space = []
        solution = []

        for w in stream:

            maxspace, worstI = -1,0

            for j in range(num_bins):
                if (rem_space[j] >= w and rem_space[j] - w > maxspace):
                    worstI = j
                    maxspace = rem_space[j] - w
        
            if (maxspace == -1):
                rem_space.append(capacity - w)
                num_bins += 1
                solution.append([w])
         
            else: 
                rem_space[worstI] -= w
                solution[worstI].append(w)
        
        return solution
        

class FirstFit(Online):
    
    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        numBins = 0
        solution=[]
        rem_space = []
        for w in stream:
            j = 0
            while j < len(rem_space):
                if rem_space[j] >= w:
                    rem_space[j] -= w
                    solution[j].append(w)
                    break 
                j += 1

            if j == numBins:
                solution.append([w])
                rem_space.append(capacity-w)
                numBins += 1
                    
        return solution

class Bin:
    def __init__(self, capacity, classification):
        self.classification = classification
        self.remaining_space = capacity
        self.objects = list()

    def GetRemainingSpace(self):
         return self.remaining_space

    def GetObjects(self):
        return self.objects

    def GetWeightsInBin(self):
        weights = list()
        for object in self.objects:
            weights.append(object.GetWeight())

        return weights

    def GetClass(self):
        return self.classification

    def AddObject(self, object):
        self.objects.append(object)
        self.remaining_space -= object.GetWeight()

    def Display(self):
        for object in self.objects:
            print("Weight: ", object.GetWeight(), "Class: ", object.GetClassification())

class Object:
    def __init__(self, weight, classification):
        self.weight = weight
        self.classification = classification

    def SetClass(self, classification):
        self.classification = classification

    def GetWeight(self):
        return self.weight

    def GetClass(self):
        return self.classification
    
class RefinedFirstFit(Online):
        def _process(self, capacity: int, stream: WeightStream) -> Solution:

            def GetClass(capacity, w):
                if w > capacity/2 and w <= capacity:       #(5,10]
                    return 'A'
                elif w > 2*capacity/5 and w <= capacity/2: #(4,5]
                    return 'B1'
                elif w > capacity/3 and w <= 2*capacity/5: 
                    return 'B2'
                else:                                             
                    return 'X'

            def MapClass(classification):
                if classification == 'A':
                    return 1
                elif classification == 'B1':
                    return 2
                elif classification == 'X':
                    return 4

            bins = list()
            objects = list()
            solution = list()
            b2_objects = list()

            for w in stream:
                objects.append(Object(w, GetClass(capacity, w)))
                if objects[-1].GetClass() == 'B2':
                    b2_objects.append(objects[-1])
                
                j = 0

                while j < len(bins):
                    if objects[-1].GetClass() == 'B2':
                        if len(b2_objects) % 6 == 0 or len(b2_objects) % 7 == 0 or len(b2_objects) % 8 == 0 or len(b2_objects) % 9 == 0:
                            if bins[j].GetRemainingSpace() >= objects[-1].GetWeight() and bins[j].GetClass() == 1:
                                bins[j].AddObject(objects[-1])
                                break
                        else:
                            if bins[j].GetRemainingSpace() >= objects[-1].GetWeight() and bins[j].GetClass() == 3:
                                bins[j].AddObject(objects[-1])
                                break
                    else:
                        if bins[j].GetRemainingSpace() >= objects[-1].GetWeight() and bins[j].GetClass() == MapClass(objects[-1].GetClass()):
                                bins[j].AddObject(objects[-1])
                                break
                    j += 1
                
                if j == len(bins):
                    if(objects[-1].GetClass() == 'B2'):
                        if (len(b2_objects) % 6 == 0 or len(b2_objects) % 7 == 0 or len(b2_objects) % 8 == 0 or len(b2_objects) % 9 == 0):
                            bins.append(Bin(capacity, 1))    
                        else:
                            bins.append(Bin(capacity, 3))                    
                    else:
                        bins.append(Bin(capacity, MapClass(objects[-1].GetClass())))
                    
                    bins[j].AddObject(objects[-1])

            for bin in bins:
                solution.append(bin.GetWeightsInBin())

            return solution