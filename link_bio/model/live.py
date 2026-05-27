from dataclasses import dataclass

@dataclass
class Live:
    live: bool
    title: str | None
    user: str

