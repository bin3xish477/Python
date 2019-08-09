import pickle as pic
class Account():
	def __init__(self, name='none', email='none', verif_ques='none', 
		birth_date='none', password='none', phone_num=0, age=0):
		self._name = name
		self._email = email
		self._verif_ques = verif_ques
		self._birth_date = birth_date
		self._password = password
		self._phone_num = phone_num
		self._age = age

	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, name):
		self._name = name
		return self._name

	@property
	def email(self):
		return self._email
	@email.setter
	def email(self, email):
		self._email= email

	@property
	def verif_ques(self):
		return self._verif_ques
	@verif_ques.setter
	def verif_ques(self, verif_ques):
		self._verif_ques = new_verif_ques
		return self._verif_ques

	@property
	def birth_date(self):
		return self._birth_date
	@birth_date.setter
	def birth_date(self, birth_date):
		self._birth_date = birth_date
		return self._birth_date

	@property
	def password(self):
		return self._password
	@password.setter
	def password(self, password):
		self._password = password
		return self._password

	@property
	def phone_num(self):
		return self._phone_num
	@phone_num.setter
	def phone_num(self, phone_num):
		self._phone_num = phone_num
		return self._phone_num

	@property
	def age(self):
		return self._age
	@age.setter
	def age(self, age):
		self._age = age
		return self._age
	
	def __repr__(self):
		return f"Account : {self._name}, {self._email}, {self._verif_ques} , {self._birth_date}, {self._password}, {self._phone_num}, {self._age}"
