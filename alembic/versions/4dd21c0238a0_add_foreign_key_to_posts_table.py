"""add foreign-key to posts table

Revision ID: 4dd21c0238a0
Revises: 2067fd63809b
Create Date: 2022-01-23 17:10:58.006314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dd21c0238a0'
down_revision = '2067fd63809b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                            local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column(table_name="posts", column_name="owner_id")
    pass
