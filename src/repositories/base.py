from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, Sequence, TypeVar

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

    # @abstractmethod
    # def exists(self, entity_id: int) -> bool:
    #     pass

    # @abstractmethod
    # def find_all(self) -> Sequence[Model]:
    #     pass

    @abstractmethod
    def find_by_id(self, entity_id: int) -> Model:
        pass
