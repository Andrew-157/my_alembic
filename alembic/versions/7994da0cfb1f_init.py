"""Init

Revision ID: 7994da0cfb1f
Revises: 
Create Date: 2022-11-28 15:38:08.763065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7994da0cfb1f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=23), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contacts')
    # ### end Alembic commands ###
