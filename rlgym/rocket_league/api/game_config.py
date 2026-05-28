from dataclasses import dataclass

from .utils import create_default_init


@dataclass(init=False)
class GameConfig:
    gravity: float
    boost_consumption: float
    dodge_deadzone: float  # TODO move to car?

    __slots__ = ("gravity", "boost_consumption", "dodge_deadzone")

    exec(create_default_init(__slots__))
