"""Unit tests for add-on instruction storage objects."""

import unittest

from . import common


class Attributes(unittest.TestCase):
    """Tests for the attributes dictionary."""

    def test_attribute(self):
        """Confirm attributes are stored correctly."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION foo (spam := eggs)
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({"spam": "eggs"}, ctl.aois["foo"].attributes)

    def test_default(self):
        """Confirm default value if no attributes are present."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION foo
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({}, ctl.aois["foo"].attributes)


class Parameters(unittest.TestCase):
    """Tests for the parameters attribute."""

    def test_datatype(self):
        """Confirm data type is stored correctly."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
		PARAMETERS
                param : BOOL;
		END_PARAMETERS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual("BOOL", ctl.aois["aoi"].parameters["param"].datatype)

    def test_dim(self):
        """Confirm array dimensions are stored correctly."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
		PARAMETERS
                param : DINT[1,2,3];
		END_PARAMETERS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual((3, 2, 1), ctl.aois["aoi"].parameters["param"].dim)

    def test_default_dim(self):
        """Confirm default value if no array dimensions exist."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
		PARAMETERS
                param : DINT;
		END_PARAMETERS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertIsNone(ctl.aois["aoi"].parameters["param"].dim)

    def test_attributes(self):
        """Confirm attributes are stored correctly."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
		PARAMETERS
                param : DINT (spam := eggs);
		END_PARAMETERS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            {"spam": "eggs"},
            ctl.aois["aoi"].parameters["param"].attributes,
        )

    def test_default_attributes(self):
        """Confirm default attributes if none exist."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
		PARAMETERS
                param : DINT;
		END_PARAMETERS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({}, ctl.aois["aoi"].parameters["param"].attributes)

    def test_order(self):
        """Confirm parameters are stored in the order they are defined."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION aoi
		PARAMETERS
                spam : DINT;
                bar : DINT;
                foo : DINT;
                eggs : DINT;
		END_PARAMETERS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            ["spam", "bar", "foo", "eggs"],
            list(ctl.aois["aoi"].parameters.keys()),
        )


class LocalTags(unittest.TestCase):
    """Tests for the local_tags attribute."""

    def test_default(self):
        """Confirm default value if no local tags are defined"""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION foo
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({}, ctl.aois["foo"].local_tags)

    def test_datatype(self):
        """Confirm data type is stored correctly."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION foo
            LOCAL_TAGS
            tag : DINT;
            END_LOCAL_TAGS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual("DINT", ctl.aois["foo"].local_tags["tag"].datatype)

    def test_dim(self):
        """Confirm array dimensions are stored correctly."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION foo
            LOCAL_TAGS
            tag : DINT[42];
            END_LOCAL_TAGS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual((42,), ctl.aois["foo"].local_tags["tag"].dim)

    def test_default_dim(self):
        """Confirm default value if no array dimensions exist."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION foo
            LOCAL_TAGS
            tag : DINT;
            END_LOCAL_TAGS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertIsNone(ctl.aois["foo"].local_tags["tag"].dim)

    def test_attributes(self):
        """Confirm attributes are stored correctly."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION foo
            LOCAL_TAGS
            tag : DINT (spam := eggs);
            END_LOCAL_TAGS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            {"spam": "eggs"},
            ctl.aois["foo"].local_tags["tag"].attributes,
        )

    def test_default_attributes(self):
        """Confirm default attributes if none exist."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION foo
            LOCAL_TAGS
            tag : DINT;
            END_LOCAL_TAGS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({}, ctl.aois["foo"].local_tags["tag"].attributes)

    def test_order(self):
        """Confirm tags are stored in the order they are defined."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            ADD_ON_INSTRUCTION_DEFINITION foo
            LOCAL_TAGS
            t6 : DINT;
            t1 : DINT;
            t99 : DINT;
            t42 : DINT;
            END_LOCAL_TAGS
            END_ADD_ON_INSTRUCTION_DEFINITION
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual(
            ["t6", "t1", "t99", "t42"], list(ctl.aois["foo"].local_tags.keys())
        )
