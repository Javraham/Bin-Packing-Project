import pyperf
from benchmark import Benchmark

from os import listdir
from os.path import isfile, join, basename
from macpacking.algorithms.online import NextFit, FirstFit, BestFit, WorstFit
from macpacking.reader import JburkardtReader
from macpacking import reader

def main():
    dir = './_datasets/jburkardt/' 
    cases = list_case_files(dir)

    algorithms = [NextFit, BestFit, WorstFit, FirstFit]
    algorithm_names = ["Next Fit", "Best Fit", "Worst Fit", "First Fit"]
    runner = pyperf.Runner()

    i = 0
    for algorithm in algorithms:
        if i <= 4: 
            bench = Benchmark(runner, [str(dir + case) for case in cases], "ONLINE", algorithm, algorithm_names[i], JburkardtReader)
            bench.do_benchmark()
        else:
            bench = Benchmark(runner, [str(dir + case) for case in cases], "OFFLINE", algorithm, algorithm_names[i], JburkardtReader)
            bench.do_benchmark()
        i += 1

def list_case_files(dir: str) -> list[str]:
    return sorted(["p0" + str(i) for i in range(1, int(len(listdir(dir))/3) + 1)])

if __name__ == "__main__":
    main()