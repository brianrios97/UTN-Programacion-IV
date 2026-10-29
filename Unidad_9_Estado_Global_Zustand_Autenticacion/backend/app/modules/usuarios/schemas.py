from pydantic import EmailStr, Field
from sqlmodel import SQLModel


class UserBase(SQLModel):
    username: str = Field(min_length=3, max_length=50)
    full_name: str = Field(min_length=1, max_length=100)
    email: EmailStr


class UserCreate(UserBase):
    # La contrase?a en texto plano para el registro (entre 8 y 72 caracteres por limitaci?n de bcrypt)
    password: str = Field(min_length=8, max_length=72)


class UserPublic(UserBase):
    # Esquema p?blico: NUNCA expone hashed_password
    id: int
    role: str
    disabled: bool


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


class MessageResponse(SQLModel):
    mensaje: str
