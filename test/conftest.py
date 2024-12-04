import pytest
import inspect


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    for item in items:
        if (
            isinstance(item, pytest.Function)
            and inspect.iscoroutinefunction(item.function)
        ):
            item.add_marker(pytest.mark.asyncio)
