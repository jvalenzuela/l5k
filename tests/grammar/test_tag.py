"""Tests for TAG parsing grammar."""

import unittest

import l5k


class DataType(unittest.TestCase):
    """Tests for the data type identifier."""

    def test_module(self):
        """Confirm module types are accepted."""
        self.parse("AB:5000_DO16:O:0")

    def parse(self, data_type):
        l5k.grammar.TAG.parse_string(f"TAG foo : {data_type} := 0; END_TAG")
