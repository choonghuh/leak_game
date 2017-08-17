import random

class Staff:
	def __init__(self, namestr=None, titlestr=None, staff_id=None, loyalty=None):
		self.name = namestr
		self.title = titlestr
		self.id = staff_id
		#implement department?
		self.loyalty = loyalty
		self.fired = False
		if loyalty is None:
			self.loyalty = 50 + random.randint(0,50)

		self.insider_infos = []

	def decrease_loyalty(self, amount):
		self.loyalty = max(0, self.loyalty - amount)

	def increase_loyalty(self, amount):
		self.loyalty = min(100, self.loyalty + amount)

	def leak(self, do_it=False):
		# if loyalty < 50 and has info on something
		if (self.loyalty<50 or do_it) and len(self.insider_infos)>0:
			print("Lets see if %s wants to leak" % self.name)
			pass
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
			namestr = "staff member " + str(staff_id)
			titlestr = "job title " + str(staff_id)
			self.staff_list.append(Staff(namestr, titlestr, staff_id))

	def overview(self):
		# TODO - Want to display loyalty only if spied or researched
		if len(self.staff_list) == 0:
			return
		for staff in self.staff_list:
			if not staff.fired:
				print("%s - %s - ID:%d - %d/100 - Info: %d" % \
					(staff.name, staff.title,\
					staff.id, staff.loyalty, len(staff.insider_infos)))

	def fire(self, sid):
		exists = False
		for staff in self.staff_list:
			if staff.id == sid:
				staff.fired = True
				exists = True
				print("Fired %s" % staff.name)

	def process_info(self, info_id, details):
		# detail should be dict with key 'name' and 'severity'. Raise KeyError maybe
		new_info = Info(info_id, details['name'], details['severity'])

		count = 0
		for staff in self.staff_list:
			if random.randint(0,4) % 4 == 0: # For now, 25% chance
				staff.insider_infos.append(new_info)
				count += 1
				# TODO - If NOT A SPY, decrease loyalty by SOME amount.
				staff.decrease_loyalty(details['severity']*random.randint(0,5))

		print("%d staff(s) found out about this event." % count)


class President:
	class PresidentAction:
		def __init__(self, name, likelihood, severity):
			self.name = name
			self.likelihood = likelihood
			self.severity = severity


	def __init__(self):
		self.available_actions = [
			self.PresidentAction("doing nothing", 10, 0),
			self.PresidentAction("chatting with Vladimir Putin", 1, 2),
			self.PresidentAction("taking bribes", 1, 2),
			self.PresidentAction("yelling racial profanity at staff", 2, 1),
			self.PresidentAction("yelling homophobic profanity at staff", 2, 1),
			self.PresidentAction("chatting with an ex-girlfriend", 1, 1),
			self.PresidentAction("on a drunken rant", 1, 1),
		]

	# Return an Info / None?
	def do_something(self):
		temp_action_list = []
		for action in self.available_actions:
			for aa in xrange(0, action.likelihood):
				temp_action_list.append({"name":action.name, "severity":action.severity})

		choice = temp_action_list[random.randint(0,len(temp_action_list)-1)]
		print("\nPresident is " + choice["name"] + "...\n")
		if choice["severity"] != 0:
			# return {"name":choice.name, "severity":choice.severity}
			return choice
		return None

class Info:
	def __init__(self, info_id, summary=None, severity=None):
		self.info_id = info_id
		self.summary = summary
		# self.details = details
		self.published = False


class Leak:
	# Gonna need to think about this...
	# Leak needs to have:
	# - info (info_id)
	# - who did it (staff_id)
	def __init__(self, info_id, staff_id):
		self.info_id = info_id
		self.staff_id = staff_id


class Director:
	def __init__(self, namestr=None, respect=None):
		self.name = namestr
		self.respect = respect # Max 300
		if respect is None:
			self.respect = 200

	def increase_respect(self, amount=0):
		self.respect = min(300, self.respect + amount)
