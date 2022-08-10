#!/usr/bin/python3
import sys
import time
import random
import argparse


parser = argparse.ArgumentParser(description='Loto & euromillions game')
parser.add_argument('-e','--euromillions',dest='euromillions',action='store_true',help='Choose Euromillions mode')
parser.add_argument('-l','--loto',dest='loto',action='store_true',help='Choose Loto mode')
args = parser.parse_args()

numbers = []
stars = []

z = """
 			Tirage en cours ....
        [+]█████████████████████████████████████████████████[+]
"""
for c in z:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.02)

def tirage(name_list,len_num,nb_min,nb_max):

	for x in range(len_num):
		gen_num = random.randrange(nb_min,nb_max)
		name_list.append(gen_num)
		if name_list.count(gen_num) > 1:
			name_list.remove(gen_num)
			name_list.append(random.randrange(nb_min,nb_max))
	return name_list


if args.euromillions:
	print('Numbers:',tirage(numbers,5,1,49))
	print('Stars:',tirage(stars,2,1,12))
elif args.loto:
	print('Numbers:',tirage(numbers,5,1,49))
	print('Stars:',tirage(numbers,1,1,12))
