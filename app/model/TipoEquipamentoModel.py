from typing import Optional

from sqlmodel import SQLModel, Field


class TipoEquipamento(SQLModel, table=True):
    __tablename__ = "tipo_equipamento"

    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    nome: str = Field(unique=True)
    