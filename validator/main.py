from typing import Any, Dict, Optional, Callable
from guardrails.validator_base import (
    FailResult,
    PassResult,
    ValidationResult,
    Validator,
    register_validator,
)
from MauvaiseLangue import scrape_insultes, detect_insultes  # Importer vos fonctions

@register_validator(name="guardrails/french_toxic_language", data_type="string")
class FrenchToxicLanguage(Validator):
    """French Toxic Language Validator.
    
    Ce validateur vÃ©rifie si le texte donnÃ© contient des insultes en franÃ§ais basÃ©es sur les donnÃ©es extraites de Wiktionary.
    """

    def __init__(self, on_fail: Optional[Callable] = None):
        """
        Initialise le validateur FrenchToxicLanguage.
        
        Args:
            on_fail (Callable, optional): Politique Ã  appliquer en cas d'Ã©chec (e.g., reask, fix, filter).
        """
        super().__init__(on_fail=on_fail)
        # Charger les insultes via la fonction de scraping
        self.insultes = scrape_insultes()

    def validate(self, value: Any, metadata: Dict) -> ValidationResult:
        """
        Valide la chaÃ®ne de caractÃ¨res donnÃ©e pour vÃ©rifier si elle contient des insultes en franÃ§ais.
        
        Args:
            value (Any): Le texte d'entrÃ©e Ã  valider.
            metadata (Dict): MÃ©tadonnÃ©es supplÃ©mentaires (optionnel).
        
        Returns:
            ValidationResult: PassResult si valide, FailResult sinon.
        """
        detected_insultes = detect_insultes(value)
        
        if detected_insultes:
            return FailResult(
                error_message=f"Le texte contient un langage toxique : {', '.join(detected_insultes)}",
                fix_value=None  # Optionnellement, vous pouvez proposer de filtrer les insultes dÃ©tectÃ©es
            )
        
        return PassResult()

# Tests
class TestFrenchToxicLanguage:
    def test_success_case(self):
        validator = FrenchToxicLanguage()
        result = validator.validate("Bonjour, comment Ã§a va ?", {})
        assert isinstance(result, PassResult)

    def test_failure_case(self):
        validator = FrenchToxicLanguage()
        result = validator.validate("EspÃ¨ce de idiot, imbÃ©cile !", {})
        assert isinstance(result, FailResult)
        assert "idiot" in result.error_message
