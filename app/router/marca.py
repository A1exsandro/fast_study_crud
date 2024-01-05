from fastapi import APIRouter, Path, Query


from app.repository.MarcaRepository import MarcaRepository
from app.schema.MarcaSchema import ResponseSchema, MarcaCreate


router = APIRouter(
    prefix="/marca",
    tags=['marca']
)

# CREATE
@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_marca(
        create_form: MarcaCreate
):
    await MarcaRepository.create(create_form)
    return ResponseSchema(detail="Successfully created data !")

# GET BY ID
@router.get("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_marca_by_id(
        marca_id: int = Path(..., alias="id")
):
    result = await MarcaRepository.get_by_id(marca_id)
    return ResponseSchema(detail="Successfully fetch person data by id !", result=result)

# UPDATE
@router.patch("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_marca(
        marca_id: int = Path(..., alias="id"),
        *,
        update_form: MarcaCreate
):
    await MarcaRepository.update(marca_id, update_form)
    return ResponseSchema(detail="Successfully updated data !")

# DELETE
@router.delete("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_marca(
        marca_id: int = Path(..., alias="id"),
):
    await MarcaRepository.delete(marca_id)
    return ResponseSchema(detail="Successfully deleted data !")

# READ
@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_marca(
        page: int = 1,
        limit: int = 10,
        columns: str = Query(None, alias="columns"),
        sort: str = Query(None, alias="sort"),
        filter: str = Query(None, alias="filter"),
):
    result = await MarcaRepository.get_all(page, limit, columns, sort, filter)
    return ResponseSchema(detail="Successfully fetch person data by id !", result=result)
