"""create books table

Revision ID: 524c2f7043de
Revises: 
Create Date: 2023-02-16 17:35:44.082505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '524c2f7043de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('books_genders', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_genders_books_genders'), 'genders', ['books_genders'], unique=True)
    op.create_index(op.f('ix_genders_id'), 'genders', ['id'], unique=False)
    op.create_table('books',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=125), nullable=True),
    sa.Column('gender_name', sa.String(length=30), nullable=True),
    sa.Column('available', sa.Boolean(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('release_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['gender_name'], ['genders.books_genders'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_id'), 'books', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_books_id'), table_name='books')
    op.drop_table('books')
    op.drop_index(op.f('ix_genders_id'), table_name='genders')
    op.drop_index(op.f('ix_genders_books_genders'), table_name='genders')
    op.drop_table('genders')
    # ### end Alembic commands ###