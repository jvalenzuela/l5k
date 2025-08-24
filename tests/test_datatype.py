"""Unit tests for user-defined data type definitions."""

import unittest

from . import common


class ControllerAttribute(unittest.TestCase):
    """Tests for the datatypes attribute in the top-level controller."""

    def test_no_data_types(self):
        """Confirm default value if no DATATYPE components exist."""
        data = r"""
        CONTROLLER foo
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual({}, ctl.datatypes)

    def test_data_types(self):
        """Confirm data types are stored correctly."""
        data = r"""
        CONTROLLER ctl
        DATATYPE foo
        INT bar;
        END_DATATYPE
        DATATYPE spam
        BOOL eggs;
        END_DATATYPE
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual("INT", ctl.datatypes["foo"].members["bar"].datatype)
        self.assertEqual("BOOL", ctl.datatypes["spam"].members["eggs"].datatype)


class DataType(unittest.TestCase):
    """Tests for storage of a single data type."""

    def test_member_order(self):
        """Confirm members are stored in original order."""
        data = r"""
        CONTROLLER ctl
        DATATYPE myType
        INT foo;
        INT bar;
        INT spam;
        INT eggs;
        END_DATATYPE
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual(
            [
                "foo",
                "bar",
                "spam",
                "eggs",
            ],
            list(ctl.datatypes["myType"].members.keys()),
        )

    def test_attributes(self):
        """Confirm attributes are stored correctly."""
        data = r"""
        CONTROLLER ctl
        DATATYPE myType (spam := eggs)
        INT foo;
        END_DATATYPE
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual({"spam": "eggs"}, ctl.datatypes["myType"].attributes)

    def test_default_attributes(self):
        """Confirm default attributes if none exist."""
        data = r"""
        CONTROLLER ctl
        DATATYPE myType
        INT foo;
        END_DATATYPE
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual({}, ctl.datatypes["myType"].attributes)


class Member(unittest.TestCase):
    """Tests for normal(non-bit) member storage."""

    def test_datatype(self):
        """Confirm data type is stored correctly."""
        data = r"""
        CONTROLLER ctl
        DATATYPE myType
        foo member;
        END_DATATYPE
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual("foo", ctl.datatypes["myType"].members["member"].datatype)

    def test_dim(self):
        """Confirm array dimensions are stored correctly."""
        data = r"""
        CONTROLLER ctl
        DATATYPE myType
        foo member[42,99];
        END_DATATYPE
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual((99, 42), ctl.datatypes["myType"].members["member"].dim)

    def test_default_dim(self):
        """Confirm default value if no array dimensions exist."""
        data = r"""
        CONTROLLER ctl
        DATATYPE myType
        foo member;
        END_DATATYPE
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertIsNone(ctl.datatypes["myType"].members["member"].dim)

    def test_attributes(self):
        """Confirm attributes are stored correctly."""
        data = r"""
        CONTROLLER ctl
        DATATYPE myType
        foo member (spam := eggs);
        END_DATATYPE
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual(
            {"spam": "eggs"}, ctl.datatypes["myType"].members["member"].attributes
        )

    def test_default_attributes(self):
        """Confirm default attributes if none exist."""
        data = r"""
        CONTROLLER ctl
        DATATYPE myType
        foo member;
        END_DATATYPE
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual({}, ctl.datatypes["myType"].members["member"].attributes)


class BitMember(unittest.TestCase):
    """Tests for bit member storage."""

    def test_target(self):
        """Confirm target name is stored correctly."""
        data = r"""
        CONTROLLER ctl
        DATATYPE myType
        BIT bitName foo : 0;
        END_DATATYPE
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual("foo", ctl.datatypes["myType"].members["bitName"].target)

    def test_bit(self):
        """Confirm bit number is stored correctly."""
        data = r"""
        CONTROLLER ctl
        DATATYPE myType
        BIT bitName foo : 5;
        END_DATATYPE
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual(5, ctl.datatypes["myType"].members["bitName"].bit)

    def test_attributes(self):
        """Confirm attributes are stored correctly."""
        data = r"""
        CONTROLLER ctl
        DATATYPE myType
        BIT bitName foo : 5 (spam := eggs);
        END_DATATYPE
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual(
            {"spam": "eggs"}, ctl.datatypes["myType"].members["bitName"].attributes
        )

    def test_default_attributes(self):
        """Confirm default attributes if none exist."""
        data = r"""
        CONTROLLER ctl
        DATATYPE myType
        BIT bitName foo : 5;
        END_DATATYPE
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual({}, ctl.datatypes["myType"].members["bitName"].attributes)
