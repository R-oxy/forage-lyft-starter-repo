from abc import ABC, abstractmethod

# Serviceable interface to ensure all serviceable parts implement the needs_service method
class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
