from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class Modelo(SQLModel, table=True):
    __tablename__ = "modelo"

    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    nome: str = Field(unique=True)
    equipamentos: List["Equipamento"] = Relationship(back_populates="modelo")
    