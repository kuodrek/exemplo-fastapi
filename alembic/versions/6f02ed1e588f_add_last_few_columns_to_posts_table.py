"""add last few columns to posts table

Revision ID: 6f02ed1e588f
Revises: 4dd21c0238a0
Create Date: 2022-01-23 17:16:35.965681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f02ed1e588f'
down_revision = '4dd21c0238a0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))


def downgrade():
    op.drop_column(table_name="posts", column_name="published")
    op.drop_column(table_name="posts", column_name="created_at")
    pass
