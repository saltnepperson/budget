from budget.models.budget import Budget

def test_new_budget(test_user):
    budget = Budget(
        name='testing budget',
        description='tester description',
        amount=100,
        category='test category',
        created_by=test_user.id
    )
    assert budget.name == 'testing budget'
    assert budget.created_by == test_user.id
