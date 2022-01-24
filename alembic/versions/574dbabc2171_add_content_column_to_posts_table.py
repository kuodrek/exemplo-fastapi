"""add content column to posts table

Revision ID: 574dbabc2171
Revises: f83a0230a271
Create Date: 2022-01-21 17:39:42.597917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '574dbabc2171'
down_revision = 'f83a0230a271'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
