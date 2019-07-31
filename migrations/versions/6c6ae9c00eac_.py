"""empty message

Revision ID: 6c6ae9c00eac
Revises: 31c117cf9535
Create Date: 2019-07-31 14:41:11.440479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c6ae9c00eac'
down_revision = '31c117cf9535'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('producer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyname', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=100), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address'),
    sa.UniqueConstraint('companyname')
    )
    op.add_column('product', sa.Column('producer_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'product', 'producer', ['producer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_column('product', 'producer_id')
    op.drop_table('producer')
    # ### end Alembic commands ###