"""add column email

Revision ID: 3ab600d66ca6
Revises: ce59c744313d
Create Date: 2022-11-29 09:27:29.334062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ab600d66ca6'
down_revision = 'ce59c744313d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('contact', sa.Column('email', sa.String(50)))


def downgrade() -> None:
    op.drop_column('contact', 'email')
