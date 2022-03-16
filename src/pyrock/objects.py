from __future__ import annotations
import typing

class Rock:
    def __init__(self, name, description, image, rating):
        self.name = name
        self.description = description
        self.desc = description
        self.image = image
        self.rating = rating

    """
    Defines a rock. This is created and returned when a user gets a rock from the API.
    """

    @classmethod
    def from_dict(cls, dict_: dict) -> Rock:
        name = dict_.get("name")
        desc = dict_.get("desc")
        image = dict_.get("image")
        rating = dict_.get("rating")

        return cls(name=name, description=desc, image=image, rating=rating)
