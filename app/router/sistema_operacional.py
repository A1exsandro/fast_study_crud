from fastapi import APIRouter, Path, Query


from app.repository.SistemaOperacionalRepository import SistemaOperacionalRepository
from app.schema.SistemaOperacionalSchema import ResponseSchema, SistemaOperacionalCreate


router = APIRouter(
    prefix="/sistema_operacional",
    tags=['sistema_operacional']
)

# CREATE
@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_sistema_operacional(
        create_form: SistemaOperacionalCreate
):
    await SistemaOperacionalRepository.create(create_form)
    return ResponseSchema(detail="Successfully created data !")

# GET BY ID
@router.get("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_sistema_operacional_by_id(
        sistema_operacional_id: int = Path(..., alias="id")
):
    result = await SistemaOperacionalRepository.get_by_id(sistema_operacional_id)
    return ResponseSchema(detail="Successfully fetch person data by id !", result=result)

# UPDATE
@router.patch("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_sistema_operacional(
        sistema_operacional_id: int = Path(..., alias="id"),
        *,
        update_form: SistemaOperacionalCreate
):
    await SistemaOperacionalRepository.update(sistema_operacional_id, update_form)
    return ResponseSchema(detail="Successfully updated data !")

# DELETE
@router.delete("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_sistema_operacional(
        sistema_operacional_id: int = Path(..., alias="id"),
):
    await SistemaOperacionalRepository.delete(sistema_operacional_id)
    return ResponseSchema(detail="Successfully deleted data !")

# READ
@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_sistema_operacional(
        page: int = 1,
        limit: int = 10,
        columns: str = Query(None, alias="columns"),
        sort: str = Query(None, alias="sort"),
        filter: str = Query(None, alias="filter"),
):
    result = await SistemaOperacionalRepository.get_all(page, limit, columns, sort, filter)
    return ResponseSchema(detail="Successfully fetch person data by id !", result=result)
