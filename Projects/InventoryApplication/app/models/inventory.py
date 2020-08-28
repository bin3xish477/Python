#!/usr/bin/env python3

"""Inventory Models"""

from app.utils.validators import validate_integer

class Resource:
	"""Base class for resources"""
	def __init__(self, name, manufacturer, total, allocated):
		"""

		Args:
			name (str):
			manufacturer (str):
			total (int):
			allocated (int):

		Note:
			`allocated` cannot exceed `total`
		"""

		self._name = name
		self._manufacturer = manufacturer

		validate_integer('total', total, min_value=0)
		self._total = total

		validate_integer('allocated', allocated, 0, total,
			custom_max_msg='Allocated inventory cannot exceed total inventory.')
		self._allocated = allocated

	@property
	def name(self) -> str:
		"""

		Returns:
			str: the resource name
		"""
		return self._name
		
	@property
	def manufacturer(self) -> str:
		"""

		Returns:
			str: the resource manufacturer
		"""
		return self._manufacturer

	@property
	def total(self) -> int:
		"""

		Returns:
			int: the total inventory count
		"""
		return self._total

	@property
	def allocated(self) -> int:
		"""

		Returns:
			int: the number of resources used
		"""
		return self._allocated
	
	@property
	def category(self) -> str:
		"""

		Returns:
			str: the resource category
		"""
		return type(self).__name__.lower()
	
	@property
	def available(self) -> int:
		"""
		
		Returns:
			int: the number of resources available for use
		"""
		return self.total - self.allocated
	
	def __str__(self):
		return self.name

	def __repr__(self):
		return (f"{self.name} {self.category}-{self.manufacturer}:"
				f"total={self.total}, allocated={self.allocated}"
				)

	def claim(self, num):
		"""Claim number of inventory items (if available)

		Args:
			num (int): number of inventory items to claim

		Returns:
			None
		"""
		validate_integer(
			'num', num, 1, self.available, 
			custom_max_msg="Cannot claim more than available"
		)
		self._allocated += num

	def freeup(self, num):
		"""Return an inventory item to the available pool

		Args:
			num (int): Number of items to return (cannot exceed number is use)

		Returns:

		"""
		validate_integer(
			'num', num, 1, self.allocated,
			custom_max_msg='Cannot return more than allocated.'
		)
		self._allocated -= num

	def dies(self, num):
		"""Number of items to deallocate and remove the inventory pool

		Args:
			num (int): Number of items that have died
		
		Returns:

		"""
		validate_integer(
			'num', num, 1, self.allocated,
			custom_max_msg='Cannot retire more than allocated.'
		)
		self._total -= num
		self._allocated -= num

	def purchased(self, num):
		"""Add new inventory to the pool

		Args:
			num (int): Number of items to add to the pool

		Returns:

		"""
		validate_integer('num', num, 1)
		self._total += num


class CPU(Resource):
	"""Resource subclass used to track specific CPU inventory pools"""

	def __init__(
		self, name, manufacturer, total, allocated,
		cores, socket, power_watts
	):
		super().__init__(name, manufacturer, total, allocated)

		validate_integer('cores', cores, 1)
		validate_integer('power_watts', power_watts, 1)

		self._cores = cores
		self._socket = socket
		self._power_watts = power_watts


	@property
	def cores(self) -> int:
		"""Number of cores.

		Returns:
			int
		"""
		return self._cores


	@property
	def power_watts(self) -> int:
		"""The rated wattage of this CPU.

		Returns:
			int
		"""		
		return self._power_watts


	@property
	def socket(self) -> str:
		"""The socket type of this CPU.

		Returns:
			str
		"""
		return self._socket
	
	
	def __repr__(self):
		return f"{self.category}: {self.name} ({self.socket} - x{self.cores}"