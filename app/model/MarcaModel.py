from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class Marca(SQLModel, table=True):
    __tablename__ = "marca"

    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    nome: str = Field(unique=True)
    equipamentos: List["Equipamento"] = Relationship(back_populates="marca")
