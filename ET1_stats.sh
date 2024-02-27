max=95
for i in `seq 1 $max`
do
    python3 ./src/sudtosat.py <./ET1/ET1_puzzles/ET1puzzle${i}.txt >./tmp/puzzle.cnf
    minisat tmp/puzzle.cnf tmp/assign.txt >./results/stat.txt
    python3 ./src/sattosud.py <./tmp/assign.txt >./results/solution.txt
    echo $i >> ET1_stats.txt
    python3 ./src/extract_stats.py ./results/stat.txt >>ET1_stats.txt
done