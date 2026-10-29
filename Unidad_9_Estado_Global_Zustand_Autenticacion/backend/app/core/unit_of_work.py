from typing import Callable
from sqlmodel import Session


class AbstractUnitOfWork:
    """Clase base de Unit of Work que maneja la sesi?n y el ciclo de vida de la transacci?n."""

    def __init__(self, session_factory: Callable[[], Session]):
        self.session_factory = session_factory
        self.session: Session | None = None

    def __enter__(self):
        self.session = self.session_factory()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type:
                self.rollback()
            else:
                self.commit()
        finally:
            if self.session:
                self.session.close()

    def commit(self):
        if self.session:
            self.session.commit()

    def rollback(self):
        if self.session:
            self.session.rollback()
