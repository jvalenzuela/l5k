"""Unit tests for built-in structured data type definitions."""

import unittest

from . import common


class Counter(unittest.TestCase):
    """COUNTER value tests."""

    def test_pre(self):
        """Confirm correct preset value."""
        self.assert_value("[0,42,0]", PRE=42)

    def test_acc(self):
        """Confirm correct accumulator value."""
        self.assert_value("[0,0,42]", ACC=42)

    def test_cu(self):
        """Confirm correct count-up value."""
        self.assert_value("[-2147483648,0,0]", CU=1)

    def test_cd(self):
        """Confirm correct count-down value."""
        self.assert_value("[1073741824,0,0]", CD=1)

    def test_dn(self):
        """Confirm correct done value."""
        self.assert_value("[536870912,0,0]", DN=1)

    def test_ov(self):
        """Confirm correct overflow value."""
        self.assert_value("[268435456,0,0]", OV=1)

    def test_un(self):
        """Confirm correct underflow value."""
        self.assert_value("[134217728,0,0]", UN=1)

    def assert_value(self, raw, *, PRE=0, ACC=0, CU=0, CD=0, DN=0, OV=0, UN=0):
        """Verifies raw data is converted to the correct structured value."""
        # Allow default arguments for all members.
        # pylint: disable=too-many-arguments

        ctl = common.parse(
            f"""
            CONTROLLER ctl
            TAG
            tag : COUNTER := {raw};
            END_TAG
            END_CONTROLLER
            """
        )
        expected = {
            "PRE": PRE,
            "ACC": ACC,
            "CU": CU,
            "CD": CD,
            "DN": DN,
            "OV": OV,
            "UN": UN,
        }
        self.assertEqual(expected, ctl.tags["tag"].value)


class Timer(unittest.TestCase):
    """TIMER value tests."""

    def test_pre(self):
        """Confirm correct preset value."""
        self.assert_value("[0,42,0]", PRE=42)

    def test_acc(self):
        """Confirm correct accumulator value."""
        self.assert_value("[0,0,42]", ACC=42)

    def test_en(self):
        """Confirm correct enable value."""
        self.assert_value("[-2147483648,0,0]", EN=1)

    def test_tt(self):
        """Confirm correct timer timing value."""
        self.assert_value("[1073741824,0,0]", TT=1)

    def test_dn(self):
        """Confirm correct done value."""
        self.assert_value("[536870912,0,0]", DN=1)

    def assert_value(self, raw, *, PRE=0, ACC=0, EN=0, TT=0, DN=0):
        """Verifies raw data is converted to the correct structured value."""
        # Allow default arguments for all members.
        # pylint: disable=too-many-arguments

        ctl = common.parse(
            f"""
            CONTROLLER ctl
            TAG
            tag : TIMER := {raw};
            END_TAG
            END_CONTROLLER
            """
        )
        expected = {
            "PRE": PRE,
            "ACC": ACC,
            "EN": EN,
            "TT": TT,
            "DN": DN,
        }
        self.assertEqual(expected, ctl.tags["tag"].value)
