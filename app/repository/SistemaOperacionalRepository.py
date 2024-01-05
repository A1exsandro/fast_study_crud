import math

from sqlalchemy import update, delete, or_, text, func, column
from sqlalchemy.sql import select

from app.config import db, commit_rollback
from app.model.SistemaOperacionalModel import SistemaOperacional
from app.schema.SistemaOperacionalSchema import SistemaOperacionalCreate, PageResponse


class SistemaOperacionalRepository:

    # CREATE
    @staticmethod
    async def create(create_form: SistemaOperacionalCreate):
        nome_upcase = create_form.nome.upper()
        db.add(SistemaOperacional(nome=nome_upcase))
        await commit_rollback()

    # GET BY ID
    @staticmethod
    async def get_by_id(sistema_operacional_id: int):
        """ retrieve data by id """
        query = select(SistemaOperacional).where(SistemaOperacional.id == sistema_operacional_id)
        return (await db.execute(query)).scalar_one_or_none()
    
    # UPDATE
    @staticmethod
    async def update(sistema_operacional_id: int, update_form: SistemaOperacionalCreate):
        """ update data """

        query = update(SistemaOperacional) \
            .where(SistemaOperacional.id == sistema_operacional_id) \
            .values(**update_form.dict()) \
            .execution_options(synchronize_session="fetch")

        await db.execute(query)
        await commit_rollback()

    # DELETE
    @staticmethod
    async def delete(sistema_operacional_id: int):
        """ delete data by id """

        query = delete(SistemaOperacional).where(SistemaOperacional.id == sistema_operacional_id)
        await db.execute(query)
        await commit_rollback()

    # READ
    @staticmethod
    async def get_all(
            page: int = 1,
            limit: int = 10,
            columns: str = None,
            sort: str = None,
            filter: str = None
    ):
        query = select(from_obj=SistemaOperacional, columns="*")

        # select columns dynamically
        if columns is not None and columns != "all":
            # we need column format data like this --> [column(id),column(name),column(sex)...]

            query = select(from_obj=SistemaOperacional, columns=convert_columns(columns))

        # select filter dynamically
        if filter is not None and filter != "null":
            # we need filter format data like this  --> {'name': 'an','country':'an'}

            # convert string to dict format
            criteria = dict(x.split("*") for x in filter.split('-'))

            criteria_list = []

            # check every key in dict. are there any table attributes that are the same as the dict key ?

            for attr, value in criteria.items():
                _attr = getattr(SistemaOperacional, attr)

                # filter format
                search = "%{}%".format(value)

                # criteria list
                criteria_list.append(_attr.like(search))

            query = query.filter(or_(*criteria_list))

        # select sort dynamically
        if sort is not None and sort != "null":
            # we need sort format data like this --> ['id','name']
            query = query.order_by(text(convert_sort(sort)))

        # count query
        count_query = select(func.count(1)).select_from(query)

        offset_page = page - 1
        # pagination
        query = (query.offset(offset_page * limit).limit(limit))

        # total record
        total_record = (await db.execute(count_query)).scalar() or 0

        # total page
        total_page = math.ceil(total_record / limit)

        # result
        result = (await db.execute(query)).fetchall()

        return PageResponse(
            page_number=page,
            page_size=limit,
            total_pages=total_page,
            total_record=total_record,
            content=result
        )


def convert_sort(sort):
    """
    # separate string using split('-')
    split_sort = sort.split('-')
    # join to list with ','
    new_sort = ','.join(split_sort)
    """
    return ','.join(sort.split('-'))


def convert_columns(columns):
    """
    # seperate string using split ('-')
    new_columns = columns.split('-')

    # add to list with column format
    column_list = []
    for data in new_columns:
        column_list.append(data)

    # we use lambda function to make code simple

    """

    return list(map(lambda x: column(x), columns.split('-')))
