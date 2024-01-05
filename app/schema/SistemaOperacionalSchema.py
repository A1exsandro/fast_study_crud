from typing import Optional, TypeVar, Generic, List

from fastapi import HTTPException
from pydantic import BaseModel
from pydantic.generics import GenericModel


T = TypeVar('T')


class SistemaOperacionalCreate(BaseModel):
    nome: str


class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None


class PageResponse(GenericModel, Generic[T]):
    """ The response for a pagination query. """

    page_number: int
    page_size: int
    total_pages: int
    total_record: int
    content: List[T]
