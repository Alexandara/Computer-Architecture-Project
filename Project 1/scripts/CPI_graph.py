"""
Program written by Alexis Tudor at the University of Texas at Dallas
Email at alexisrenee1@gmail.com
Copyright and Licensing: GNU @ Alexis Tudor
"""
import csv
import matplotlib
import matplotlib.pyplot as plt
class CPIData:
    def __init__(self, benchmark, experimentName, cpi, l1d_assoc=0, l1i_assoc=0, l2_assoc=0, size=0, l1d_size=0, l1i_size=0):
        self.bm = benchmark
        self.exp = experimentName
        self.cpi = cpi
        self.l1d_assoc = l1d_assoc
        self.l1i_assoc = l1i_assoc
        self.l2_assoc = l2_assoc
        self.size = size
        self.l1d_size = l1d_size
        self.l1i_size = l1i_size

def readCPI(filename):
    cpidata=[]
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[1][0] == 'B' and row[1][1] == 'l':
                number = row[1][9]
                if number == "1":
                    cpidata.append(CPIData(row[0],row[1],float(row[2]), size = 8))
                elif number == "2":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), size=16))
                elif number == "3":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), size=32))
                elif number == "4":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), size=64))
            elif row[1][0] == "S" and row[1][1] == "e":
                number = row[1][8]
                number2 = row[1][9]
                if number == "1" and number2 == ".":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_assoc=2, l1i_assoc=2, l2_assoc=1))
                elif number == "2":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_assoc=4, l1i_assoc=4, l2_assoc=1))
                elif number == "3":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_assoc=8, l1i_assoc=8, l2_assoc=1 ))
                elif number == "4":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_assoc=16, l1i_assoc=16, l2_assoc=1 ))
                elif number == "5":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_assoc=4, l1i_assoc=2, l2_assoc=1))
                elif number == "6":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_assoc=8, l1i_assoc=2, l2_assoc=1))
                elif number == "7":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_assoc=16, l1i_assoc=2, l2_assoc=1))
                elif number == "8":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_assoc=2, l1i_assoc=4, l2_assoc=1))
                elif number == "9":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_assoc=2, l1i_assoc=8, l2_assoc=1))
                elif number == "1" and number2 == "0":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_assoc=2, l1i_assoc=16, l2_assoc=1))
                elif number == "1" and number2 == "1":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_assoc=1, l1i_assoc=1, l2_assoc=1))
                elif number == "1" and number2 == "2":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_assoc=2, l1i_assoc=1, l2_assoc=1))
                elif number == "1" and number2 == "3":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_assoc=1, l1i_assoc=2, l2_assoc=1))
            elif row[1][0] == "S" and row[1][1] == "i":
                number = row[1][9]
                if number == "1" and number2 == ".":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_size=128, l1i_size=128))
                elif number == "2":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_size=64, l1i_size=128))
                elif number == "3":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_size=32, l1i_size=128))
                elif number == "4":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_size=16, l1i_size=128))
                elif number == "5":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_size=128, l1i_size=64))
                elif number == "6":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_size=128, l1i_size=32))
                elif number == "7":
                    cpidata.append(CPIData(row[0], row[1], float(row[2]), l1d_size=128, l1i_size=16))
    return cpidata

def plot(X: object, Y: object, title: object, xLabel: object, offset: object, name: object) -> object:
    plt.scatter(X, Y)
    plt.ylabel("CPI")
    plt.title(title)
    plt.xlabel(xLabel)
    plt.tight_layout()
    plt.ylim((min(Y) - offset), (max(Y) + offset))
    y_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
    plt.gca().yaxis.set_major_formatter(y_formatter)
    plt.savefig(name, bbox_inches='tight')
    plt.close()

def generateGraphs(cpidata):
    b401SetSame = []
    b401SetSameX = []
    b401SetD = []
    b401SetDX = []
    b401SetI = []
    b401SetIX = []
    b401Block = []
    b401BlockX = []
    b401AllocD = []
    b401AllocDX = []
    b401AllocI = []
    b401AllocIX = []

    b429SetSame = []
    b429SetD = []
    b429SetI = []
    b429Block = []
    b429SetSameX = []
    b429SetDX = []
    b429SetIX = []
    b429BlockX = []
    b429AllocD = []
    b429AllocDX = []
    b429AllocI = []
    b429AllocIX = []

    b456SetSame = []
    b456SetD = []
    b456SetI = []
    b456Block = []
    b456SetSameX = []
    b456SetDX = []
    b456SetIX = []
    b456BlockX = []
    b456AllocD = []
    b456AllocDX = []
    b456AllocI = []
    b456AllocIX = []

    b458SetSame = []
    b458SetD = []
    b458SetI = []
    b458Block = []
    b458SetSameX = []
    b458SetDX = []
    b458SetIX = []
    b458BlockX = []
    b458AllocD = []
    b458AllocDX = []
    b458AllocI = []
    b458AllocIX = []

    b470SetSame = []
    b470SetD = []
    b470SetI = []
    b470Block = []
    b470SetSameX = []
    b470SetDX = []
    b470SetIX = []
    b470BlockX = []
    b470AllocD = []
    b470AllocDX = []
    b470AllocI = []
    b470AllocIX = []
    for cpi in cpidata:
        if cpi.bm == "401Data":
            if cpi.exp[0] == 'B' and cpi.exp[1] == 'l':
                b401Block.append(cpi.cpi)
                b401BlockX.append(cpi.size)
            elif cpi.exp[0] == "S" and cpi.exp[1] == "e":
                if cpi.l1d_assoc == cpi.l1i_assoc:
                    b401SetSame.append(cpi.cpi)
                    b401SetSameX.append(cpi.l1d_assoc)
                elif cpi.l1d_assoc == 2:
                    b401SetI.append(cpi.cpi)
                    b401SetIX.append(cpi.l1i_assoc)
                elif cpi.l1i_assoc == 2:
                    b401SetD.append(cpi.cpi)
                    b401SetDX.append(cpi.l1d_assoc)
            elif cpi.exp[0] == "S" and cpi.exp[1] == "i":
                if cpi.l1d_size == cpi.l1i_assoc:
                    b401AllocD.append(cpi.cpi)
                    b401AllocDX.append(cpi.l1d_size)
                    b401AllocI.append(cpi.cpi)
                    b401AllocIX.append(cpi.l1i_size)
                elif cpi.l1d_size == 128:
                    b401AllocI.append(cpi.cpi)
                    b401AllocIX.append(cpi.l1i_size)
                elif cpi.l1i_size == 128:
                    b401AllocD.append(cpi.cpi)
                    b401AllocDX.append(cpi.l1d_size)
        if cpi.bm == "429Data":
            if cpi.exp[0] == 'B' and cpi.exp[1] == 'l':
                b429Block.append(cpi.cpi)
                b429BlockX.append(cpi.size)
            elif cpi.exp[0] == "S" and cpi.exp[1] == "e":
                if cpi.l1d_assoc == cpi.l1i_assoc:
                    b429SetSame.append(cpi.cpi)
                    b429SetSameX.append(cpi.l1d_assoc)
                elif cpi.l1d_assoc == 2:
                    b429SetI.append(cpi.cpi)
                    b429SetIX.append(cpi.l1i_assoc)
                elif cpi.l1i_assoc == 2:
                    b429SetD.append(cpi.cpi)
                    b429SetDX.append(cpi.l1d_assoc)
            elif cpi.exp[0] == "S" and cpi.exp[1] == "i":
                if cpi.l1d_size == cpi.l1i_assoc:
                    b429AllocD.append(cpi.cpi)
                    b429AllocDX.append(cpi.l1d_size)
                    b429AllocI.append(cpi.cpi)
                    b429AllocIX.append(cpi.l1i_size)
                elif cpi.l1d_size == 128:
                    b429AllocI.append(cpi.cpi)
                    b429AllocIX.append(cpi.l1i_size)
                elif cpi.l1i_size == 128:
                    b429AllocD.append(cpi.cpi)
                    b429AllocDX.append(cpi.l1d_size)
        if cpi.bm == "456Data":
            if cpi.exp[0] == 'B' and cpi.exp[1] == 'l':
                b456Block.append(cpi.cpi)
                b456BlockX.append(cpi.size)
            elif cpi.exp[0] == "S" and cpi.exp[1] == "e":
                if cpi.l1d_assoc == cpi.l1i_assoc:
                    b456SetSame.append(cpi.cpi)
                    b456SetSameX.append(cpi.l1d_assoc)
                elif cpi.l1d_assoc == 2:
                    b456SetI.append(cpi.cpi)
                    b456SetIX.append(cpi.l1i_assoc)
                elif cpi.l1i_assoc == 2:
                    b456SetD.append(cpi.cpi)
                    b456SetDX.append(cpi.l1d_assoc)
            elif cpi.exp[0] == "S" and cpi.exp[1] == "i":
                if cpi.l1d_size == cpi.l1i_assoc:
                    b456AllocD.append(cpi.cpi)
                    b456AllocDX.append(cpi.l1d_size)
                    b456AllocI.append(cpi.cpi)
                    b456AllocIX.append(cpi.l1i_size)
                elif cpi.l1d_size == 128:
                    b456AllocI.append(cpi.cpi)
                    b456AllocIX.append(cpi.l1i_size)
                elif cpi.l1i_size == 128:
                    b456AllocD.append(cpi.cpi)
                    b456AllocDX.append(cpi.l1d_size)
        if cpi.bm == "458Data":
            if cpi.exp[0] == 'B' and cpi.exp[1] == 'l':
                b458Block.append(cpi.cpi)
                b458BlockX.append(cpi.size)
            elif cpi.exp[0] == "S" and cpi.exp[1] == "e":
                if cpi.l1d_assoc == cpi.l1i_assoc:
                    b458SetSame.append(cpi.cpi)
                    b458SetSameX.append(cpi.l1d_assoc)
                elif cpi.l1d_assoc == 2:
                    b458SetI.append(cpi.cpi)
                    b458SetIX.append(cpi.l1i_assoc)
                elif cpi.l1i_assoc == 2:
                    b458SetD.append(cpi.cpi)
                    b458SetDX.append(cpi.l1d_assoc)
            elif cpi.exp[0] == "S" and cpi.exp[1] == "i":
                if cpi.l1d_size == cpi.l1i_assoc:
                    b458AllocD.append(cpi.cpi)
                    b458AllocDX.append(cpi.l1d_size)
                    b458AllocI.append(cpi.cpi)
                    b458AllocIX.append(cpi.l1i_size)
                elif cpi.l1d_size == 128:
                    b458AllocI.append(cpi.cpi)
                    b458AllocIX.append(cpi.l1i_size)
                elif cpi.l1i_size == 128:
                    b458AllocD.append(cpi.cpi)
                    b458AllocDX.append(cpi.l1d_size)
        if cpi.bm == "470Data":
            if cpi.exp[0] == 'B' and cpi.exp[1] == 'l':
                b470Block.append(cpi.cpi)
                b470BlockX.append(cpi.size)
            elif cpi.exp[0] == "S" and cpi.exp[1] == "e":
                if cpi.l1d_assoc == cpi.l1i_assoc:
                    b470SetSame.append(cpi.cpi)
                    b470SetSameX.append(cpi.l1d_assoc)
                elif cpi.l1d_assoc == 2:
                    b470SetI.append(cpi.cpi)
                    b470SetIX.append(cpi.l1i_assoc)
                elif cpi.l1i_assoc == 2:
                    b470SetD.append(cpi.cpi)
                    b470SetDX.append(cpi.l1d_assoc)
            elif cpi.exp[0] == "S" and cpi.exp[1] == "i":
                if cpi.l1d_size == cpi.l1i_assoc:
                    b470AllocD.append(cpi.cpi)
                    b470AllocDX.append(cpi.l1d_size)
                    b470AllocI.append(cpi.cpi)
                    b470AllocIX.append(cpi.l1i_size)
                elif cpi.l1d_size == 128:
                    b470AllocI.append(cpi.cpi)
                    b470AllocIX.append(cpi.l1i_size)
                elif cpi.l1i_size == 128:
                    b470AllocD.append(cpi.cpi)
                    b470AllocDX.append(cpi.l1d_size)

    offset401 = .000000001
    offset429 = .0000001
    offset456 = .00000001
    offset458 = .00000001
    offset470 = .000000001

    # Set Same
    setSameTitle = "CPI for Set Associativity of both L1 Data and Instruction Caches"
    setSameXAxis = "Set Associativity for L1 Data and Instruction Caches"
    plot(b401SetSameX, b401SetSame, setSameTitle, setSameXAxis, offset401, "../graphs/401SameSetAlloc.png")
    plot(b429SetSameX, b429SetSame, setSameTitle, setSameXAxis, offset429, "../graphs/429SameSetAlloc.png")
    plot(b456SetSameX, b456SetSame, setSameTitle, setSameXAxis, offset456, "../graphs/456SameSetAlloc.png")
    plot(b458SetSameX, b458SetSame, setSameTitle, setSameXAxis, offset458, "../graphs/458SameSetAlloc.png")
    plot(b470SetSameX, b470SetSame, setSameTitle, setSameXAxis, offset470, "../graphs/470SameSetAlloc.png")

    # SetD
    setDTitle = "CPI for Set Associativity of L1 Data Cache"
    setDXAxis = "Set Associativity for L1 Data Cache"
    plot(b470SetDX, b470SetD, setDTitle, setDXAxis, offset470, "../graphs/470DataSetAlloc.png")
    plot(b458SetDX, b458SetD, setDTitle, setDXAxis, offset458, "../graphs/458DataSetAlloc.png")
    plot(b456SetDX, b456SetD, setDTitle, setDXAxis, offset456, "../graphs/456DataSetAlloc.png")
    plot(b429SetDX, b429SetD, setDTitle, setDXAxis, offset429, "../graphs/429DataSetAlloc.png")
    plot(b401SetDX, b401SetD, setDTitle, setDXAxis, offset401, "../graphs/401DataSetAlloc.png")

    # SetI
    setITitle = "CPI for Set Associativity of L1 Instruction Cache"
    setIXAxis = "Set Associativity for L1 Instruction Cache"
    plot(b470SetIX, b470SetI, setITitle, setIXAxis, offset470, "../graphs/470InstructionSetAlloc.png")
    plot(b458SetIX, b458SetI, setITitle, setIXAxis, offset458, "../graphs/458InstructionSetAlloc.png")
    plot(b456SetIX, b456SetI, setITitle, setIXAxis, offset456, "../graphs/456InstructionSetAlloc.png")
    plot(b429SetIX, b429SetI, setITitle, setIXAxis, offset429, "../graphs/429InstructionSetAlloc.png")
    plot(b401SetIX, b401SetI, setITitle, setIXAxis, offset401, "../graphs/401InstructionSetAlloc.png")

    # Block Size
    setBlockTitle = "CPI for Block Size of both L1 Caches"
    setBlockXAxis = "Cache Block Size"
    plot(b401BlockX, b401Block, setBlockTitle, setBlockXAxis, offset401, "../graphs/401BlockSize.png")
    plot(b429BlockX, b429Block, setBlockTitle, setBlockXAxis, offset429, "../graphs/429BlockSize.png")
    plot(b456BlockX, b456Block, setBlockTitle, setBlockXAxis, offset456, "../graphs/456BlockSize.png")
    plot(b458BlockX, b458Block, setBlockTitle, setBlockXAxis, offset458, "../graphs/458BlockSize.png")
    plot(b470BlockX, b470Block, setBlockTitle, setBlockXAxis, offset470, "../graphs/470BlockSize.png")

    # Size Allocation Data
    setSizeDataTitle = "CPI for Size Allocation for L1 Data Cache Given 128kB Instruction Cache"
    setSizeDataXAxis = "L1 Data Cache Size (kB)"
    plot(b470AllocDX, b470AllocD, setSizeDataTitle, setSizeDataXAxis, offset470, "../graphs/470DataSizeAllocation.png")
    plot(b458AllocDX, b458AllocD, setSizeDataTitle, setSizeDataXAxis, offset458, "../graphs/458DataSizeAllocation.png")
    plot(b456AllocDX, b456AllocD, setSizeDataTitle, setSizeDataXAxis, offset456, "../graphs/456DataSizeAllocation.png")
    plot(b429AllocDX, b429AllocD, setSizeDataTitle, setSizeDataXAxis, offset429, "../graphs/429DataSizeAllocation.png")
    plot(b401AllocDX, b401AllocD, setSizeDataTitle, setSizeDataXAxis, offset401, "../graphs/401DataSizeAllocation.png")

    # Size Allocation Instruction
    setSizeInstructionTitle = "CPI for Size Allocation for L1 Instruction Cache Given 128kB Data Cache"
    setSizeInstructionXAxis = "L1 Instruction Cache Size (kB)"
    plot(b470AllocIX, b470AllocI, setSizeInstructionTitle, setSizeInstructionXAxis, offset470, "../graphs/470InstructionSizeAllocation.png")
    plot(b458AllocIX, b458AllocI, setSizeInstructionTitle, setSizeInstructionXAxis, offset458, "../graphs/458InstructionSizeAllocation.png")
    plot(b456AllocIX, b456AllocI, setSizeInstructionTitle, setSizeInstructionXAxis, offset456, "../graphs/456InstructionSizeAllocation.png")
    plot(b429AllocIX, b429AllocI, setSizeInstructionTitle, setSizeInstructionXAxis, offset429, "../graphs/429InstructionSizeAllocation.png")
    plot(b401AllocIX, b401AllocI, setSizeInstructionTitle, setSizeInstructionXAxis, offset401, "../graphs/401InstructionSizeAllocation.png")




generateGraphs(readCPI("../data/cpi.csv"))
