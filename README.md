# FrenchToxicLanguage 

| Developed by |JOHN WAIA|
| --- | --- |
| Date of development | Oct 2024 |
| Validator type | Toxic Language Detection |
| License | Apache 2 |
| Input/Output | Output |

## Description

### Intended Use
This validator detects toxic language in French, focusing on insults scraped from Wiktionary. It ensures that input text does not contain harmful or offensive language based on a list of French insults.

### Requirements

* Dependencies:
	- guardrails-ai>=0.4.0
	- MauvaiseLangue>=1.0.8 (for scraping and detecting insults from Wiktionary)

## Installation

```bash
$ guardrails hub install hub://guardrails/french_toxic_language
```

## Usage Examples

### Validating string output via Python

In this example, we apply the `FrenchToxicLanguage` validator to a string output:

```python
# Import Guard and Validator
from guardrails.hub import FrenchToxicLanguage
from guardrails import Guard

# Setup Guard
guard = Guard().use(
    FrenchToxicLanguage
)

guard.validate("Bonjour, comment ça va ?")  # Validator passes
guard.validate("Espèce de idiot, imbécile !")  # Validator fails
```

### Validating JSON output via Python

In this example, we apply the validator to a string field of a JSON output:

```python
# Import Guard and Validator
from pydantic import BaseModel, Field
from guardrails.hub import FrenchToxicLanguage
from guardrails import Guard

# Initialize Validator
val = FrenchToxicLanguage()

# Create Pydantic BaseModel
class Message(BaseModel):
    content: str = Field(validators=[val])

# Create a Guard to check for valid Pydantic output
guard = Guard.from_pydantic(output_class=Message)

# Run LLM output generating JSON through guard
guard.parse("""
{
    "content": "Espèce de idiot"
}
""")
```

# API Reference

**`__init__(self, on_fail=None)`**
<ul>
Initializes a new instance of the FrenchToxicLanguage validator. 

**Parameters**
- **`on_fail`** *(Callable, optional)*: The policy to apply when a validator fails. It could be a custom function or one of Guardrails' standard policies like `reask`, `fix`, `filter`, etc.
</ul>
<br/>

**`validate(self, value, metadata) -> ValidationResult`**
<ul>
Validates the given `value` by checking it against a list of French insults. If the input contains any toxic language, it will fail the validation.

**Parameters**
- **`value`** *(Any)*: The input text to validate.
- **`metadata`** *(dict)*: A dictionary containing metadata (optional).

**Returns**
- A `PassResult` if the text does not contain toxic language.
- A `FailResult` if the text contains insults, along with a list of the detected insults.
</ul>

## Contributeurs

- [johnwaia](https://github.com/votreprofil) 
