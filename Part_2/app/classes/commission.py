from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class Commission(ABC):
    """Represents a commission payment process."""

    @abstractmethod
    def get_payment(self) -> float:
        """Returns the commission to be paid out."""
