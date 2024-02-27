max=49
for i in `seq 1 $max`
do
    python3 ./src/sudtosat.py <./puzzles/puzzle${i}.txt >./tmp/puzzle.cnf
    minisat tmp/puzzle.cnf tmp/assign.txt >./results/stat.txt
    python3 ./src/sattosud.py <./tmp/assign.txt >./results/solution.txt
    echo $i >> simple_stats.txt
    python3 ./src/extract_stats.py ./results/stat.txt >>simple_stats.txt
done