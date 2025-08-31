"""Unit tests for built-in structured data type definitions."""

import unittest

import l5k
from . import common


class StructureValue(unittest.TestCase):
    """Base class for testing structured values."""

    DATATYPE = None  # Set to data type name in subclass.

    def assert_value(self, raw, **kwargs):
        """Verifies raw data is converted to the correct structured value."""
        ctl = common.parse(
            f"""
            CONTROLLER ctl
            TAG
            tag : {self.DATATYPE} := {raw};
            END_TAG
            END_CONTROLLER
            """
        )

        # Initialize an expected value with zero for all non-hidden members.
        datatype = l5k.builtin.BUILT_INS[self.DATATYPE]
        expected = {}
        for name in datatype.members:
            try:
                if int(datatype.members[name].attributes["Hidden"]) == 1:
                    continue
            except KeyError:
                pass
            expected[name] = 0

        # Overwrite any member values provided in the arguments.
        expected.update(kwargs)

        self.assertEqual(expected, ctl.tags["tag"].value)


class Control(StructureValue):
    """CONTROL value tests."""

    DATATYPE = "CONTROL"

    def test_en(self):
        """Confirm correct EN value."""
        self.assert_value("[-2147483648,0,0]", EN=1)

    def test_eu(self):
        """Confirm correct EU value."""
        self.assert_value("[1073741824,0,0]", EU=1)

    def test_dn(self):
        """Confirm correct DN value."""
        self.assert_value("[536870912,0,0]", DN=1)

    def test_em(self):
        """Confirm correct EM value."""
        self.assert_value("[268435456,0,0]", EM=1)

    def test_er(self):
        """Confirm correct ER value."""
        self.assert_value("[134217728,0,0]", ER=1)

    def test_ul(self):
        """Confirm correct UL value."""
        self.assert_value("[67108864,0,0]", UL=1)

    def test_in(self):
        """Confirm correct IN value."""
        self.assert_value("[33554432,0,0]", IN=1)

    def test_fd(self):
        """Confirm correct FD value."""
        self.assert_value("[16777216,0,0]", FD=1)

    def test_len(self):
        """Confirm correct LEN value."""
        self.assert_value("[0,42,0]", LEN=42)

    def test_pos(self):
        """Confirm correct POS value."""
        self.assert_value("[0,0,42]", POS=42)


class Counter(StructureValue):
    """COUNTER value tests."""

    DATATYPE = "COUNTER"

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


class Timer(StructureValue):
    """TIMER value tests."""

    DATATYPE = "TIMER"

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
