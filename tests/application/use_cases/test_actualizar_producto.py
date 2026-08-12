import pytest

from app.application.use_cases.actualizar_producto import (
    ActualizarProductoUseCase,
)
from app.domain.entities.producto import Producto
from app.infrastructure.persistence.repositories.in_memory_producto_repository import (
    InMemoryProductoRepository,
)


def test_actualizar_producto():
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

    use_case = ActualizarProductoUseCase(repository)

    # Act
    producto_actualizado = use_case.ejecutar(
        producto_id=producto_guardado.id,
        nombre="Laptop Gamer",
        descripcion="Laptop Gamer Lenovo",
        precio=7500,
        stock=5,
    )

    # Assert
    assert producto_actualizado.id == 1
    assert producto_actualizado.nombre == "Laptop Gamer"
    assert producto_actualizado.descripcion == "Laptop Gamer Lenovo"
    assert producto_actualizado.precio == 7500
    assert producto_actualizado.stock == 5


def test_actualizar_producto_cuando_no_existe():
    # Arrange
    repository = InMemoryProductoRepository()
    use_case = ActualizarProductoUseCase(repository)

    # Act & Assert
    with pytest.raises(ValueError, match="El producto no existe"):
        use_case.ejecutar(
            producto_id=999,
            nombre="Producto",
            descripcion="Descripción",
            precio=100,
            stock=10,
        )