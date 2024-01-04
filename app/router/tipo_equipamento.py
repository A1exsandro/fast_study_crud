from fastapi import APIRouter


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

