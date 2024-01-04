import math

from sqlalchemy import update, delete, or_, text, func, column
from sqlalchemy.sql import select

from app.config import db, commit_rollback
from app.model.TipoEquipamentoModel import TipoEquipamento
from app.schema.TipoEquipamentoSchema import TipoEquipamentoCreate, PageResponse


class TipoEquipamentoRepository:

    # CREATE
    @staticmethod
    async def create(create_form: TipoEquipamentoCreate):
        nome_upcase = create_form.nome.upper()
        db.add(TipoEquipamento(nome=nome_upcase))
        await commit_rollback()
