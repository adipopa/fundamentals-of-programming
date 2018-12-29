from repositories.disease_repository import DiseaseRepository
from controllers.disease_controller import DiseaseController
from ui.console import Console

disease_repository = DiseaseRepository()

disease_controller = DiseaseController(disease_repository)

console = Console(disease_controller)

console.run_console()
