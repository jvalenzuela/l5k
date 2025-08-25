"""Tests for MODULE parsing grammar."""

import unittest

import l5k


class Name(unittest.TestCase):
    """Tests for parsing the module name."""

    def test_no_name(self):
        """Confirm unnamed modules are accepted."""
        self.parse("$NoName")

    def parse(self, name):
        """Attempts to parse a given name."""
        l5k.grammar.MODULE.parse_string(f"MODULE {name} END_MODULE")
