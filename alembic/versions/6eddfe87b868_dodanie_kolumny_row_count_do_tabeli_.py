"""Dodanie kolumny row_count do tabeli projects

Revision ID: 6eddfe87b868
Revises: 5ebb27b18640
Create Date: 2025-02-12 23:03:59.218280

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6eddfe87b868'
down_revision: Union[str, None] = '5ebb27b18640'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('row_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('projects', 'row_count')
    # ### end Alembic commands ###
