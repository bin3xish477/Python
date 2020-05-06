#!/usr/bin/env python3

"""
Tests the validaotr functions
Command line: python -m pytest tests/test_resources.py
"""

import pytest


from app.models import inventory


@pytest.fixture
def resource_values():
	return {
		'name': 'Parrot',
		'manufacturer': 'Pirates A-Hoy',
		'total': 100,
		'allocated': 50
	}


@pytest.fixture
def resource(resource_values):
	return inventory.Resource(**resource_values)


def test_create_resource(resource_values, resource):
	for attr_name in resource_values:
		assert getattr(resource, attr_name) == resource_values.get(attr_name)


def test_create_invalid_total_type():
	with pytest.raises(TypeError):
		resource = inventory.Resource("Parrot", "Pirate A-Hoy", 10.5, 5)