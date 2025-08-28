"""Add-on instruction storage objects."""

import collections
import dataclasses


@dataclasses.dataclass
class AddOnInstruction:
    """Storage object for an add-on instruction definition."""

    attributes: dict
    parameters: collections.OrderedDict
    local_tags: collections.OrderedDict


def convert(tokens):
    """Converts parser tokens into an AOI definition object."""
    aoi = AddOnInstruction(
        attributes=tokens["attributes"][0],
        parameters=collections.OrderedDict(list(tokens["parameters"])),
        local_tags=collections.OrderedDict(list(tokens["local_tags"])),
    )

    return tokens["name"], aoi
