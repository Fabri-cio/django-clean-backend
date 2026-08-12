from app.domain.repositories.producto_repository import ProductoRepository
from app.domain.entities.producto import Producto

class EliminarProductoUseCase:
    def __init__(self, producto_repository: ProductoRepository):
        self.producto_repository = producto_repository
    
    def ejecutar(self, producto_id: int) -> None:

        producto = self.producto_repository.obtener_por_id(producto_id)
        
        if producto is None:
            raise ValueError("El producto no existe")
        
        self.producto_repository.eliminar(producto_id)