"""Tests for models"""
from django.test import TestCase
from core import calc


class CalcTest(TestCase):
    def test_add(self):
        result = calc.add(4, 4)
        self.assertEqual(result, 8)
