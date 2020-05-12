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


def test_create_invalid_allocated_type():
	with pytest.raises(TypeError):
		resource = inventory.Resource("name", "manu", 10, 2.5)


def test_create_invalid_total_value():
	with pytest.raises(ValueError):
		resource = inventory.Resource("name", "manu", -10, 0)


@pytest.mark.parametrize('total,allocated', [(10, -5), (10, 20)])
def test_create_invalid_allocated_value(total, allocated):
	with pytest.raises(ValueError):
		inventory.Resource('name', 'manu', total, allocated)


def test_total(resource):
	assert resource.total == resource._total


def test_allocated(resource):
	assert resource.allocated == resource._allocated


def test_available(resource):
	assert resource.available == resource.total - resource.allocated


def test_category(resource):
	assert resource.category == 'resource'


def test_claim(resource):
	n = 2
	original_total = resource.total
	original_allocated = resource.allocated
	resource.claim(n)
	assert resource.total == original_total
	assert resource.allocated == original_allocated + n


@pytest.mark.parametrize('value', [-1, 0, 1_000])
def test_invalid_claim(resource, value):
	with pytest.raises(ValueError):
		resource.claim(value)