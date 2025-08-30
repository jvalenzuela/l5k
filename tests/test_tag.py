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


class AddOnInstructionValue(unittest.TestCase):
    """Tests for AOI values."""

    def test_inout_parameter(self):
        """Confirm InOut parameters are excluded."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
            PARAMETERS
	    inout : DINT (Usage := InOut);
            END_PARAMETERS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG
            tag : aoi := [0];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({"EnableIn": 0, "EnableOut": 0}, ctl.tags["tag"].value)

    def test_input_parameters(self):
        """Confirm input parameter values are extracted."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
            PARAMETERS
	    EnableIn : BOOL (Usage := Input);
	    EnableOut : BOOL (Usage := Output);
	    in : DINT (Usage := Input);
            END_PARAMETERS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG
            tag : aoi := [1,42];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            {
                "EnableIn": 1,
                "EnableOut": 0,
                "in": 42,
            },
            ctl.tags["tag"].value,
        )

    def test_output_parameters(self):
        """Confirm output parameter values are extracted."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
            PARAMETERS
	    EnableIn : BOOL (Usage := Input);
	    EnableOut : BOOL (Usage := Output);
	    out : DINT (Usage := Output);
            END_PARAMETERS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG
            tag : aoi := [2,42];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            {
                "EnableIn": 0,
                "EnableOut": 1,
                "out": 42,
            },
            ctl.tags["tag"].value,
        )

    def test_local_tags(self):
        """Confirm local tag values are extracted."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
            PARAMETERS
	    EnableIn : BOOL (Usage := Input);
	    EnableOut : BOOL (Usage := Output);
            END_PARAMETERS
	    LOCAL_TAGS
	    local : DINT;
	    END_LOCAL_TAGS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG
            tag : aoi := [0,42];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            {
                "EnableIn": 0,
                "EnableOut": 0,
                "local": 42,
            },
            ctl.tags["tag"].value,
        )

    def test_bool(self):
        """Confirm BOOL parameters and local tags are correctly extracted.

        This AOI definition includes enough BOOL items to require more
        than one packed DINT, and non-BOOL items so the packed DINTs are
        nonconsecutive.
        """
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
            PARAMETERS
	    EnableIn : BOOL (Usage := Input);
	    EnableOut : BOOL (Usage := Output);
	    p0 : BOOL (Usage := Input);
	    p1 : BOOL (Usage := Input);
	    p2 : BOOL (Usage := Input);
	    p3 : BOOL (Usage := Input);
	    p4 : BOOL (Usage := Input);
	    p5 : BOOL (Usage := Input);
	    p6 : BOOL (Usage := Input);
	    p7 : BOOL (Usage := Input);
	    p8 : BOOL (Usage := Input);
	    pdint : DINT (Usage := Input);
            END_PARAMETERS
	    LOCAL_TAGS
	    t31 : BOOL (RADIX := Decimal);
	    t30 : BOOL (RADIX := Decimal);
	    t29 : BOOL (RADIX := Decimal);
	    t28 : BOOL (RADIX := Decimal);
	    t27 : BOOL (RADIX := Decimal);
	    t26 : BOOL (RADIX := Decimal);
	    t25 : BOOL (RADIX := Decimal);
	    t24 : BOOL (RADIX := Decimal);
	    t23 : BOOL (RADIX := Decimal);
	    t22 : BOOL (RADIX := Decimal);
	    t21 : BOOL (RADIX := Decimal);
	    t20 : BOOL (RADIX := Decimal);
	    t19 : BOOL (RADIX := Decimal);
	    t18 : BOOL (RADIX := Decimal);
	    t17 : BOOL (RADIX := Decimal);
	    t16 : BOOL (RADIX := Decimal);
	    t15 : BOOL (RADIX := Decimal);
	    t14 : BOOL (RADIX := Decimal);
	    t13 : BOOL (RADIX := Decimal);
	    t12 : BOOL (RADIX := Decimal);
	    t11 : BOOL (RADIX := Decimal);
	    t10 : BOOL (RADIX := Decimal);
	    t9 : BOOL (RADIX := Decimal);
	    tdint : DINT (RADIX := Decimal);
	    END_LOCAL_TAGS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG
            tag : aoi := [33587265,42,2,99];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            {
                "EnableIn": 1,
                "EnableOut": 0,
                "p0": 0,
                "p1": 0,
                "p2": 0,
                "p3": 0,
                "p4": 1,
                "p5": 0,
                "p6": 0,
                "p7": 0,
                "p8": 0,
                "pdint": 42,
                "t9": 1,
                "t10": 0,
                "t11": 0,
                "t12": 0,
                "t13": 0,
                "t14": 0,
                "t15": 0,
                "t16": 0,
                "t17": 1,
                "t18": 0,
                "t19": 0,
                "t20": 0,
                "t21": 0,
                "t22": 0,
                "t23": 0,
                "t24": 0,
                "t25": 0,
                "t26": 0,
                "t27": 1,
                "t28": 0,
                "t29": 0,
                "t30": 0,
                "t31": 0,
                "tdint": 99,
            },
            ctl.tags["tag"].value,
        )

    def test_bool_array(self):
        """Confirm BOOL array values are correctly extracted.

        Explicitly testing a BOOL array is intended to verify the array
        isn't subject to bit packing like individual BOOL tags.
        """
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
            PARAMETERS
	    EnableIn : BOOL (Usage := Input);
	    EnableOut : BOOL (Usage := Output);
            END_PARAMETERS
	    LOCAL_TAGS
	    array : BOOL[3];
	    END_LOCAL_TAGS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG
            tag : aoi := [0,[2#1,2#0,2#0]];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            {
                "EnableIn": 0,
                "EnableOut": 0,
                "array": [1, 0, 0],
            },
            ctl.tags["tag"].value,
        )


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

    def test_array_of_aoi(self):
        """Confirm value of an array of AOIs."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
            PARAMETERS
            EnableIn : BOOL (Usage := Input);
            EnableOut : BOOL (Usage := Output);
            END_PARAMETERS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG
            tag : aoi[2] := [[1],[2]];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            [
                {
                    "EnableIn": 1,
                    "EnableOut": 0,
                },
                {
                    "EnableIn": 0,
                    "EnableOut": 1,
                },
            ],
            ctl.tags["tag"].value,
        )

    def test_udt_aoi_member(self):
        """Confirm value of a UDT with an AOI member."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            DATATYPE udt (FamilyType := NoFamily)
            aoi aoimember;
            END_DATATYPE
            ADD_ON_INSTRUCTION_DEFINITION aoi
            PARAMETERS
            EnableIn : BOOL (Usage := Input);
            EnableOut : BOOL (Usage := Output);
            END_PARAMETERS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG
            tag : udt := [[1]];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            {"aoimember": {"EnableIn": 1, "EnableOut": 0}},
            ctl.tags["tag"].value,
        )

    def test_aoi_array_local_tag(self):
        """Confirm value of an AOI with an array local tag."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
            PARAMETERS
            EnableIn : BOOL (Usage := Input);
            EnableOut : BOOL (Usage := Output);
            END_PARAMETERS
            LOCAL_TAGS
            arraymember : DINT[3];
            END_LOCAL_TAGS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG
            tag : aoi := [1,[42,43,44]];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            {
                "EnableIn": 1,
                "EnableOut": 0,
                "arraymember": [42, 43, 44],
            },
            ctl.tags["tag"].value,
        )

    def test_aoi_udt_local_tag(self):
        """Confirm value of an AOI with a UDT local tag."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            DATATYPE udt (FamilyType := NoFamily)
            DINT m1;
            END_DATATYPE
            ADD_ON_INSTRUCTION_DEFINITION aoi
            PARAMETERS
            EnableIn : BOOL (Usage := Input);
            EnableOut : BOOL (Usage := Output);
            END_PARAMETERS
            LOCAL_TAGS
            udtmember : udt;
            END_LOCAL_TAGS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG
            tag : aoi := [2,[42]];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            {
                "EnableIn": 0,
                "EnableOut": 1,
                "udtmember": {"m1": 42},
            },
            ctl.tags["tag"].value,
        )

    def test_nested_aoi(self):
        """Confirm value of an AOI with an AOI local tag."""
        ctl = common.parse(
            """
            CONTROLLER ctl

            ADD_ON_INSTRUCTION_DEFINITION inner
            PARAMETERS
            EnableIn : BOOL (Usage := Input);
            EnableOut : BOOL (Usage := Output);
            END_PARAMETERS
            END_ADD_ON_INSTRUCTION_DEFINITION

            ADD_ON_INSTRUCTION_DEFINITION outer
            PARAMETERS
            EnableIn : BOOL (Usage := Input);
            EnableOut : BOOL (Usage := Output);
            END_PARAMETERS
            LOCAL_TAGS
            aoimember : inner;
            END_LOCAL_TAGS
            END_ADD_ON_INSTRUCTION_DEFINITION

            TAG
            tag : outer := [1,[2]];
            END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            {
                "EnableIn": 1,
                "EnableOut": 0,
                "aoimember": {"EnableIn": 0, "EnableOut": 1},
            },
            ctl.tags["tag"].value,
        )


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
