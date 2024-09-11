from pydantic import BaseModel, Field
from .constants import Const

class Config(BaseModel):
    model: str = Field(default=Const.MODEL_DEFAULT)
    lang: str = Field(default=Const.LANG_DEFAULT)
    offset: int = Field(default=Const.OFFSET_DEFAULT)
    retries: int = Field(default=Const.RETRIES_DEFAULT)
    debug: bool = Field(default=Const.DEBUG_DEFAULT)
