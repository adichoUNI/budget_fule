from dataclasses import dataclass, field


@dataclass
class BudgetManager:
    budget_limit: float = 0.0
    income: float = 0.0
    expenses: list[float] = field(default_factory=list)

    def set_budget_limit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Budget limit cannot be negative.")
        self.budget_limit = float(amount)

    def add_income(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Income cannot be negative.")
        self.income += float(amount)

    def add_expense(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Expense cannot be negative.")
        self.expenses.append(float(amount))

    @property
    def total_expenses(self) -> float:
        return sum(self.expenses)

    @property
    def available_budget(self) -> float:
        return self.budget_limit + self.income - self.total_expenses

    @property
    def is_over_budget(self) -> bool:
        return self.total_expenses > (self.budget_limit + self.income)

    def summary(self) -> dict[str, float | bool]:
        return {
            "budget_limit": self.budget_limit,
            "income": self.income,
            "total_expenses": self.total_expenses,
            "available_budget": self.available_budget,
            "is_over_budget": self.is_over_budget,
        }
