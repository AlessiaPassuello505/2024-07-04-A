from dataclasses import dataclass

from model.sighting import Sighting


@dataclass
class Arco:
    a1:Sighting
    a2:Sighting