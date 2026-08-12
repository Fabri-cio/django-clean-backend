from app.domain.repositories.producto_repository import ProductoRepository
from app.domain.entities.producto import Producto

class ActualizarProductoUseCase:
    def __init__(self, producto_repository: ProductoRepository):
        self.producto_repository = producto_repository

    def ejecutar(self, producto_id: int, nombre: str, descripcion: str, precio: float, stock: int) -> Producto:
        producto = self.producto_repository.obtener_por_id(producto_id)
        
        if producto is None:
            raise ValueError("El producto no existe")
        
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.stock = stock
        
        return self.producto_repository.actualizar(producto)
        