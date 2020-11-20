from budget.models.budget_item import BudgetItem

def test_new_budget_item(test_budget, test_user):
    budget_item = BudgetItem(
        name='testing budget item',
        description='tester budget item description',
        amount=100,
        category='test category',
        budget_id=test_budget.id,
        created_by=test_user.id
    )
    assert budget_item.name == 'testing budget item'
    assert budget_item.amount == 100
    assert budget_item.budget_id == test_budget.id
    assert budget_item.created_by == test_user.id
