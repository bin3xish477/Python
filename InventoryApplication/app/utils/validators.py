#!/usr/bin/env python3

"""Various Validators"""

def validate_integer(
	arg_name, arg_value, min_value=None, max_value=None,
	custom_min_msg=None, custom_max_msg=None 
):
	""" Validates that `arg_value` is an integer, and optionally falls within
	specific bounds.
	A custom override error message can be provided when min/max bounds are
	exceeded.
	Args:
		arg_name (str): 
		arg_value (obj):
		min_value (int):
		max_value (int):
		custom_min_msg (str):
		custom_max_msg (str):

	Returns:
		None: no exceptions raised if validation passes.

	Raises:
		TypeError: if `arg_value` is not an integer
		ValueError: if `arg_value` does not satisfy the bounds
	"""
	if not isinstance(arg_value, int):
		raise TypeError(f"{arg_name} must be an integer.")

	if min_value is not None and arg_value < min_value:
		if custom_min_msg is not None:
			raise ValueError(custom_min_msg)
		raise ValueError(f"{arg_name} cannot be less than {min_value}")

	if max_value is not None and arg_value > max_value:
		if custom_max_msg is not None:
			raise ValueError(custom_max_msg)
		raise ValueError(f"{arg_name} cannot be greater than {max_value}")
