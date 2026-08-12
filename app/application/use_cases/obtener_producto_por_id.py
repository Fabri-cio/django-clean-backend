from app.domain.entities.producto import Producto
from app.domain.repositories.producto_repository import ProductoRepository

class ObtenerProductoPorIdUseCase:
    def __init__(self, producto_repository: ProductoRepository):
        self.producto_repository = producto_repository

    def ejecutar(self, producto_id: int) -> Producto:
        producto = self.producto_repository.obtener_por_id(producto_id)

        if producto is None:
            raise ValueError("Producto no encontrado")
        
        return producto

