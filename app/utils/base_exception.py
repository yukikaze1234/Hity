from typing import Any

from fastapi import HTTPException






class BaseException(HTTPException):
    def __init__(self,detail:Any =None)->None:
        super().__init__(status_code=200,detail=detail)