"""Initial migration.

Revision ID: 3845bd2a1e22
Revises: 
Create Date: 2023-11-14 20:35:12.543880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3845bd2a1e22'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###
