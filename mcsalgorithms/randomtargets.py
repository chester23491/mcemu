# -*- coding: utf-8 -*-
#
# Calculates availabilities for random assignments

from distavail import Service, ServiceSet
import random

class Random:
	def __init__(self, debug=False, debugout=False, calcmode=None):
		self.debug = debug
		self.debugout = debugout
		self.logtext = ""
		self.calcmode = calcmode

	def log(self, s):
		if self.debug:
			if self.debugout:
				print "»", s
			self.logtext += "» " + str(s) + "\n"

	def getlog(self):
		return self.logtext

	def random(self, services):
		shares = [0] * len(services)
		for i in range(len(services)):
			shares[random.randint(0, len(services) - 1)] += 1

		for i, service in enumerate(services):
			if shares[i] == 0:
				service.fragment = 0
			elif shares[i] > 1:
				service.redundant = shares[i] - 1

		self.log("Random shares = %s" % str(shares))
		if not shares:
			return None

		ss = ServiceSet(services, debug=False)
		oav = ss.availability(k=random.randint(1, len(services)), mode=self.calcmode)

		return oav
