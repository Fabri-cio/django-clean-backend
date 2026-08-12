from app.application.use_cases.obtener_productos import ObtenerProductosUseCase
from app.domain.entities.producto import Producto
from app.infrastructure.persistence.repositories.in_memory_producto_repository import (
    InMemoryProductoRepository,
)


def test_obtener_productos():
    # Arrange
    repository = InMemoryProductoRepository()

    repository.guardar(
        Producto(
            id=None,
            nombre="Laptop",
            descripcion="Laptop Lenovo",
            precio=5000,
            stock=10,
        )
    )

    repository.guardar(
        Producto(
            id=None,
            nombre="Mouse",
            descripcion="Mouse Logitech",
            precio=150,
            stock=20,
        )
    )

    use_case = ObtenerProductosUseCase(repository)

    # Act
    productos = use_case.ejecutar()

    # Assert
    assert len(productos) == 2

    assert productos[0].id == 1
    assert productos[0].nombre == "Laptop"

    assert productos[1].id == 2
    assert productos[1].nombre == "Mouse"


def test_obtener_productos_sin_productos():
    # Arrange
    repository = InMemoryProductoRepository()
    use_case = ObtenerProductosUseCase(repository)

    # Act
    productos = use_case.ejecutar()

    # Assert
    assert productos == []