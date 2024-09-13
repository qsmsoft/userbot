"""add column to messages table

Revision ID: 74d414235cae
Revises: 93bc62d3e7f7
Create Date: 2024-09-13 14:00:14.225970

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '74d414235cae'
down_revision: Union[str, None] = '93bc62d3e7f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('messages', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('messages', sa.Column('updated_at', sa.DateTime(), nullable=True))


def downgrade() -> None:
    op.drop_column('messages', 'updated_at')
    op.drop_column('messages', 'created_at')