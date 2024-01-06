from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class TipoEquipamento(SQLModel, table=True):
    __tablename__ = "tipo_equipamento"

    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    nome: str = Field(unique=True)
    equipamentos: List["Equipamento"] = Relationship(back_populates="tipo_equipamento")