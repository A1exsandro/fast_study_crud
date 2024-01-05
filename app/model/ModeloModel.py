from typing import Optional

from sqlmodel import SQLModel, Field


class Modelo(SQLModel, table=True):
    __tablename__ = "modelo"

    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    nome: str = Field(unique=True)
    