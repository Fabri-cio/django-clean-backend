from app.domain.entities.producto import Producto
from app.domain.repositories.producto_repository import ProductoRepository

class ObtenerProductosUseCase:
    def __init__(self, producto_repository: ProductoRepository):
        self.producto_repository = producto_repository

    def ejecutar(self) -> list[Producto]:
        return self.producto_repository.obtener_todos()