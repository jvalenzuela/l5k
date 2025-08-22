"""Storage representation of the top-level Controller component."""

import dataclasses


@dataclasses.dataclass
class Controller:
    """Storage object for the top-level Controller component."""

    name: str
    attributes: dict


def convert(tokens):
    """Converts the parser tokens into a Controller object."""
    return Controller(
        tokens["name"],
        tokens["attributes"][0],
    )
