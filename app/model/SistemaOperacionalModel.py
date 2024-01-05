from typing import Optional

from sqlmodel import SQLModel, Field


class SistemaOperacional(SQLModel, table=True):
    __tablename__ = "sistema_operacional"

    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    nome: str = Field(unique=True)
    