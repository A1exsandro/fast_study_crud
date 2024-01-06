import math

from sqlalchemy import update, delete, or_, text, func, column
from sqlalchemy.sql import select
from typing import Optional, List

from app.config import db, commit_rollback
from app.model.EquipamentoModel import Equipamento
from app.schema.EquipamentoSchema import EquipamentoCreate, EquipamentoUpdate, EquipamentoResponse, EquipamentoPaginationResponse


class EquipamentoRepository:

    # CREATE
    @staticmethod
    async def create(create_form: EquipamentoCreate):
        equipamento_data = create_form.dict()
        db.add(Equipamento(**equipamento_data))
        await commit_rollback()

    # GET BY ID
    @staticmethod
    async def get_by_id(equipamento_id: int) -> Optional[EquipamentoResponse]:
        query = select(Equipamento).where(Equipamento.id == equipamento_id)
        equipamento = (await db.execute(query)).scalar_one_or_none()
        return EquipamentoResponse(**equipamento.dict()) if equipamento else None

    # UPDATE
    @staticmethod
    async def update(equipamento_id: int, update_form: EquipamentoUpdate) -> Optional[EquipamentoResponse]:
        query = update(Equipamento).where(Equipamento.id == equipamento_id).values(**update_form.dict()).execution_options(synchronize_session="fetch")
        await db.execute(query)
        await commit_rollback()

        return await EquipamentoRepository.get_by_id(equipamento_id)

    # DELETE
    @staticmethod
    async def delete(equipamento_id: int) -> bool:
        query = delete(Equipamento).where(Equipamento.id == equipamento_id)
        await db.execute(query)
        await commit_rollback()
        return True

    # READ
    @staticmethod
    async def get_all(
            page: int = 1,
            limit: int = 10,
            columns: str = None,
            sort: str = None,
            filter: str = None
    ) -> EquipamentoPaginationResponse:
        query = select(Equipamento)

        # Select columns dynamically
        if columns and columns != "all":
            query = select(convert_columns(columns)).from_statement(text("FROM equipamento"))

        # Select filter dynamically
        if filter and filter != "null":
            criteria = dict(x.split("*") for x in filter.split('-'))
            criteria_list = [getattr(Equipamento, attr).ilike(f"%{value}%") for attr, value in criteria.items()]
            query = query.filter(or_(*criteria_list))

        # Select sort dynamically
        if sort and sort != "null":
            query = query.order_by(text(convert_sort(sort)))

        # Count query
        count_query = select(func.count(1)).select_from(query)

        offset_page = page - 1
        # Pagination
        query = query.offset(offset_page * limit).limit(limit)

        # Total record
        total_record = (await db.execute(count_query)).scalar() or 0

        # Total page
        total_page = math.ceil(total_record / limit)

        # Result
        result = (await db.execute(query)).fetchall()

        print('...............:', result)

        return EquipamentoPaginationResponse(
            page_number=page,
            page_size=limit,
            total_pages=total_page,
            total_record=total_record,
            content=result
        )


def convert_sort(sort: str) -> str:
    return ','.join(sort.split('-'))


def convert_columns(columns: str) -> List[column]:
    return [column(column_name) for column_name in columns.split('-')]
