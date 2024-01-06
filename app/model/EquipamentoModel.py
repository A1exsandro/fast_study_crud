from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship

from .TipoEquipamentoModel import TipoEquipamento
from .MarcaModel import Marca
from .ModeloModel import Modelo
from .SistemaOperacionalModel import SistemaOperacional


# class Equipamento(SQLModel, table=True):
#     __tablename__ = "equipamento"

#     id: Optional[int] = Field(None, primary_key=True, nullable=False)
    # created_at
    # updated_at
    # status

    # numero_patrimonio
    # numero_contrato
    # numero_serie
    # numero_requisicao
    
    # tipo_equipamento_id
    # marca_id
    # modelo_id
    # sistema_operacional_id
    # user_id                         # falta add
    # termo_entrega_id                # falta add

class Equipamento(SQLModel, table=True):
    __tablename__ = "equipamento"

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    updated_at: Optional[datetime] = Field(default=None, nullable=True)
    status: str = Field(max_length=50)

    numero_patrimonio: Optional[str] = Field(max_length=50, nullable=True, unique=True)
    numero_serie: str = Field(max_length=50, nullable=True, unique=True)
    numero_contrato: str = Field(max_length=50, nullable=True)
    numero_requisicao: Optional[str] = Field(max_length=50, nullable=True)

    tipo_equipamento_id: Optional[int] = Field(default=None, foreign_key="tipo_equipamento.id", nullable=True)
    tipo_equipamento: Optional["TipoEquipamento"] = Relationship(back_populates="equipamentos")

    marca_id: Optional[int] = Field(default=None, foreign_key="marca.id", nullable=True)
    marca: Optional["Marca"] = Relationship(back_populates="equipamentos")

    modelo_id: Optional[int] = Field(default=None, foreign_key="modelo.id", nullable=True)
    modelo: Optional["Modelo"] = Relationship(back_populates="equipamentos")

    sistema_operacional_id: Optional[int] = Field(default=None, foreign_key="sistema_operacional.id", nullable=True)
    sistema_operacional: Optional["SistemaOperacional"] = Relationship(back_populates="equipamentos")

    # termo_entrega: Optional["TermoEntrega"] = Relationship(back_populates="equipamentos")
    # termo_entrega_cod_entrega: Optional[int] = Field(default=None, foreign_key="TermoEntrega.cod_entrega", nullable=True)

    # user: Optional["User"] = Relationship(back_populates="cadastros")
    # user_id: Optional[int] = Field(default=None, foreign_key="User.cod_policial")
