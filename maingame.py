import sys, time

from datetime import datetime, timedelta

from entities import StaffList, Director, President, Leak

# TODO - Implement salary?
# TODO - Implement spying


class Game:
	def __init__(self, namestr):
		self.start_time = datetime.now()

		# Entities
		self.director = Director(namestr)
		self.staff_list = StaffList(20)
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
		self.todays_leak = None

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
		if self.todays_leak:
			print("Oh no!")
			news_date = self.start_time + timedelta(days = self.todays_leak.info.info_id)
			make_news(self.todays_leak, str(news_date))
			self.director.decrease_respect(self.todays_leak.severity * 10)
		else:
			print("Another peaceful day without a leak. Well done, Director.")
			self.director.increase_respect(5)

		self.todays_leak = None

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
			info = staff.leak()
			if info is not None:
				#break, clear leak from the rest of the staffs
				leak = Leak(info, staff.id)
				self.todays_leak = leak
				self.staff_list.clear_leaked_info(leak.info.info_id)
				self.total_leaks += 1
		self.day += 1

	def playgame(self):
		print("Let's do this\n\n")
		while self.director.respect>0:
			# Start of the day. Display Messages Of The Day
			self.motd()
			# TODO - self.spy_overview() # Some spy that tells you who knows what info

			# Display a list of available actions
			self.print_actions()
			action = get_int_input(max=len(self.action_list)+1)
			while action != len(self.action_list)+1:
				self.action_list[action-1]()
				time.sleep(1)
				self.print_actions()
				action = get_int_input(max=len(self.action_list)+1)
			self.pass_day()

		print("You moron! You are fired!")

def make_news(leak, date):
	main_bit = leak.info.summary
	headline = "Report: President " + main_bit + "."
	print("="*(len(headline)+10))
	print("|    "+headline+"    |")
	print("="*(len(headline)+10))
	print(date)

def get_int_input(max):
	ok = False
	while not ok:
		try:
			action = int(raw_input("What to do? :  "))#Check Input
			if action>0 and action<=max:
				return action
			else:
				print("Only enter a valid option number")
		except ValueError:
			print("Only enter a valid option number")
			pass
		# except:
		# 	print("Only enter a valid option number")
		# 	print("Unknown exception!!")

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