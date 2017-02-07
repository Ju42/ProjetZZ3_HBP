#!/usr/bin/python
# -*-coding:Utf-8 -*

year=input("Saisissez une année :")

if year%4==0 :
	if year%100==0:
		if year%400==0 :
			print("Bissextile")
		else:
			print("Non bissextile")
	else:
		print("Bissextile")
else:
	print("Non bissextile")

print(__name__)
