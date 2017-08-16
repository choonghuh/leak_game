import sys

from datetime import datetime

from entities import StaffList, Director, Leak

import random

class Game:
	def __init__(self, namestr):
		self.start_time = str(datetime.now())

		# Entities
		self.director = Director(namestr)
		self.staff_list = StaffList()

		# States
		self.total_leaks = 0
		self.day = 1
		self.todays_leaks = []

	def motd(self):
		print("Day - " + str(self.day))
		print("President tolerates you this much - %d / 300" % self.director.respect)
		self.process_leaks()

	def process_leaks(self):
		if len(self.todays_leaks) < 1:
			print("Another peaceful day without a leak. Well done, Director.")
			self.director.increase_respect(5)

	def print_actions(self):
		print("1 - View your current status and history.")
		print("2 - View the staff list")
		print("3 - Fire a staff")
		pass

	def pass_day(self):
		#leak here
		for staff in self.staff_list.staff_list:
			leak = staff.leak()
			if leak is not None:
				self.todays_leaks.append(leak)
		self.day += 1

	def playgame(self):
		print("Let's do it")
		while self.director.respect>0:
			self.motd()
			#self.spy_overview() # Some spy that tells you who knows what info
			self.print_actions()
			action = int(raw_input())#Check Input
			if action == 1:
				pass
			elif action == 2:
				self.staff_list.overview()
				pass
			elif action == 3:
				pass
			

			self.pass_day()

		print("You moron! You are fired!")


if __name__ == '__main__':
	py3 = sys.version_info[0] > 2

	if py3:
		name = input("What is your name, Director?")
	else:
		name = raw_input("What is your name, Director?")

	if name in ['', None]:
		name = "Choong"
	print("Good luck, " + name)
	Game(name).playgame()