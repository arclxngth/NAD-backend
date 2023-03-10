"""empty message

Revision ID: 546eb6a5a887
Revises: 55996b2e583d
Create Date: 2023-02-25 12:59:39.152565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '546eb6a5a887'
down_revision = '55996b2e583d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id', 'username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
