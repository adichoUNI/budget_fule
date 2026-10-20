import unittest

from budget_management import BudgetManager


class BudgetManagerTests(unittest.TestCase):
    def test_summary_values(self) -> None:
        manager = BudgetManager()
        manager.set_budget_limit(1000)
        manager.add_income(250)
        manager.add_expense(100)
        manager.add_expense(50)

        self.assertEqual(
            manager.summary(),
            {
                "budget_limit": 1000.0,
                "income": 250.0,
                "total_expenses": 150.0,
                "available_budget": 1100.0,
                "is_over_budget": False,
            },
        )

    def test_is_over_budget(self) -> None:
        manager = BudgetManager()
        manager.set_budget_limit(100)
        manager.add_expense(150)

        self.assertTrue(manager.is_over_budget)
        self.assertEqual(manager.available_budget, -50.0)

    def test_negative_values_raise(self) -> None:
        manager = BudgetManager()
        with self.assertRaises(ValueError):
            manager.set_budget_limit(-1)
        with self.assertRaises(ValueError):
            manager.add_income(-1)
        with self.assertRaises(ValueError):
            manager.add_expense(-1)


if __name__ == "__main__":
    unittest.main()
