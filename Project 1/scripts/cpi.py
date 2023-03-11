import os
import csv
data_directories = ["401Data", "429Data", "456Data", "458Data", "470Data"]

# Fields of interest in data files
DL1_MISS_NUM_SRT  = "system.cpu.dcache.overall_miss_rate::total"
IL1_MISS_NUM_SRT = "system.cpu.icache.overall_miss_rate::total"
L2_MISS_NUM_SRT = "system.l2.overall_misses::total"
TOTAL_NUM_INST_SRT = "sim_insts"

data_list = [["Directory", "File", "CPI"]]
row_data = []

for dir in data_directories:
    print("Start of" , dir)
    dir_path = "../" + dir
    print(dir_path)
    dir_data_files = os.listdir(dir_path)
    for data_file in dir_data_files:
        print("Data for file" , data_file, "in directory", dir)
        data_file_path = dir_path + '/' + data_file
        with open(data_file_path, 'r') as file:        
            data = file.read().splitlines()
            for row in data:
                if (len(row) == 0):
                    continue          
                sim_stats = row.split(maxsplit=2)
                if(sim_stats[0] == IL1_MISS_NUM_SRT):
                    print("IL1.miss_num:", sim_stats[1])
                    il1_miss_num = float(sim_stats[1])
                if(sim_stats[0] == DL1_MISS_NUM_SRT):
                    print("DL1.miss_num:", sim_stats[1])
                    dl1_numm_num = float(sim_stats[1])
                if(sim_stats[0] == L2_MISS_NUM_SRT):
                    print("L2.miss_num:", sim_stats[1])
                    l2_miss_num = float(sim_stats[1])
                if(sim_stats[0] == TOTAL_NUM_INST_SRT):
                    print("Total_Inst_num:", sim_stats[1])
                    total_num_inst = float(sim_stats[1])
        cpi = 1 + ((il1_miss_num + dl1_numm_num) * 6 + l2_miss_num * 50) / total_num_inst
        print("CPI:", cpi)
        row_data.append(dir)
        row_data.append(data_file)
        row_data.append(cpi)
        data_list.append(row_data)
        row_data = []
        print("\n")
        
with open('../data/cpi.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for list in data_list:
        writer.writerow(list)