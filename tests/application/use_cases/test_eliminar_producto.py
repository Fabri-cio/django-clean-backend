import pytest

from app.application.use_cases.eliminar_producto import (
    EliminarProductoUseCase,
)
from app.domain.entities.producto import Producto
from app.infrastructure.persistence.repositories.in_memory_producto_repository import (
    InMemoryProductoRepository,
)


def test_eliminar_producto():
    # Arrange
    repository = InMemoryProductoRepository()

    producto = Producto(
        id=None,
        nombre="Laptop",
        descripcion="Laptop Lenovo",
        precio=5000,
        stock=10,
    )

    producto_guardado = repository.guardar(producto)

    use_case = EliminarProductoUseCase(repository)

    # Act
    use_case.ejecutar(producto_guardado.id)

    # Assert
    assert repository.obtener_por_id(producto_guardado.id) is None


def test_eliminar_producto_cuando_no_existe():
    # Arrange
    repository = InMemoryProductoRepository()
    use_case = EliminarProductoUseCase(repository)

    # Act & Assert
    with pytest.raises(ValueError, match="El producto no existe"):
        use_case.ejecutar(999)