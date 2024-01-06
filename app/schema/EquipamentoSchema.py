from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

class EquipamentoCreate(BaseModel):
    status: str
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None
    numero_patrimonio: Optional[str] = None
    numero_serie: str
    numero_contrato: str
    numero_requisicao: Optional[str] = None
    tipo_equipamento_id: Optional[int] = None
    marca_id: Optional[int] = None
    modelo_id: Optional[int] = None
    sistema_operacional_id: Optional[int] = None

class EquipamentoUpdate(BaseModel):
    status: str
    numero_patrimonio: Optional[str] = None
    numero_serie: str
    numero_contrato: str
    numero_requisicao: Optional[str] = None
    tipo_equipamento_id: Optional[int] = None
    marca_id: Optional[int] = None
    modelo_id: Optional[int] = None
    sistema_operacional_id: Optional[int] = None

class EquipamentoResponse(BaseModel):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    status: str
    numero_patrimonio: Optional[str] = None
    numero_serie: str
    numero_contrato: str
    numero_requisicao: Optional[str] = None
    tipo_equipamento_id: Optional[int] = None
    marca_id: Optional[int] = None
    modelo_id: Optional[int] = None
    sistema_operacional_id: Optional[int] = None

class EquipamentoListResponse(BaseModel):
    content: List[EquipamentoResponse]

class EquipamentoPaginationResponse(BaseModel):
    page_number: int
    page_size: int
    total_pages: int
    total_record: int
    content: List[EquipamentoCreate]
