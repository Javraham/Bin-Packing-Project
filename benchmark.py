import pyperf
from os import listdir
from os.path import isfile, join, basename
from macpacking.algorithms.online import NextFit as NFOnline, BestFit as BFOnline, WorstFit as WFOnline, FirstFit as FFOnline, RefinedFirstFit as RFOnline
from macpacking.algorithms.offline import NextFit as NFOffline, BestFitDecreasing as BFOffline, WorstFitDecreasing as WFOffline, FirstFitDecreasing as FFOffline
from macpacking.reader import BinppReader

HARDBPP_CASES = './_datasets/binpp-hard'
BPP_CASES = './_datasets/binpp/N2C3W2'
JBURKARDT_CASES = './_datasets/jburkardt' 

def main():   
    runner = pyperf.Runner()
    cases = list_case_files(HARDBPP_CASES)
    algorithms = [NFOnline, BFOnline, WFOnline, FFOnline, RFOnline, NFOffline, BFOffline, WFOffline, FFOffline]
    algorithm_names = ["Next Fit Online", "Best Fit Online", "Worst Fit Online", "First Fit Online", "Refined First Fit Online", "Next Fit Offline", "Best Fit Offline", "Worst Fit Offline", "First Fit Offline"]
    
    i = 0
    for algorithm in algorithms:
        bench = Benchmark(runner, cases, type, algorithm, algorithm_names[i])
        bench.do_benchmark()
        i += 1

def list_case_files(dir: str) -> list[str]:
    return sorted([dir + "/HARD" + str(f) + ".BPP.txt" for f in range(1) if isfile(join(dir, listdir(dir)[f]))])

class Benchmark:
    def __init__(self, runner, cases, type, algorithm, algorithm_name, reader):
        self.runner = runner
        self.cases = cases
        self.type = type
        self.algorithm = algorithm
        self.algorithm_name = algorithm_name
        self.reader = reader

    def do_benchmark(self):
        for case in self.cases:
            name = self.algorithm_name + " - " + self.type + " - " + basename(case)

            if self.type == "ONLINE":
                data = self.reader(case).online()
            elif self.type == "OFFLINE":
                data = self.reader(case).offline()
            
            self.runner.bench_func(name, self.algorithm(), data)

if __name__ == "__main__":
    main()