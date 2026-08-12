import pytest

from app.application.use_cases.obtener_producto_por_id import (
    ObtenerProductoPorIdUseCase,
)
from app.domain.entities.producto import Producto
from app.infrastructure.persistence.repositories.in_memory_producto_repository import (
    InMemoryProductoRepository,
)


def test_obtener_producto_por_id():
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
    use_case = ObtenerProductoPorIdUseCase(repository)

    # Act
    resultado = use_case.ejecutar(producto_guardado.id)

    # Assert
    assert resultado.id == 1
    assert resultado.nombre == "Laptop"
    assert resultado.descripcion == "Laptop Lenovo"
    assert resultado.precio == 5000
    assert resultado.stock == 10


def test_obtener_producto_por_id_cuando_no_existe():
    # Arrange
    repository = InMemoryProductoRepository()
    use_case = ObtenerProductoPorIdUseCase(repository)

    # Act & Assert
    with pytest.raises(ValueError, match="El producto no existe"):
        use_case.ejecutar(999)