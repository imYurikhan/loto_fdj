#!/usr/bin/python

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
rand_num = random.randrange(1,49)

def euromillions(nb_stars):

	z = """
 			Tirage en cours ....
        [+]█████████████████████████████████████████████████[+]

"""
	for c in z:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.02)
	for num in range(5):
		add_num_to_list = numbers.append(rand_num)
		if numbers.count(rand_num) > 1:
			multiple_numbers()
	for star in range(nb_stars):
		rand_star = random.randrange(1,12)
		stars.append(rand_star)
		if stars.count(rand_num) > 1:
			multiple_numbers()
	return numbers,stars

def multiple_numbers():
	ind = numbers.index(rand_num)
	new_random_num = random.randrange(1,49)
	numbers.remove(rand_num)
	numbers.insert(ind,new_random_num)

def loto():
	euromillions(1)

if args.euromillions:
	euromillions(2)
	print(f'Numbers: {numbers}\nStars: {stars}')

elif args.loto:
	loto()
	print(f'Numbers: {numbers}\nStars: {stars}')
