from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class DepositData:
    document_number: str
    amount: Decimal
