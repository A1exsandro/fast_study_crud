from fastapi import APIRouter


from app.repository import TipoEquipamentoRepository


router = APIRouter(
    prefix="/tipo_equipamento",
    tags=['tipo_equipamento']
)


