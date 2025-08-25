"""Unit tests for program storage objects."""

import unittest

from . import common


class Attributes(unittest.TestCase):
    """Tests for the attributes dictionary."""

    def test_default(self):
        """Confirm default value if no attributes exist."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG END_TAG
            PROGRAM prg
            END_PROGRAM
            END_CONTROLLER
            """
        )
        self.assertEqual({}, ctl.programs["prg"].attributes)

    def test_attributes(self):
        """Confirm attributes are stored."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG END_TAG
            PROGRAM prg (spam := eggs)
            END_PROGRAM
            END_CONTROLLER
            """
        )
        self.assertEqual({"spam": "eggs"}, ctl.programs["prg"].attributes)


class Tags(unittest.TestCase):
    """Tests for the tags attribute."""

    def test_no_tags(self):
        """Confirm default value if no tag section exists."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG END_TAG
            PROGRAM prg
            END_PROGRAM
            END_CONTROLLER
            """
        )
        self.assertEqual({}, ctl.programs["prg"].tags)

    def test_empty_tags(self):
        """Confirm default value if the tag section is empty."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG END_TAG
            PROGRAM prg
            TAG END_TAG
            END_PROGRAM
            END_CONTROLLER
            """
        )
        self.assertEqual({}, ctl.programs["prg"].tags)

    def test_value_conversion(self):
        """Confirm values are converted to structured form."""
        ctl = common.parse(
            """
            CONTROLLER ctl
            TAG END_TAG
            PROGRAM prg
            TAG
            t : TIMER := [0,0,0];
            END_TAG
            END_PROGRAM
            END_CONTROLLER
            """
        )
        self.assertIsInstance(ctl.programs["prg"].tags["t"].value, dict)
