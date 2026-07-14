from pydantic import BaseModel


class DocumentCreate(BaseModel):
    filename: str
    file_type: str
    file_path: str
    uploaded_by: str