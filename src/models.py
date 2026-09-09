from typing import List, Optional
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorites: Mapped[List["Favorite"]] = relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
        }


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    population: Mapped[Optional[str]] = mapped_column(String(50))
    climate: Mapped[Optional[str]] = mapped_column(String(120))
    terrain: Mapped[Optional[str]] = mapped_column(String(120))
    diameter: Mapped[Optional[str]] = mapped_column(String(50))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "diameter": self.diameter
        }


class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    gender: Mapped[Optional[str]] = mapped_column(String(50))
    height: Mapped[Optional[str]] = mapped_column(String(50))
    eye_color: Mapped[Optional[str]] = mapped_column(String(50))
    birth_year: Mapped[Optional[str]] = mapped_column(String(50))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year
        }


class Favorite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    people_id: Mapped[Optional[int]] = mapped_column(ForeignKey("people.id"))
    user: Mapped["User"] = relationship(back_populates="favorites")
    planet: Mapped[Optional["Planet"]] = relationship()
    people: Mapped[Optional["People"]] = relationship()

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "people_id": self.people_id,
            "planet": self.planet.serialize() if self.planet else None,
            "people": self.people.serialize() if self.people else None
        }