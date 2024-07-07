"""Add fields about_me and last_seen to User model

Revision ID: 23b0d7228b0f
Revises: 14bc916cc583
Create Date: 2024-07-07 16:59:38.121324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23b0d7228b0f'
down_revision = '14bc916cc583'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
