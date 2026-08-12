from abc import ABC, abstractmethod
from app.domain.entities.producto import Producto

class ProductoRepository(ABC):
    @abstractmethod
    def guardar(self, producto: Producto) -> Producto:
        pass
    
    @abstractmethod
    def obtener_por_id(self, producto_id: int) -> Producto | None:
        pass

    @abstractmethod
    def obtener_todos(self) -> list[Producto]:
        pass
    
    @abstractmethod
    def actualizar(self, producto: Producto) -> Producto:
        pass

    @abstractmethod
    def eliminar(self, producto_id: int) -> bool:
        pass