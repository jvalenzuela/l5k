"""Common unit test tools."""

from unittest.mock import mock_open, patch

import l5k


def parse(data):
    """
    Wrapper for the parse() function to parse a given string instead
    of a file.
    """
    # Add the mandatory version statement.
    version = "IE_VER := 0;"
    full_content = "\n".join((version, data))

    with patch("builtins.open", mock_open(read_data=full_content)):
        return l5k.parse(None)
