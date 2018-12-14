from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class UserId:
    value: str

@dataclass(frozen=True)
class Username:
    value: str

@dataclass(frozen=True)
class FullName:
    first_name: str
    family_name: str

@dataclass
class User:
    id: UserId
    username: Username
    name: FullName
