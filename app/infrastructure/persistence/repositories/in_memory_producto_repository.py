from app.domain.entities.producto import Producto
from app.domain.repositories.producto_repository import ProductoRepository


class InMemoryProductoRepository(ProductoRepository):

    def __init__(self):
        self._productos: dict[int, Producto] = {}
        self._next_id = 1

    def guardar(self, producto: Producto) -> Producto:
        producto.id = self._next_id
        self._productos[self._next_id] = producto
        self._next_id += 1

        return producto

    def obtener_por_id(self, producto_id: int) -> Producto | None:
        return self._productos.get(producto_id)

    def obtener_todos(self) -> list[Producto]:
        return list(self._productos.values())

    def actualizar(self, producto: Producto) -> Producto:
        if producto.id is None:
            raise ValueError("El producto debe tener un ID para actualizarse")

        if producto.id not in self._productos:
            raise ValueError("El producto no existe")

        self._productos[producto.id] = producto

        return producto

    def eliminar(self, producto_id: int) -> None:
        if producto_id not in self._productos:
            raise ValueError("El producto no existe")

        del self._productos[producto_id]