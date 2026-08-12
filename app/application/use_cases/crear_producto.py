from app.domain.entities.producto import Producto
from app.domain.repositories.producto_repository import ProductoRepository


class CrearProductoUseCase:

    def __init__(self, producto_repository: ProductoRepository):
        self.producto_repository = producto_repository

    def ejecutar(self, nombre: str, descripcion: str, precio: float, stock: int) -> Producto:

        producto = Producto(
            id=None,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
        )

        return self.producto_repository.guardar(producto)