from account import Account

class Account():
	def __repr__(self):
		return f"Account : {self._name}, {self._email}, {self._verif_ques},\
		{self._birth_date}, {self._password}, {self._phone_num}, {self._age}"
