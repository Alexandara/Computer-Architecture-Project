import subprocess
import shlex
import cpi
import CPI_Read_In
import csv
#from pathlib import Path
import os
import os.path
import time

def cost(cpi):
    return 1

def evaluate(list):
    minimum = 10000000000
    best = ""
    for i in list:
        tot = i.cpi * i.cost
        if tot < minimum:
            minimum = tot
            best = i
    return best

def optimize(projectlocation):
    #l1d_assoc=0, l1i_assoc=0, l2_assoc=0, size=0, l1d_size=0, l1i_size=0
    l1d_assoc_options = ["1"]#,"2","4","8","16"]
    l1i_assoc_options = ["1"]#,"2","4","8","16"]
    size_options = ["8"]#, "16", "32", "64"]
    l1d_size_options = ["16kB"]#, "32kB", "64kB", "128kB"]
    l1i_size_options = ["16kB"]#, "32kB", "64kB", "128kB"]
    benchmark_data_options = [["401.bzip2","./data/input.program"],
                              ["429.mcf","./data/inp.in"],
                              ["456.hmmer", "./data/bombesin.hmm.new"],
                              ["458.sjeng", "./data/test.txt"],
                              ["470.lbm", "./data/lbm.in"]]
    min401 = []
    min429 = []
    min456 = []
    min458 = []
    min470 = []
    for benchmark in benchmark_data_options:
        for l1d_assoc in l1d_assoc_options:
            for l1i_assoc in l1i_assoc_options:
                for size in size_options:
                    for l1d_size in l1d_size_options:
                        for l1i_size in l1i_size_options:
                            commandtext = "/usr/local/gem5/build/X86/gem5.opt " \
                                          "-d ~/m5out /usr/local/gem5/configs/example/se.py " \
                                          "-I 100000000 " \
                                          "-c ./src/benchmark " \
                                          "-o " + benchmark[1] +" " \
                                          "--cpu-type=atomic " \
                                          "--caches --l2cache " \
                                          "--l1d_size=" + l1d_size + " " \
                                          "--l1i_size=" + l1i_size + " " \
                                          "--l2_size=1MB " \
                                          "--l1d_assoc=" + l1d_assoc + " " \
                                          "--l1i_assoc=" + l1i_assoc + " " \
                                          "--l2_assoc=1 " \
                                          "--cacheline_size=" + size
                            location = projectlocation + "/" + benchmark[0] + "/"
                            command = shlex.split(commandtext)
                            print(commandtext)
			    p = subprocess.Popen(commandtext, shell=True,cwd=location)
			    p.wait()
			    #path = Path(location)
			    while not os.path.exists('~/m5out/stats.txt'):
			    	# Bad practice
				time.sleep(10)
			    while os.path.getsize('~/m5out/stats.txt') == 0:
			    	# Still bad practice
				time.sleep(10)
			    print("Post Command")
                            cpival = cpi.calculatecpisingle("~/m5out/stats.txt")
                            costval = cost(cpival)
			    os.remove(location)
                            if benchmark[0] == "401.bzip2":
                                min401.append(CPI_Read_In.CPIData(benchmark[0], "NA", cpival,
                                                                  l1d_assoc=l1d_assoc, l1i_assoc=l1i_assoc, l2_assoc="1MB",
                                                                  size=size, l1d_size=l1d_size, l1i_size=l1i_size, cost=costval))
                            elif benchmark[0] == "429.mcf":
                                min429.append(CPI_Read_In.CPIData(benchmark[0], "NA", cpival,
                                                                  l1d_assoc=l1d_assoc, l1i_assoc=l1i_assoc, l2_assoc="1MB",
                                                                  size=size, l1d_size=l1d_size, l1i_size=l1i_size, cost=costval))
                            elif benchmark[0] == "456.hmmer":
                                min456.append(CPI_Read_In.CPIData(benchmark[0], "NA", cpival,
                                                                  l1d_assoc=l1d_assoc, l1i_assoc=l1i_assoc, l2_assoc="1MB",
                                                                  size=size, l1d_size=l1d_size, l1i_size=l1i_size, cost=costval))
                            elif benchmark[0] == "458.sjeng":
                                min458.append(CPI_Read_In.CPIData(benchmark[0], "NA", cpival,
                                                                  l1d_assoc=l1d_assoc, l1i_assoc=l1i_assoc, l2_assoc="1MB",
                                                                  size=size, l1d_size=l1d_size, l1i_size=l1i_size, cost=costval))
                            elif benchmark[0] == "470.lbm":
                                min470.append(CPI_Read_In.CPIData(benchmark[0], "NA", cpival,
                                                                  l1d_assoc=l1d_assoc, l1i_assoc=l1i_assoc, l2_assoc="1MB",
                                                                  size=size, l1d_size=l1d_size, l1i_size=l1i_size, cost=costval))
    with open('../data/optimization.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Benchmark", "Experiment", "CPI", "Data Associativity", "Instruction Associativity",
                "L2 Associativity", "Block Size", "Data Size", "Instruction Size", "Cost"])
        best = evaluate(min401)
        writer.writerow(best.toArray())
        best = evaluate(min429)
        writer.writerow(best.toArray())
        best = evaluate(min456)
        writer.writerow(best.toArray())
        best = evaluate(min458)
        writer.writerow(best.toArray())
        best = evaluate(min470)
        writer.writerow(best.toArray())



optimize("/people/cs/a/art150530/Project1_SPEC")
