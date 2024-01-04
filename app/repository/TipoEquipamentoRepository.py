import math

from sqlalchemy import update, delete, or_, text, func, column
from sqlalchemy.sql import select

from app.config import db, commit_rollback
from app.model import TipoEquipamentoModel
from app.schema.TipoEquipamentoSchema import TipoEquipamentoCreate, PageResponse


class TipoEquipamentoRepository:

    # CREATE
    @staticmethod
    async def create(create_form: TipoEquipamentoCreate):
        db.add(TipoEquipamentoModel(nome=create_form.nome))
        await commit_rollback()