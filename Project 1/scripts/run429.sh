export LOC=429
export DATA="./data/inp.in"

# Base
rm ~/m5out/stats.txt
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/Base.txt

# Set Assoc 1
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SetAssoc1.txt

# Set Assoc 2
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=4 --l1i_assoc=4 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SetAssoc2.txt

#Set Assoc 3
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SetAssoc3.txt

#Set Assoc 4
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=16 --l1i_assoc=16 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SetAssoc4.txt

#Set Assoc 5
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=4 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SetAssoc5.txt

#Set Assoc 6
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=8 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SetAssoc6.txt

#Set Assoc 7
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=16 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SetAssoc7.txt

#Set Assoc 8
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=4 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SetAssoc8.txt

#Set Assoc 9
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=8 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SetAssoc9.txt

#Set Assoc 10
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=16 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SetAssoc10.txt

#Set Assoc 11
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=1 --l1i_assoc=1 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SetAssoc11.txt

#Set Assoc 12
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=1 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SetAssoc12.txt

#Set Assoc 13
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=1 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SetAssoc13.txt

#Block Size 1
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/BlockSize1.txt

#Block Size 2
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=16"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/BlockSize2.txt

#Block Size 3
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=32"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/BlockSize3.txt

#Block Size 4
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/BlockSize4.txt

#Size Alloc 1
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SizeAlloc1.txt

#Size Alloc 2
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=64kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SizeAlloc2.txt

#Size Alloc 3
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=32kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SizeAlloc3.txt

#Size Alloc 4
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=16kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SizeAlloc4.txt

#Size Alloc 5
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=64kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SizeAlloc5.txt

#Size Alloc 6
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=32kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SizeAlloc6.txt

#Size Alloc 7
export CS="--cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=16kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=8"
/usr/local/gem5/build/X86/gem5.opt -d ~/m5out /usr/local/gem5/configs/example/se.py -I 100000000 -c ./src/benchmark -o $DATA $CS
mv ~/m5out/stats.txt ~/m5out/$LOC/SizeAlloc7.txt























