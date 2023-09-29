"""change type to field name

Revision ID: dbf2a10ef5b6
Revises: 97d3fb37c6b0
Create Date: 2023-09-28 23:50:31.019038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbf2a10ef5b6'
down_revision = '97d3fb37c6b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.CHAR(length=8),
               type_=sa.VARCHAR(length=8),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=8),
               type_=sa.CHAR(length=8),
               existing_nullable=True)

    # ### end Alembic commands ###
