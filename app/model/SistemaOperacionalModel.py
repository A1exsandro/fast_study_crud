from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class SistemaOperacional(SQLModel, table=True):
    __tablename__ = "sistema_operacional"

    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    nome: str = Field(unique=True)
    equipamentos: List["Equipamento"] = Relationship(back_populates="sistema_operacional")
    