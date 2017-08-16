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
			print("Lets see if %s wants to leak")
			pass
		else:
			return None

	def has_info_on(self, info_id):
		for info in self.insider_infos:
			if info.info_id == info_id:
				return True
		return False

class Infos:
	def __init__(self, info_id, summary=None, details=None, severity=None):
		self.info_id = info_id
		self.summary = summary
		self.details = details
		self.published = False


class StaffList:
	def __init__(self, howmany=30):
		self.staff_list = []

		for staff_id in xrange(1, howmany+1):
			namestr = "staff member " + str(staff_id)
			titlestr = "job title " + str(staff_id)
			self.staff_list.append(Staff(namestr, titlestr, staff_id))

	def overview(self):
		if len(self.staff_list) == 0:
			return
		for staff in self.staff_list:
			if not staff.fired:
				print("%s - %s - ID:%d - %d/100" % \
					(staff.name, staff.title,\
					staff.id, staff.loyalty))

	def fire(self, sid):
		exists = False
		for staff in self.staff_list:
			if staff.id == sid:
				staff.fired = True
				exists = True
				print("Fired %s" % staff.name)


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
