from music21 import *
import os
import operator

all_diffs = {}

for f in sorted(os.listdir('../gen_am/')):
	if f.endswith('.xml'):
		print('###### '+f+' ######')
		base_peggy = ('../gen_am/'+f)
		diffs = []
		total = 0
		for i in sorted(os.listdir('../gen_am/')):
			if i.endswith('.xml'):
				peggy_pair = omr.evaluators.OmrGroundTruthPair(omr=converter.parse(base_peggy),ground=converter.parse('../gen_am/'+i))
				diff = peggy_pair.getDifferences()
				diffs.append(diff)
				total += diff
				print(i+': '+str(diff))
		all_diffs[f] = total
		print(' ')

# print(all_diffs)
sorted_all_diffs = sorted(all_diffs.items(), key=operator.itemgetter(1))
print(sorted_all_diffs)
print('winner: '+str(sorted_all_diffs[0]))
print('average edit distance for winner: '+str(sorted_all_diffs[0][1]/(len(all_diffs)-1))