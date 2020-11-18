"""Budget changes

Revision ID: d656427b061e
Revises: f3489c4ea98f
Create Date: 2020-11-18 13:05:57.355006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd656427b061e'
down_revision = 'f3489c4ea98f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('budgets_created_by_key', 'budgets', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('budgets_created_by_key', 'budgets', ['created_by'])
    # ### end Alembic commands ###
