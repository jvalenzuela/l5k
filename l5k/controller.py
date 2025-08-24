"""Storage representation of the top-level Controller component."""

import dataclasses


@dataclasses.dataclass
class Controller:
    """Storage object for the top-level Controller component."""

    name: str
    attributes: dict
    datatypes: dict
    tags: dict

    def __post_init__(self):
        # Tag values are converted after initialization because
        # data type definions are now available.
        self._convert_tag_values()

    def _convert_tag_values(self):
        """Converts tag values across all scopes."""
        for t in self.tags.values():
            t.convert_value(self.datatypes)


def convert(tokens):
    """Converts the parser tokens into a Controller object."""
    return Controller(
        tokens["name"],
        tokens["attributes"][0],
        datatypes=tokens["datatypes"][0],
        tags=tokens["tags"][0],
    )
