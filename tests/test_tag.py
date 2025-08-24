"""Tag unit tests."""

import unittest

from . import common


class Dimensions(unittest.TestCase):
    """Tests for the array dimension attribute."""

    def test_default(self):
        """Confirm default value if no dimensions are present."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG
            tag : DINT := 0;
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertIsNone(ctl.tags["tag"].dim)

    def test_dim(self):
        """Confirm array dimensions are stored."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG
            tag : DINT[3,2,1] := [0,0,0,0,0,0];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual((1, 2, 3), ctl.tags["tag"].dim)


class Attributes(unittest.TestCase):
    """Tests for tag attributes."""

    def test_default(self):
        """Confirm default value if no attributes are present."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG
            tag : DINT := 0;
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({}, ctl.tags["tag"].attributes)

    def test_attributes(self):
        """Confirm attributes are stored."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG
            tag : DINT (foo := bar) := 0;
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({"foo": "bar"}, ctl.tags["tag"].attributes)


class BaseTypeValue(unittest.TestCase):
    """Base data type value tests."""

    def test_binary(self):
        """Confirm a binary value."""
        self.assert_value("2#0000_0000_0000_1111", 15)

    def test_octal(self):
        """Confirm an octal value."""
        self.assert_value("8#000_017", 15)

    def test_decimal(self):
        """Confirm a decimal value."""
        for i in [-42, 0, 15]:
            with self.subTest(i=i):
                self.assert_value(str(i), i)

    def test_hex(self):
        """Confirm a hexadecimal value."""
        self.assert_value("16#000F", 15)

    def test_ascii(self):
        """Confirm an ASCII value."""
        self.assert_value("'spam eggs'", "spam eggs")

    def test_exponential(self):
        """Confirm exponential values.

        Fractional values selected with exact floating-point representations,
        i.e., can be written as a fraction with a denominator that is a
        power of 2.
        """
        for lit, val in [("2.5e-01", 0.25), ("-2.5e+01", -25.0)]:
            with self.subTest(lit=lit, val=val):
                self.assert_value(lit, val)

    def test_float(self):
        """Confirm float values.

        Non-zero values selected with exact floating-point representations,
        i.e., can be written as a fraction with a denominator that is a
        power of 2.
        """
        for i in [-1.25, -0.0, 1.25]:
            with self.subTest(i=i):
                self.assert_value(str(i), i)

    def assert_value(self, literal, expected):
        """Verifies the resulting value and type."""
        ctl = common.parse(
            f"""
            CONTROLLER ctl
            TAG
            foo : xxx := {literal};
            END_TAG
            END_CONTROLLER
            """
        )
        value = ctl.tags["foo"].value
        self.assertEqual(expected, value)
        self.assertIs(type(expected), type(value))


class StructureValue(unittest.TestCase):
    """Structured data type value tests."""

    def test_undefined(self):
        """Confirm the value of an undefined type."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG
            foo : undefined := [1,2,3];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual([1, 2, 3], ctl.tags["foo"].value)

    def test_member(self):
        """Confirm normal(non-bit) members are captured."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            DATATYPE foo
                DINT m1;
                DINT m2;
            END_DATATYPE
            TAG
            tag : foo := [42, 99];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({"m1": 42, "m2": 99}, ctl.tags["tag"].value)

    def test_bit_member(self):
        """Confirm bit members are captured.

        SINTs seem to be used for bit storage, so this test includes a bit
        member occupying the sign bit(MSB) to ensure the bit value is
        correctly extracted from a negative number.
        """
        ctl = common.parse(
            """
            CONTROLLER ctl
            DATATYPE foo
                SINT m1 (Hidden := 1);
                BIT b0 m1 : 0;
                BIT b7 m1 : 7;
            END_DATATYPE
            TAG
            tag : foo := [-128];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({"b0": 0, "b7": 1}, ctl.tags["tag"].value)

    def test_hidden(self):
        """Confirm hidden members are removed."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            DATATYPE foo
                DINT m1;
                DINT m2 (Hidden := 1);
            END_DATATYPE
            TAG
            tag : foo := [42, 99];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({"m1": 42}, ctl.tags["tag"].value)


class ArrayValue(unittest.TestCase):
    """Array value tests."""

    def test_single_dimension(self):
        """Confirm value for a single-dimensional array."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG
            foo : DINT[3] := [42, 99, 15];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual([42, 99, 15], ctl.tags["foo"].value)

    def test_multi_dimension(self):
        """Confirm value for a multi-dimensional array."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG
            foo : DINT[2,2,2] := [42,99,10,18,64,72,2,35];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            [
                [
                    [42, 99],
                    [10, 18],
                ],
                [
                    [64, 72],
                    [2, 35],
                ],
            ],
            ctl.tags["foo"].value,
        )

    def test_length_one(self):
        """Confirm value for a dimension containing one element."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG
            foo : DINT[1] := [42];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual([42], ctl.tags["foo"].value)


class ComplexValue(unittest.TestCase):
    """Tests for values of nested structures and arrays."""

    def test_array_of_struct(self):
        """Confirm value of an array of UDTs."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            DATATYPE udt
                DINT m1;
                DINT m2;
            END_DATATYPE
            TAG
            tag : udt[2] := [[1,2],[3,4]];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            [{"m1": 1, "m2": 2}, {"m1": 3, "m2": 4}], ctl.tags["tag"].value
        )

    def test_array_member(self):
        """Confirm value of a UDT with an array member."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            DATATYPE udt
                DINT m1;
                DINT m2[2];
            END_DATATYPE
            TAG
            tag : udt := [1,[2,3]];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({"m1": 1, "m2": [2, 3]}, ctl.tags["tag"].value)

    def test_nested_struct(self):
        """Confirm value of a UDT with a nested UDT member."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            DATATYPE udt1
                DINT m1;
                DINT m2;
            END_DATATYPE
            DATATYPE udt2
                udt1 m1;
            END_DATATYPE
            TAG
            tag : udt2 := [[1,2]];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({"m1": {"m1": 1, "m2": 2}}, ctl.tags["tag"].value)


class NoValue(unittest.TestCase):
    """Tests for data types that do not include a normal value."""

    def test_no_value(self):
        """Confirm no value."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG
            tag : no_value_type;
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertIsNone(ctl.tags["tag"].value)
