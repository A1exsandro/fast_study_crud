from fastapi import APIRouter, Path, Query


from app.repository.TipoEquipamentoRepository import TipoEquipamentoRepository
from app.schema.TipoEquipamentoSchema import ResponseSchema, TipoEquipamentoCreate


router = APIRouter(
    prefix="/tipo_equipamento",
    tags=['tipo_equipamento']
)

# CREATE
@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_tipo_equipamento(
        create_form: TipoEquipamentoCreate
):
    await TipoEquipamentoRepository.create(create_form)
    return ResponseSchema(detail="Successfully created data !")

# GET BY ID
@router.get("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_tipo_equipamento_by_id(
        tipo_equipamento_id: int = Path(..., alias="id")
):
    result = await TipoEquipamentoRepository.get_by_id(tipo_equipamento_id)
    return ResponseSchema(detail="Successfully fetch person data by id !", result=result)

# UPDATE
@router.patch("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_tipo_equipamento(
        tipo_equipamento_id: int = Path(..., alias="id"),
        *,
        update_form: TipoEquipamentoCreate
):
    await TipoEquipamentoRepository.update(tipo_equipamento_id, update_form)
    return ResponseSchema(detail="Successfully updated data !")

# DELETE
@router.delete("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_tipo_equipamento(
        tipo_equipamento_id: int = Path(..., alias="id"),
):
    await TipoEquipamentoRepository.delete(tipo_equipamento_id)
    return ResponseSchema(detail="Successfully deleted data !")

# READ
@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_tipo_equipamento(
        page: int = 1,
        limit: int = 10,
        columns: str = Query(None, alias="columns"),
        sort: str = Query(None, alias="sort"),
        filter: str = Query(None, alias="filter"),
):
    result = await TipoEquipamentoRepository.get_all(page, limit, columns, sort, filter)
    return ResponseSchema(detail="Successfully fetch person data by id !", result=result)
