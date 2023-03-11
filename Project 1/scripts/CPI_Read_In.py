"""
Program written by Alexis Tudor at the University of Texas at Dallas
Email at alexisrenee1@gmail.com
Copyright and Licensing: GNU @ Alexis Tudor
"""
import csv

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
                    cpidata.append(CPIData(row[0],row[1],float(row[2]), size = 8:))
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
                if number == "1":
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