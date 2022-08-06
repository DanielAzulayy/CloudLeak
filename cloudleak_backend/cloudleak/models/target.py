from datetime import datetime
from platform import platform
from typing import List, Optional, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field

from .objectid import PydanticObjectId


class Bucket(BaseModel):
    ...


class Scan(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    target: str
    platform: str
    added_ts: Optional[datetime]
    finished_ts: Optional[datetime]
    # buckets: List[Bucket]

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data
