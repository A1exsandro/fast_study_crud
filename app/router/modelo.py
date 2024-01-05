from fastapi import APIRouter, Path, Query


from app.repository.ModeloRepository import ModeloRepository
from app.schema.ModeloSchema import ResponseSchema, ModeloCreate


router = APIRouter(
    prefix="/modelo",
    tags=['modelo']
)

# CREATE
@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_modelo(
        create_form: ModeloCreate
):
    await ModeloRepository.create(create_form)
    return ResponseSchema(detail="Successfully created data !")

# GET BY ID
@router.get("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_modelo_by_id(
        modelo_id: int = Path(..., alias="id")
):
    result = await ModeloRepository.get_by_id(modelo_id)
    return ResponseSchema(detail="Successfully fetch person data by id !", result=result)

# UPDATE
@router.patch("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_Modelo(
        modelo_id: int = Path(..., alias="id"),
        *,
        update_form: ModeloCreate
):
    await ModeloRepository.update(modelo_id, update_form)
    return ResponseSchema(detail="Successfully updated data !")

# DELETE
@router.delete("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_Modelo(
        modelo_id: int = Path(..., alias="id"),
):
    await ModeloRepository.delete(modelo_id)
    return ResponseSchema(detail="Successfully deleted data !")

# READ
@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_Modelo(
        page: int = 1,
        limit: int = 10,
        columns: str = Query(None, alias="columns"),
        sort: str = Query(None, alias="sort"),
        filter: str = Query(None, alias="filter"),
):
    result = await ModeloRepository.get_all(page, limit, columns, sort, filter)
    return ResponseSchema(detail="Successfully fetch person data by id !", result=result)
