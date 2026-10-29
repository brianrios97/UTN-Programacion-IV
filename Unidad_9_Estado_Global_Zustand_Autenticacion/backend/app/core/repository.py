from typing import Generic, Type, TypeVar, Optional, List
from sqlmodel import Session, select, SQLModel

ModelType = TypeVar("ModelType", bound=SQLModel)


class BaseRepository(Generic[ModelType]):
    """Repositorio base que encapsula las operaciones CRUD sin hacer commit."""

    def __init__(self, model: Type[ModelType], session: Session):
        self.model = model
        self.session = session

    def get_by_id(self, id: any) -> Optional[ModelType]:
        return self.session.get(self.model, id)

    def get_all(self) -> List[ModelType]:
        return list(self.session.exec(select(self.model)).all())

    def create(self, entity: ModelType) -> ModelType:
        self.session.add(entity)
        self.session.flush()
        return entity

    def delete(self, entity: ModelType) -> None:
        self.session.delete(entity)
        self.session.flush()
