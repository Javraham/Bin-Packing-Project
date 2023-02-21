from os import listdir
from os.path import isfile, join, basename
from macpacking.algorithms.online import NextFit as NFOnline, BestFit as BFOnline, WorstFit as WFOnline, FirstFit as FFOnline, RefinedFirstFit as RFOnline
from macpacking.algorithms.offline import NextFit as NFOffline, BestFitDecreasing as BFOffline, WorstFitDecreasing as WFOffline, FirstFitDecreasing as FFOffline

from macpacking.reader import BinppReader
import matplotlib.pyplot as plot

def main():
    reader = BinppReader

    HARDBPP_CASES = './_datasets/binpp-hard'

    cases = list_case_files(HARDBPP_CASES)

    solutions = list()
    num_bins = list()
    for case in cases:
        data = reader(case).online()
        weights = (list(data[1]))
        capacity = data[0]

        num_bins.append(len(NFOnline()._process(capacity, weights)))
        num_bins.append(len(BFOnline()._process(capacity, weights)))
        num_bins.append(len(WFOnline()._process(capacity, weights)))
        num_bins.append(len(FFOnline()._process(capacity, weights)))
        num_bins.append(len(RFOnline()._process(capacity, weights)))

        data = reader(case).offline()
        weights = (list(data[1]))
        capacity = data[0]      

        num_bins.append(len(NFOffline()._process(capacity, weights)))
        num_bins.append(len(BFOffline()._process(capacity, weights)))
        num_bins.append(len(WFOffline()._process(capacity, weights)))
        num_bins.append(len(FFOffline()._process(capacity, weights)))

        solutions.append((basename(case), min(num_bins)))
        num_bins = list()

    tested_optimal = [solutions[i][1] for i in range(10)]
    oracle_optimal = [56, 57, 56, 55, 57, 56, 57, 55, 57, 56]
    diffs = list()
    for i in range(len(tested_optimal)):
        diffs.append(("HARD" + str(i), "Difference: " + str(tested_optimal[i]-oracle_optimal[i])))

    for diff in diffs:
        print(diff)

    GraphResults(oracle_optimal, tested_optimal)

def GraphResults(optimal, tested):
    plot.scatter(["HARD"+str(i)+".BPP" for i in range(10)], tested, color='blue', label="Tested Number  of Bins")
    plot.scatter(["HARD"+str(i)+".BPP" for i in range(10)], optimal, color='green', label = "Optimal Number of Bins")
    plot.legend(loc="upper right")

    for i,txt in enumerate(optimal):
        plot.annotate(txt, (i, optimal[i]))

    for i,txt in enumerate(tested):
        plot.annotate(txt, (i, tested[i]))

    plot.xticks(range(10))
    plot.yticks(range(40,70,2))

    plot.xlabel('File Name')
    plot.ylabel('Number of Bins')

    plot.xticks(rotation = 45)

    plot.grid('both')
    plot.show()

def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])

if __name__ == "__main__":
    main()