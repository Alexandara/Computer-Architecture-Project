import subprocess
import shlex
import cpi
import CPI_Read_In
import csv
import os

import time

def cost(cpi):
    return 1

def evaluate(i):
    i.value = i.cpi * i.cost
    return i

def minimum(list):
    min = 1000000000000000000
    best = None
    for i in list:
        if i.value < min:
            min = i.value
            best = i
    return best


def optimize(benchmark, init=None, min=CPI_Read_In.CPIData("", "", 0)):
    #l1d_assoc=0, l1i_assoc=0, l2_assoc=0, size=0, l1d_size=0, l1i_size=0
    if init is None:
        init = [3,3,4,4,3]
    projectlocation = "/people/cs/a/art150530/Project1_SPEC"
    l1d_size_options = ["16kB", "32kB", "64kB", "128kB"]
    l1i_size_options = ["16kB", "32kB", "64kB", "128kB"]
    l1d_assoc_options = ["1","2","4","8","16"]
    l1i_assoc_options = ["1","2","4","8","16"]
    size_options = ["8", "16", "32", "64"]
    commandtext = "/usr/local/gem5/build/X86/gem5.opt " \
                  "-d /people/cs/a/art150530/m5out /usr/local/gem5/configs/example/se.py " \
                  "-I 100000000 " \
                  "-c ./src/benchmark " \
                  "-o " + benchmark[1] +" " \
                  "--cpu-type=atomic " \
                  "--caches --l2cache " \
                  "--l1d_size=" + l1d_size_options[init[0]] + " " \
                  "--l1i_size=" + l1i_size_options[init[1]] + " " \
                  "--l2_size=1MB " \
                  "--l1d_assoc=" + l1d_assoc_options[init[2]] + " " \
                  "--l1i_assoc=" + l1i_assoc_options[init[3]] + " " \
                  "--l2_assoc=1 " \
                  "--cacheline_size=" + size_options[init[4]]
    location = projectlocation + "/" + benchmark[0]
    p = subprocess.Popen(commandtext,shell=True,cwd=location)
    p.wait()
    # path = Path(location)
    while not os.path.exists('/people/cs/a/art150530/m5out/stats.txt'):
        # Bad practice
        time.sleep(10)
    while os.path.getsize('/people/cs/a/art150530/m5out/stats.txt') == 0:
        # Still bad practice
        time.sleep(10)
    cpival = cpi.calculatecpisingle("/people/cs/a/art150530/m5out/stats.txt")
    costval = cost(cpival)
    cpiData = CPI_Read_In.CPIData("Unknown", "NA", cpival,
                                    l1d_assoc=l1d_assoc_options[init[2]], l1i_assoc=l1i_assoc_options[init[3]],
                                    l2_assoc="1MB",
                                    size=size_options[init[4]], l1d_size=l1d_size_options[init[0]],
                                    l1i_size=l1i_size_options[init[1]], cost=costval)
    evaluate(cpiData)
    newinit = []
    for val in init:
        if val == 0:
            newinit.append(0)
        else:
            newinit.append(val-1)
    if cpiData.value > min.value:
        return min
    elif init == [0,0,0,0,0]:
        return cpiData
    else:
        return minimum([optimize(benchmark, init=[newinit[0],newinit[1],newinit[2],newinit[3],newinit[4]], min=cpiData),
                        optimize(benchmark, init=[newinit[0],newinit[1],newinit[2],newinit[3],newinit[4]], min=cpiData),
                        optimize(benchmark, init=[newinit[0],newinit[1],newinit[2],newinit[3],newinit[4]], min=cpiData),
                        optimize(benchmark, init=[newinit[0],newinit[1],newinit[2],newinit[3],newinit[4]], min=cpiData),
                        optimize(benchmark, init=[newinit[0],newinit[1],newinit[2],newinit[3],newinit[4]], min=cpiData)])


benchmark_data_options = [["401.bzip2","./data/input.program"],
                              ["429.mcf","./data/inp.in"],
                              ["456.hmmer", "./data/bombesin.hmm.new"],
                              ["458.sjeng", "./data/test.txt"],
                              ["470.lbm", "./data/lbm.in"]]
for benchmark in benchmark_data_options:
    cpithing = optimize(benchmark)
    if benchmark[0] == "401.bzip2":
        min401 = cpithing
    elif benchmark[0] == "429.mcf":
        min429 = cpithing
    elif benchmark[0] == "456.hmmer":
        min456 = cpithing
    elif benchmark[0] == "458.sjeng":
        min458 = cpithing
    elif benchmark[0] == "470.lbm":
        min470 = cpithing
with open('../data/optimization.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Benchmark", "Experiment", "CPI", "Data Associativity", "Instruction Associativity",
            "L2 Associativity", "Block Size", "Data Size", "Instruction Size", "Cost"])
    writer.writerow(min401.toArray())
    writer.writerow(min429.toArray())
    writer.writerow(min456.toArray())
    writer.writerow(min458.toArray())
    writer.writerow(min470.toArray())
