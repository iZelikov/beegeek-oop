from dataclasses import dataclass, field


@dataclass
class City:
    name: str
    population: int
    founded: int


@dataclass(frozen=True)
class MusicAlbum:
    title: str
    artist: str
    genre: str = field(repr=False, compare=False)
    year: int = field(repr=False)


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0

    def __post_init__(self):
        if self.x == 0 or self.y == 0:
            self.quadrant = 0
        elif self.x > 0 and self.y > 0:
            self.quadrant = 1
        elif self.x < 0 and self.y > 0:
            self.quadrant = 2
        elif self.x < 0 and self.y < 0:
            self.quadrant = 3
        else:
            self.quadrant = 4

    def symmetric_y(self):
        return Point(-self.x, self.y)

    def symmetric_x(self):
        return Point(self.x, -self.y)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, quadrant={self.quadrant})"


@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)


@dataclass
class FootballTeam:
    name: str
    players: list[FootballPlayer] = field(
        default_factory=list,
        repr=False,
        compare=False
    )

    def add_players(self, *players):
        self.players.extend(players)
