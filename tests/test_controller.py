"""Unit tests for the controller storage object."""

import unittest

from . import common


class Name(unittest.TestCase):
    """Tests for the controller name string."""

    def test_name(self):
        """Confirm controller name is stored."""
        data = r"""
        CONTROLLER foo_bar
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual("foo_bar", ctl.name)


class Attributes(unittest.TestCase):
    """Tests for the attributes dictionary."""

    def test_attributes(self):
        """Confirm controller attributes are stored.."""
        data = r"""
        CONTROLLER foo (spam := eggs)
        TAG END_TAG
        END_CONTROLLER
        """
        ctl = common.parse(data)
        self.assertEqual({"spam": "eggs"}, ctl.attributes)


class AddOnInstructions(unittest.TestCase):
    """Tests for the aois dictionary."""

    def test_no_aois(self):
        """Confirm default value if no AOIs are defined."""
        ctl = common.parse(
            """
            CONTROLLER foo
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({}, ctl.aois)

    def test_encoded(self):
        """Confirm encoded AOIs are excluded."""
        ctl = common.parse(
            """
            CONTROLLER foo
            ENCODED_DATA (EncodedType := ADD_ON_INSTRUCTION_DEFINITION,
            Name := "Conveyor_Control")
            foo_bar
            END_ENCODED_DATA
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({}, ctl.aois)


class Tags(unittest.TestCase):
    """Tests for the tags attribute."""

    def test_no_tags(self):
        """Confirm default value if no tags were defined."""
        ctl = common.parse(
            r"""
            CONTROLLER foo
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({}, ctl.tags)


class Programs(unittest.TestCase):
    """Tests for the programs attribute."""

    def test_no_programs(self):
        """Confirm default value if no programs exist."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG END_TAG
            END_CONTROLLER
            """
        )
        self.assertEqual({}, ctl.programs)
