# TournamentBP 
time TournamentBP/gem5/build/X86/gem5.opt -d TournamentBP/gem5/m5out /usr/local/gem5/configs/example/se.py -I 500000000 -c /people/cs/a/art150530/Project1_SPEC/401.bzip2/src/benchmark -o /people/cs/a/art150530/Project1_SPEC/401.bzip2/data/input.program --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=4 --cacheline_size=64
cp TournamentBP/gem5/m5out/stats.txt data/TournamentBP/TournamentBP401.txt

time TournamentBP/gem5/build/X86/gem5.opt -d TournamentBP/gem5/m5out /usr/local/gem5/configs/example/se.py -I 500000000 -c /people/cs/a/art150530/Project1_SPEC/429.mcf/src/benchmark -o /people/cs/a/art150530/Project1_SPEC/429.mcf/data/inp.in --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=4 --cacheline_size=64
cp TournamentBP/gem5/m5out/stats.txt data/TournamentBP/TournamentBP429.txt

time TournamentBP/gem5/build/X86/gem5.opt -d TournamentBP/gem5/m5out /usr/local/gem5/configs/example/se.py -I 500000000 -c /people/cs/a/art150530/Project1_SPEC/456.hmmer/src/benchmark -o /people/cs/a/art150530/Project1_SPEC/456.hmmer/data/bombesin.hmm --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=4 --cacheline_size=64
cp TournamentBP/gem5/m5out/stats.txt data/TournamentBP/TournamentBP456.txt

time TournamentBP/gem5/build/X86/gem5.opt -d TournamentBP/gem5/m5out /usr/local/gem5/configs/example/se.py -I 500000000 -c /people/cs/a/art150530/Project1_SPEC/458.sjeng/src/benchmark -o /people/cs/a/art150530/Project1_SPEC/458.sjeng/data/test.txt --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=4 --cacheline_size=64
cp TournamentBP/gem5/m5out/stats.txt data/TournamentBP/TournamentBP458.txt

time TournamentBP/gem5/build/X86/gem5.opt -d TournamentBP/gem5/m5out /usr/local/gem5/configs/example/se.py -I 500000000 -c /people/cs/a/art150530/Project1_SPEC/470.lbm/src/benchmark -o /people/cs/a/art150530/Project1_SPEC/470.lbm/data/lbm.in --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=4 --cacheline_size=64
cp TournamentBP/gem5/m5out/stats.txt data/TournamentBP/TournamentBP470.txt

cp -r data/TournamentBP data/TournamentBP$SET



























