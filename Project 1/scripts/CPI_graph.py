"""
Program written by Alexis Tudor at the University of Texas at Dallas
Email at alexisrenee1@gmail.com
Copyright and Licensing: GNU @ Alexis Tudor
"""
import CPI_Read_In
import matplotlib
import matplotlib.pyplot as plt

def plot(X: object, Y: object, title: object, xLabel: object, name: object) -> object:
    plt.scatter(X, Y)
    plt.ylabel("CPI")
    plt.title(title)
    plt.margins(x = .1, y = .1)
    plt.xlabel(xLabel)
    plt.tight_layout()
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

    # Set Same
    setSameTitle = "CPI for Set Associativity of both L1 Data and Instruction Caches for Benchmark "
    setSameXAxis = "Set Associativity for L1 Data and Instruction Caches"
    plot(b401SetSameX, b401SetSame, setSameTitle+"401.bzip2", setSameXAxis, "../graphs/401/401SameSetAlloc.png")
    plot(b429SetSameX, b429SetSame, setSameTitle+"429.mcf", setSameXAxis, "../graphs/429/429SameSetAlloc.png")
    plot(b456SetSameX, b456SetSame, setSameTitle+"456.hmmer", setSameXAxis, "../graphs/456/456SameSetAlloc.png")
    plot(b458SetSameX, b458SetSame, setSameTitle+"458.sjeng", setSameXAxis, "../graphs/458/458SameSetAlloc.png")
    plot(b470SetSameX, b470SetSame, setSameTitle+"470.lbm", setSameXAxis, "../graphs/470/470SameSetAlloc.png")

    # SetD
    setDTitle = "CPI for Set Associativity of L1 Data Cache for Benchmark "
    setDXAxis = "Set Associativity for L1 Data Cache"
    plot(b470SetDX, b470SetD, setDTitle+"470.lbm", setDXAxis, "../graphs/470/470DataSetAlloc.png")
    plot(b458SetDX, b458SetD, setDTitle+"458.sjeng", setDXAxis, "../graphs/458/458DataSetAlloc.png")
    plot(b456SetDX, b456SetD, setDTitle+"456.hmmer", setDXAxis, "../graphs/456/456DataSetAlloc.png")
    plot(b429SetDX, b429SetD, setDTitle+"429.mcf", setDXAxis, "../graphs/429/429DataSetAlloc.png")
    plot(b401SetDX, b401SetD, setDTitle+"401.bzip2", setDXAxis, "../graphs/401/401DataSetAlloc.png")

    # SetI
    setITitle = "CPI for Set Associativity of L1 Instruction Cache for Benchmark "
    setIXAxis = "Set Associativity for L1 Instruction Cache"
    plot(b470SetIX, b470SetI, setITitle+"470.lbm", setIXAxis, "../graphs/470/470InstructionSetAlloc.png")
    plot(b458SetIX, b458SetI, setITitle+"458.sjeng", setIXAxis, "../graphs/458/458InstructionSetAlloc.png")
    plot(b456SetIX, b456SetI, setITitle+"456.hmmer", setIXAxis, "../graphs/456/456InstructionSetAlloc.png")
    plot(b429SetIX, b429SetI, setITitle+"429.mcf", setIXAxis, "../graphs/429/429InstructionSetAlloc.png")
    plot(b401SetIX, b401SetI, setITitle+"401.bzip2", setIXAxis, "../graphs/401/401InstructionSetAlloc.png")

    # Block Size
    setBlockTitle = "CPI for Block Size of both L1 Caches for Benchmark "
    setBlockXAxis = "Cache Block Size"
    plot(b401BlockX, b401Block, setBlockTitle+"401.bzip2", setBlockXAxis, "../graphs/401/401BlockSize.png")
    plot(b429BlockX, b429Block, setBlockTitle+"429.mcf", setBlockXAxis, "../graphs/429/429BlockSize.png")
    plot(b456BlockX, b456Block, setBlockTitle+"456.hmmer", setBlockXAxis, "../graphs/456/456BlockSize.png")
    plot(b458BlockX, b458Block, setBlockTitle+"458.sjeng", setBlockXAxis, "../graphs/458/458BlockSize.png")
    plot(b470BlockX, b470Block, setBlockTitle+"470.lbm", setBlockXAxis, "../graphs/470/470BlockSize.png")

    # Size Allocation Data
    setSizeDataTitle = "CPI for Size Allocation for L1 Data Cache Given 128kB Instruction Cache for Benchmark "
    setSizeDataXAxis = "L1 Data Cache Size (kB)"
    plot(b470AllocDX, b470AllocD, setSizeDataTitle+"470.lbm", setSizeDataXAxis, "../graphs/470/470DataSizeAllocation.png")
    plot(b458AllocDX, b458AllocD, setSizeDataTitle+"458.sjeng", setSizeDataXAxis, "../graphs/458/458DataSizeAllocation.png")
    plot(b456AllocDX, b456AllocD, setSizeDataTitle+"456.hmmer", setSizeDataXAxis, "../graphs/456/456DataSizeAllocation.png")
    plot(b429AllocDX, b429AllocD, setSizeDataTitle+"429.mcf", setSizeDataXAxis, "../graphs/429/429DataSizeAllocation.png")
    plot(b401AllocDX, b401AllocD, setSizeDataTitle+"401.bzip2", setSizeDataXAxis, "../graphs/401/401DataSizeAllocation.png")

    # Size Allocation Instruction
    setSizeInstructionTitle = "CPI for Size Allocation for L1 Instruction Cache Given 128kB Data Cache for Benchmark "
    setSizeInstructionXAxis = "L1 Instruction Cache Size (kB)"
    plot(b470AllocIX, b470AllocI, setSizeInstructionTitle+"470.lbm", setSizeInstructionXAxis, "../graphs/470/470InstructionSizeAllocation.png")
    plot(b458AllocIX, b458AllocI, setSizeInstructionTitle+"458.sjeng", setSizeInstructionXAxis, "../graphs/458/458InstructionSizeAllocation.png")
    plot(b456AllocIX, b456AllocI, setSizeInstructionTitle+"456.hmmer", setSizeInstructionXAxis, "../graphs/456/456InstructionSizeAllocation.png")
    plot(b429AllocIX, b429AllocI, setSizeInstructionTitle+"429.mcf", setSizeInstructionXAxis, "../graphs/429/429InstructionSizeAllocation.png")
    plot(b401AllocIX, b401AllocI, setSizeInstructionTitle+"401.bzip2", setSizeInstructionXAxis, "../graphs/401/401InstructionSizeAllocation.png")




generateGraphs(CPI_Read_In.readCPI("../data/cpi.csv"))
