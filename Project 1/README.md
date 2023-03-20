# Computer-Architecture-Project-1

## Script Variables
$LOC is the location of the folder in ~/m5out to put the output files

$DATA is the input file from the data folder in the benchmark.

## Data Key
### Base Command:
- --cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8

### Set Associativity:
1. --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 
2. --l1d_assoc=4 --l1i_assoc=4 --l2_assoc=1 
3. --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=1 
4. --l1d_assoc=16 --l1i_assoc=16 --l2_assoc=1 
5. --l1d_assoc=4 --l1i_assoc=2 --l2_assoc=1 
6. --l1d_assoc=8 --l1i_assoc=2 --l2_assoc=1 
7. --l1d_assoc=16 --l1i_assoc=2 --l2_assoc=1 
8. --l1d_assoc=2 --l1i_assoc=4 --l2_assoc=1 
9. --l1d_assoc=2 --l1i_assoc=8 --l2_assoc=1
10. --l1d_assoc=2 --l1i_assoc=16 --l2_assoc=1 
11. --l1d_assoc=1 --l1i_assoc=1 --l2_assoc=1 
12. --l1d_assoc=2 --l1i_assoc=1 --l2_assoc=1 
13. --l1d_assoc=1 --l1i_assoc=2 --l2_assoc=1 

### Block Size:
1. --cacheline_size=8
2. --cacheline_size=16
3. --cacheline_size=32
4. --cacheline_size=64

### Size Allocation:
1. --l1d_size=128kB --l1i_size=128kB --l2_size=1MB 
2. --l1d_size=64kB --l1i_size=128kB --l2_size=1MB 
3. --l1d_size=32kB --l1i_size=128kB --l2_size=1MB 
4. --l1d_size=16kB --l1i_size=128kB --l2_size=1MB 
5. --l1d_size=128kB --l1i_size=64kB --l2_size=1MB 
6. --l1d_size=128kB --l1i_size=32kB --l2_size=1MB
7. --l1d_size=128kB --l1i_size=16kB --l2_size=1MB 
