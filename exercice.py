#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(nb):
	return (0 if nb==0 else 1 if nb==1 else get_fibonacci_number(nb-1) + get_fibonacci_number(nb-2))

def get_fibonacci_sequence(nb):
	fib = [0]
	while len(fib)<nb:
		if len(fib)<2: fib.append(1)
		else: fib.append(fib[-1]+fib[-2])
	return fib

def get_sorted_dict_by_decimals(dct):
	return dict(sorted(dct.items(), key= lambda x: x[1]%1))

def fibonacci_numbers(length):
	elems = [0,1]
	
	for _ in range(length):
		if elems[0] == 0:
			yield elems.pop(0)
			elems.append(1)
		else:
			elems.append(elems[0]+elems[1])
			yield elems.pop(0)


def build_recursive_sequence_generator(values: list, fct, sequenceInMem=False):
	
	def gen(length):
		for value in values[:length]:
			yield value
		last_elems = deque(values)
		for _ in range(len(values), length):
			elem = fct(last_elems)
			last_elems.append(elem)
			if not sequenceInMem:
				last_elems.popleft()
			yield elem
	
	return gen


if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator([2,1], lambda lst: lst[-1]+lst[-2])
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator([3,0,2], lambda seq: seq[-2]+seq[-3])
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator([1,1], lambda seq: seq[-(seq[-1])] + seq[-(seq[-2])], True)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
