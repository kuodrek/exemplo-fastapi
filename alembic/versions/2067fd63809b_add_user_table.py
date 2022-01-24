"""add user table

Revision ID: 2067fd63809b
Revises: 574dbabc2171
Create Date: 2022-01-21 17:45:22.958174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2067fd63809b'
down_revision = '574dbabc2171'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade():
    op.drop_table('users')
    pass
