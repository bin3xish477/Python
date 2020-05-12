"""Tests the CPU class
Command line: python -m pytest tests/unit/test_cpu.py
"""

import pytest


from app.models import inventory


@pytest.fixture
def cpu_values():
	return {
		'name': 'RYZEN Threadripper 2990WX',
		'manufacturer': 'AMD',
		'total': 10,
		'allocated': 3,
		'cores': 32,
		'socket': 'sTR4',
		'power_watts': 250
	}


@pytest.fixture
def cpu(cpu_values):
	inventory.CPU(**cpu_values)