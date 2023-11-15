"""rename address

Revision ID: 90fb5b049faf
Revises: 50bcba436187
Create Date: 2023-11-14 21:11:41.331229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90fb5b049faf'
down_revision = '50bcba436187'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
