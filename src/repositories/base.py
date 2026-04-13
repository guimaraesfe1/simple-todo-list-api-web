from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

Model = TypeVar('Model')


class BaseRepository(ABC, Generic[Model]):
    @abstractmethod
    def save(self, entity: Model) -> Model:
        pass

    @abstractmethod
    def remove(self, entity: Model) -> None:
        pass

    @abstractmethod
    def update(self, entity: Model, entity_data_dict: dict[str, Any]) -> Model:
        pass

    @abstractmethod
    def find_by_id(self, entity_id: int) -> Model:
        pass

    @abstractmethod
    def find_by_label(self, entity_label: str) -> Model:
        pass
