import subprocess
import cpi
import CPI_Read_In
import csv
import os

import time

def cost(cpival):
    # cost per KB
    # cost per association
    cost_weight = {
        "l1d_size_cost": .75,
        "l1i_size_cost": .75,
        "l2_size_cost": .25,
        "l1d_assoc_cost": 5,
        "l1i_assoc_cost": 5,
        "l2_assoc_cost": 8,
        "cacheline_size_cost": .8,
    }

    l1d_size_cost_total         = cost_weight["l1d_size_cost"]          * cpival.l1d_size
    l1i_size_cost_total         = cost_weight["l1i_size_cost"]          * cpival.l1i_size
    l2_size_cost_total          = cost_weight["l2_size_cost"]           * 1000 
    l1d_assoc_cost_total        = cost_weight["l1d_assoc_cost"]         * cpival.l1d_assoc
    l1i_assoc_cost_total        = cost_weight["l1i_assoc_cost"]         * cpival.l1i_assoc
    l2_assoc_cost_total         = cost_weight["l2_assoc_cost"]          * cpival.l2_assoc
    cacheline_size_cost_total   = cost_weight["cacheline_size_cost"]    * cpival.size

    cost =  l1d_size_cost_total + \
            l1i_size_cost_total + \
            l2_size_cost_total + \
            l1d_assoc_cost_total + \
            l1i_assoc_cost_total + \
            l2_assoc_cost_total + \
            cacheline_size_cost_total
   
    return cost

def evaluate(i):
    if i.bm == "401.bzip2":
        c = i.cpi/5.191292009
    elif i.bm == "429.mcf":
        c = i.cpi/1.0240455
    elif i.bm == "456.hmmer":
        c = i.cpi/1.151417501
    elif i.bm == "458.sjeng":
        c = i.cpi/17.58480152
    elif i.bm == "470.lbm":
        c = i.cpi/10.21103247
    else:
        c = i.cpi
    i.value = c * (i.cost/650)
    return i

def minimum(listcpi):
    min = 1000000000000000000
    best = None
    for i in listcpi:
        if i.value < min:
            min = i.value
            best = i
    return best


def optimize(benchmark, init=None, min=CPI_Read_In.CPIData("", "", 0,value=10000000000000000000)):
    #l1d_assoc=0, l1i_assoc=0, l2_assoc=0, size=0, l1d_size=0, l1i_size=0
    if init is None:
        init = [3,3,4,4,3]
    projectlocation = "/people/cs/a/art150530/Project1_SPEC"
    l1d_size_options = ["16", "32", "64", "128"]
    l1i_size_options = ["16", "32", "64", "128"]
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
                  "--l1d_size=" + l1d_size_options[init[0]] + "kB " \
                  "--l1i_size=" + l1i_size_options[init[1]] + "kB " \
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
    cpiData = CPI_Read_In.CPIData(benchmark[0], "NA", cpival,
                                    l1d_assoc=int(l1d_assoc_options[init[2]]), l1i_assoc=int(l1i_assoc_options[init[3]]),
                                    l2_assoc=1,
                                    size=int(size_options[init[4]]), l1d_size=int(l1d_size_options[init[0]]),
                                    l1i_size=int(l1i_size_options[init[1]]))
    costval = cost(cpiData)
    cpiData.cost = costval
    cpiData = evaluate(cpiData)
    newinit = []
    for val in init:
        if val == 0:
            newinit.append(0)
        else:
            newinit.append(val-1)
    print(cpiData.value)
    print(cpiData.cpi)
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


def run(num):
    benchmark = [["401.bzip2","./data/input.program"],
                                  ["429.mcf","./data/inp.in"],
                                  ["456.hmmer", "./data/bombesin.hmm.new"],
                                  ["458.sjeng", "./data/test.txt"],
                                  ["470.lbm", "./data/lbm.in"]]
    cpithing = optimize(benchmark[num])
    with open('../data/optimization'+benchmark[num][0]+'.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Benchmark", "Experiment", "CPI", "Data Associativity", "Instruction Associativity",
                "L2 Associativity", "Block Size", "Data Size", "Instruction Size", "Cost"])
        writer.writerow(cpithing.toArray())

