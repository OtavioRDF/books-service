"""create books table

Revision ID: 105d4d86f7f8
Revises: f00064fcbd0c
Create Date: 2023-02-20 12:45:24.206812

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '105d4d86f7f8'
down_revision = 'f00064fcbd0c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('author', sa.String(length=30), nullable=False))
    op.alter_column('books', 'title',
               existing_type=mysql.VARCHAR(length=125),
               nullable=False)
    op.alter_column('books', 'gender_name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    op.alter_column('books', 'available',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.alter_column('books', 'stock',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('books', 'release_date',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('books', 'release_date',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('books', 'stock',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('books', 'available',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('books', 'gender_name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    op.alter_column('books', 'title',
               existing_type=mysql.VARCHAR(length=125),
               nullable=True)
    op.drop_column('books', 'author')
    # ### end Alembic commands ###
