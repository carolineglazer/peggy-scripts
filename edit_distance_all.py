from music21 import *
import os
import operator

all_diffs = {}

for f in sorted(os.listdir('..')):
	if f.endswith('.xml'):
		print('###### '+f+' ######')
		base_peggy = ('../'+f)
		diffs = []
		total = 0
		for i in sorted(os.listdir('..')):
			if i.endswith('.xml'):
				peggy_pair = omr.evaluators.OmrGroundTruthPair(omr=converter.parse(base_peggy),ground=converter.parse('../'+i))
				diff = peggy_pair.getDifferences()
				diffs.append(diff)
				total += diff
				print(i+': '+str(diff))
		all_diffs[f] = total
		print(' ')

# print(all_diffs)
sorted_all_diffs = sorted(all_diffs.items(), key=operator.itemgetter(1))
print(sorted_all_diffs)