from typing import List, Optional
from sqlmodel import Session, select
from app.ingrediente.model import Ingrediente
from app.ingrediente.schema import IngredienteCreate, IngredienteUpdate


class IngredienteService:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Ingrediente]:
        statement = (
            select(Ingrediente)
            .where(Ingrediente.activo == True)
            .order_by(Ingrediente.id)
        )
        return list(self.session.exec(statement).all())

    def get_by_id(self, id: int) -> Optional[Ingrediente]:
        statement = select(Ingrediente).where(
            Ingrediente.id == id,
            Ingrediente.activo == True,
        )
        return self.session.exec(statement).first()

    def create(self, data: IngredienteCreate) -> Ingrediente:
        # Verificar unicidad entre los activos (409)
        existente = self.session.exec(
            select(Ingrediente).where(
                Ingrediente.nombre.ilike(data.nombre),
                Ingrediente.activo == True,
            )
        ).first()
        if existente:
            raise ValueError(f"Ya existe un ingrediente con el nombre '{data.nombre}'")

        db_ingrediente = Ingrediente(nombre=data.nombre, activo=True)
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
                    Ingrediente.id != id,
                    Ingrediente.activo == True,
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

        # Borrado lógico: se marca inactivo (RN-11)
        db_ingrediente.activo = False
        self.session.add(db_ingrediente)
        self.session.commit()
        return True
