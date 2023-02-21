import pyperf
from benchmark import Benchmark

from os import listdir
from os.path import isfile, join, basename
from macpacking.algorithms.online import NextFit as NFOnline, BestFit as BFOnline, WorstFit as WFOnline, FirstFit as FFOnline, RefinedFirstFit as RFOnline
from macpacking.algorithms.offline import NextFit as NFOffline, BestFitDecreasing as BFOffline, WorstFitDecreasing as WFOffline, FirstFitDecreasing as FFOffline


from macpacking.reader import BinppReader
from macpacking import reader

def main2():
    dir = './_datasets/binpp/N4C2W2'
    cases = list_case_files(dir)

    algorithms = [NFOnline, BFOnline, WFOnline, FFOnline, RFOnline, NFOffline, BFOffline, WFOffline, FFOffline]
    algorithm_names = ["Next Fit Online", "Best Fit Online", "Worst Fit Online", "First Fit Online", "Refined First Fit Online", "Next Fit Offline", "Best Fit Offline", "Worst Fit Offline", "First Fit Offline"]
    runner = pyperf.Runner()

    i = 0
    for algorithm in algorithms:
        if i <= 4: 
            bench = Benchmark(runner, cases, "ONLINE", algorithm, algorithm_names[i], BinppReader)
            bench.do_benchmark()
        else:
            bench = Benchmark(runner, cases, "OFFLINE", algorithm, algorithm_names[i], BinppReader)
            bench.do_benchmark()
        i += 1

def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])

def main():
    dir = './_datasets/binpp/N4C2W2'
    cases = list_case_files(dir)

    algorithms = [NFOnline, FFOnline, BFOnline, WFOnline,  RFOnline, NFOffline, FFOffline, BFOffline, WFOffline]
    algorithm_names = ["Next Fit Online", "First Fit Online", "Best Fit Online", "Worst Fit Online", "Refined First Fit Online", "Next Fit Offline", "First Fit Offline", "Best Fit Offline", "Worst Fit Offline"]
    runner = pyperf.Runner()

    i = 0
    for algorithm in algorithms:
        if i <= 4: 
            bench = Benchmark(runner, cases, "ONLINE", algorithm, algorithm_names[i], BinppReader)
            bench.do_benchmark()
        else:
            bench = Benchmark(runner, cases, "OFFLINE", algorithm, algorithm_names[i], BinppReader)
            bench.do_benchmark()
        i += 1

def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])

if __name__ == "__main__":
    main()