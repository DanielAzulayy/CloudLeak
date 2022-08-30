from dataclasses import field
from datetime import datetime
from platform import platform
from typing import Optional, List

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field

from .objectid import PydanticObjectId


class Bucket(BaseModel):
    platform: str
    service: str
    bucket: str
    permission: Optional[dict]
    files: Optional[list]


class Scan(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    target: str
    platform: str
    status: Optional[int]
    added_ts: Optional[datetime]
    finished_ts: Optional[datetime]
    buckets: List[Bucket] = None

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data
