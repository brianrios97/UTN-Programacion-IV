from typing import List, Optional
from sqlmodel import Session, select
from app.ingrediente.model import Ingrediente
from app.ingrediente.schema import IngredienteCreate, IngredienteUpdate


class IngredienteService:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Ingrediente]:
        return list(self.session.exec(select(Ingrediente).order_by(Ingrediente.id)).all())

    def get_by_id(self, id: int) -> Optional[Ingrediente]:
        return self.session.get(Ingrediente, id)

    def create(self, data: IngredienteCreate) -> Ingrediente:
        # Verificar unicidad (409)
        existente = self.session.exec(
            select(Ingrediente).where(Ingrediente.nombre.ilike(data.nombre))
        ).first()
        if existente:
            raise ValueError(f"Ya existe un ingrediente con el nombre '{data.nombre}'")

        db_ingrediente = Ingrediente(nombre=data.nombre)
        self.session.add(db_ingrediente)
        self.session.commit()
        self.session.refresh(db_ingrediente)
        return db_ingrediente

    def update(self, id: int, data: IngredienteUpdate) -> Optional[Ingrediente]:
        db_ingrediente = self.get_by_id(id)
        if not db_ingrediente:
            return None

        # Si cambia el nombre, verificar que no colisione con otro
        if data.nombre.lower() != db_ingrediente.nombre.lower():
            existente = self.session.exec(
                select(Ingrediente).where(
                    Ingrediente.nombre.ilike(data.nombre),
                    Ingrediente.id != id
                )
            ).first()
            if existente:
                raise ValueError(f"Ya existe otro ingrediente con el nombre '{data.nombre}'")

        db_ingrediente.nombre = data.nombre
        self.session.add(db_ingrediente)
        self.session.commit()
        self.session.refresh(db_ingrediente)
        return db_ingrediente

    def delete(self, id: int) -> bool:
        db_ingrediente = self.get_by_id(id)
        if not db_ingrediente:
            return False

        self.session.delete(db_ingrediente)
        self.session.commit()
        return True
