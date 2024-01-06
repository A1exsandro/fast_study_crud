from fastapi import APIRouter, Path, Query

from app.repository.EquipamentoRepository import EquipamentoRepository
from app.schema.EquipamentoSchema import EquipamentoCreate, EquipamentoUpdate, EquipamentoResponse, EquipamentoPaginationResponse

router = APIRouter(
    prefix="/equipamento",
    tags=['equipamento']
)

# CREATE
@router.post("", response_model=EquipamentoResponse, response_model_exclude_none=True)
async def create_equipamento(create_form: EquipamentoCreate):
    await EquipamentoRepository.create(create_form)
    return EquipamentoResponse(detail="Successfully created data!")

# GET BY ID
@router.get("/{id}", response_model=EquipamentoResponse, response_model_exclude_none=True)
async def get_equipamento_by_id(equipamento_id: int = Path(..., alias="id")):
    result = await EquipamentoRepository.get_by_id(equipamento_id)
    return EquipamentoResponse(detail="Successfully fetch data by id!", result=result)

# UPDATE
@router.patch("/{id}", response_model=EquipamentoResponse, response_model_exclude_none=True)
async def update_equipamento(
        equipamento_id: int = Path(..., alias="id"),
        *,
        update_form: EquipamentoUpdate
):
    await EquipamentoRepository.update(equipamento_id, update_form)
    return EquipamentoResponse(detail="Successfully updated data!")

# DELETE
@router.delete("/{id}", response_model=EquipamentoResponse, response_model_exclude_none=True)
async def delete_equipamento(
        equipamento_id: int = Path(..., alias="id"),
):
    await EquipamentoRepository.delete(equipamento_id)
    return EquipamentoResponse(detail="Successfully deleted data!")

# READ
@router.get("", response_model=EquipamentoResponse, response_model_exclude_none=True)
async def get_all_equipamentos(
        page: int = 1,
        limit: int = 10,
        columns: str = Query(None, alias="columns"),
        sort: str = Query(None, alias="sort"),
        filter: str = Query(None, alias="filter"),
):
    result = await EquipamentoRepository.get_all(page, limit, columns, sort, filter)
    return EquipamentoResponse(detail="Successfully fetch data by id!", result=result)
