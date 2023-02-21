import pyperf
import matplotlib.pyplot as plot
import numpy as np

class Grapher:
    def plot_histogram(self, bench_JSON_path, title):
        bench = pyperf.Benchmark.load(bench_JSON_path)

        runs = bench.get_runs()
    
        values = []
        for run in runs:
            run_values = run.values
            
            values.extend(run_values)
        
        print(values)
        counts, bins = np.histogram(values)
        plot.title(title)
        plot.xlabel('Execution Time')
        plot.ylabel('Frequency')
        plot.hist(bins[:-1], bins, weights=counts, color='blue')
        plot.stairs(counts, bins, color = 'black')
        
        plot.show()

def graphBenchmark(algorithm : str, filename : str, bench_JSON_path):
    grapher = Grapher()
    grapher.plot_histogram(bench_JSON_path, algorithm + " for " + filename)
    
graphBenchmark("Execution time of Online Next Fit", "N4C2W2_A.BPP", r'benchmarking\results\sample_files\NextFitOnline_N4C2W2_A.BPP.json')
graphBenchmark("Execution time of Online First Fit", "N4C2W2_A.BPP", r'benchmarking\results\sample_files\FirstFitOnline_N4C2W2_A.BPP.json')
graphBenchmark("Execution time of Online Best Fit", "N4C2W2_A.BPP", r'benchmarking\results\sample_files\BestFitOnline_N4C2W2_A.BPP.json')
graphBenchmark("Execution time of Online Worst Fit", "N4C2W2_A.BPP", r'benchmarking\results\sample_files\WorstFitOnline_N4C2W2_A.BPP.json')
graphBenchmark("Execution time of Refined First Fit Online", "N4C2W2_A.BPP", r'benchmarking\results\sample_files\RefFirstFitOnline_N4C2W2_A.BPP.json')

graphBenchmark("Execution time of Offline Next Fit", "N4C2W2_A.BPP", r'benchmarking\results\sample_files\NextFitOffline_N4C2W2_A.BPP.json')
graphBenchmark("Execution time of Offline First Fit", "N4C2W2_A.BPP", r'benchmarking\results\sample_files\FirstFitOffline_N4C2W2_A.BPP.json')
graphBenchmark("Execution time of Offline Best Fit", "N4C2W2_A.BPP", r'benchmarking\results\sample_files\BestFitOffline_N4C2W2_A.BPP.json')
graphBenchmark("Execution time of Offline Worst Fit", "N4C2W2_A.BPP", r'benchmarking\results\sample_files\WorstFitOffline_N4C2W2_A.BPP.json')

