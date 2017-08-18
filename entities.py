from random import randint
import names

class Staff:
	def __init__(self, namestr=None, titlestr=None, staff_id=None, loyalty=None):
		self.name = namestr or str(names.get_full_name())
		self.title = titlestr or "Some Staff"
		self.id = staff_id
		#implement department?
		self.loyalty = loyalty
		if loyalty is None:
			self.loyalty = 40 + randint(0,50)

		self.insider_infos = []

	def decrease_loyalty(self, amount):
		self.loyalty = max(0, self.loyalty - amount)

	def increase_loyalty(self, amount):
		self.loyalty = min(100, self.loyalty + amount)

	def leak(self, do_it=False):
		# if loyalty < 50 and has info on something
		if (randint(0,100) > self.loyalty + 50 or do_it) and len(self.insider_infos)>0:
			leaked = self.insider_infos[randint(0,len(self.insider_infos)-1)]
			print("%s is leaking info from day %d!!" % (self.name, leaked.info_id))
			return leaked
		else:
			return None

	def has_info_on(self, info_id):
		for info in self.insider_infos:
			if info.info_id == info_id:
				return True
		return False


class StaffList:
	def __init__(self, howmany=30):
		self.staff_list = []

		for staff_id in xrange(1, howmany+1):
			# namestr = "staff member " + str(staff_id)
			namestr = None
			# titlestr = "job title " + str(staff_id)
			titlestr = None
			self.staff_list.append(Staff(namestr, titlestr, staff_id))

	def overview(self):
		# TODO - Want to display loyalty only if spied or researched
		print("\n")
		if len(self.staff_list) == 0:
			return
		for staff in self.staff_list:
			print("%s - %s - ID:%d - %d/100 - Info: %d" % \
				(staff.name, staff.title,\
				staff.id, staff.loyalty, len(staff.insider_infos)))
		print("\n")

	def fire(self, sid):
		exists = False
		for staff in self.staff_list:
			if staff.id == sid:
				exists = True
				print("Firing %s" % staff.name)
				self.staff_list.remove(staff)
		if not exists:
			print("Staff with that ID does not exist!")

	def process_info(self, info_id, details):
		# detail should be dict with key 'name' and 'severity'. Raise KeyError maybe
		new_info = Info(info_id, details['name'], details['severity'])

		count = 0
		for staff in self.staff_list:
			if randint(1,5) % 5 == 0: # For now, 10% chance to obtain info
				staff.insider_infos.append(new_info)
				count += 1
				# TODO - If NOT A SPY, decrease loyalty by SOME amount.
				staff.decrease_loyalty(details['severity']*randint(0,5))

		print("%d staff(s) found out about this event." % count)

	def clear_leaked_info(self, iid):
		for staff in self.staff_list:
			for info in staff.insider_infos:
				if info.info_id == iid:
					staff.insider_infos.remove(info)

class President:
	class PresidentAction:
		def __init__(self, name, likelihood, severity):
			self.name = name
			self.likelihood = likelihood
			self.severity = severity


	def __init__(self):
		self.available_actions = [
			self.PresidentAction("doing nothing", 1, 0),
			self.PresidentAction("chatting with Vladimir Putin", 1, 2),
			self.PresidentAction("taking bribes", 1, 2),
			self.PresidentAction("yelling racial profanity at staff", 2, 1),
			self.PresidentAction("yelling homophobic profanity at staff", 2, 1),
			self.PresidentAction("chatting dirty with an ex-girlfriend", 1, 1),
			self.PresidentAction("on a drunken rant", 1, 1),
		]

	# Return an Info / None?
	def do_something(self):
		temp_action_list = []
		for action in self.available_actions:
			for aa in xrange(0, action.likelihood):
				temp_action_list.append({"name":action.name, "severity":action.severity})

		choice = temp_action_list[randint(0,len(temp_action_list)-1)]
		print("\nPresident is " + choice["name"] + "...\n")
		if choice["severity"] != 0:
			# return {"name":choice.name, "severity":choice.severity}
			return choice
		return None

class Info:
	def __init__(self, info_id, summary, severity):
		self.info_id = info_id
		self.summary = summary
		self.severity = severity
		# self.details = details

class Leak:
	# Gonna need to think about this...
	# Leak needs to have:
	# - info (info_id)
	# - who did it (staff_id)
	# Gonna need to delete the info from everyone's info list
	def __init__(self, info, staff_id):
		self.info = info
		self.staff_id = staff_id


class Director:
	def __init__(self, namestr=None, respect=None):
		self.name = namestr
		self.respect = respect # Max 300
		if respect is None:
			self.respect = 200

	def increase_respect(self, amount=0):
		self.respect = min(300, self.respect + amount)
