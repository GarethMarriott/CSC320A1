# Created by Gareth Marriott
# V00875748

from pprint import pp
import fileinput

stats = []
for line in fileinput.input():
    stats.append(line)

# pp(stats)
# pp("----")

results = dict()

for line in stats:
    if "CPU time" in line:
        l = []
        for t in line.split():
            try:
                l.append(float(t))
            except ValueError:
                pass
        # pp(l)
        results["CPU time"] = l[0]

    if "restarts" in line:
        l = []
        for t in line.split():
            try:
                l.append(float(t))
            except ValueError:
                pass
        # pp(l)
        results["restarts"] = l[0]

    if "conflicts" in line:
        l = []
        for t in line.split():
            try:
                l.append(float(t))
            except ValueError:
                pass
        # pp(l)
        results["conflicts"] = l[0]

    if "propagations" in line:
        l = []
        for t in line.split():
            try:
                l.append(float(t))
            except ValueError:
                pass
        # pp(l)
        results["propagations"] = l[0]

    if "conflict literals" in line:
        l = []
        for t in line.split():
            try:
                l.append(float(t))
            except ValueError:
                pass
        # pp(l)
        results["conflict literals"] = l[0]

    if "Memory used" in line:
        l = []
        for t in line.split():
            try:
                l.append(float(t))
            except ValueError:
                pass
        # pp(l)
        results["Memory used"] = l[0]


    if "SATISFIABLE" in line:
        results["satisfiable"] = True

pp(results)
if "satisfiable" not in results:
    results["satisfiable"] = False
