"""delete phone

Revision ID: 8b76a51f373e
Revises: 3ab600d66ca6
Create Date: 2022-11-29 10:22:24.817465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b76a51f373e'
down_revision = '3ab600d66ca6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('contact', 'phone')


def downgrade() -> None:
    op.add_column('contact', sa.Column('phone', sa.String(15)))
