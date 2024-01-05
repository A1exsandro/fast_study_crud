from typing import Optional

from sqlmodel import SQLModel, Field


class Marca(SQLModel, table=True):
    __tablename__ = "marca"

    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    nome: str = Field(unique=True)
    