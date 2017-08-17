import sys, time, random

from datetime import datetime

from entities import StaffList, Director, President, Leak

class Game:
	def __init__(self, namestr):
		self.start_time = str(datetime.now())

		# Entities
		self.director = Director(namestr)
		self.staff_list = StaffList()
		self.president = President()

		self.action_list = [
			self.view_status,
			self.staff_list.overview,
			self.fire_staff,
		]

		# States
		self.total_leaks = 0
		self.fired_staffs = 0
		self.day = 1
		self.todays_leaks = []

	def view_status(self):
		pass

	def fire_staff(self):
		# Need to take another raw input
		staff_id = int(raw_input("Enter the Staff ID of the staff member to be fired: "))
		self.staff_list.fire(staff_id)
		pass

	def motd(self):
		print("Day - " + str(self.day))
		print("President tolerates you this much - %d / 300" % self.director.respect)
		self.process_leaks()

	def process_leaks(self):
		if len(self.todays_leaks) < 1:
			print("Another peaceful day without a leak. Well done, Director.")
			self.director.increase_respect(5)

		self.todays_leaks = []

	def process_president(self):
		print("\n\nPresident is thinking....\n")
		time.sleep(3)
		something = self.president.do_something()
		time.sleep(3)
		if something:
			# TODO - determine which staff will know about this. For now, all?
			# Day is OK as a unique Info ID as long as there is only one per day
			self.staff_list.process_info(self.day, something)


	def print_actions(self):
		print("1 - View your current status and history.")
		print("2 - View the staff list")
		print("3 - Fire a staff")
		print("4 - End the day")
		# Use a skill?
		# Use item or money to silence a leak, convince a staff, etc.?
		pass

	def pass_day(self):
		# President randomly does dumb stuff here
		self.process_president()


		#leak here
		for staff in self.staff_list.staff_list:
			leak = staff.leak()
			if leak is not None:
				self.todays_leaks.append(leak)
		self.day += 1

	def playgame(self):
		print("Let's do it")
		while self.director.respect>0:
			# Start of the day. Display Messages Of The Day
			self.motd()
			# TODO - self.spy_overview() # Some spy that tells you who knows what info

			# Display a list of available actions
			self.print_actions()
			action = int(raw_input())#Check Input
			while action != 4:
				self.action_list[action-1]()
				self.print_actions()
				action = int(raw_input())#Check Input
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