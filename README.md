# budget_fule

Simple budget management utilities.

## Usage

```python
from budget_management import BudgetManager

manager = BudgetManager()
manager.set_budget_limit(1000)
manager.add_income(200)
manager.add_expense(150)

print(manager.summary())
```