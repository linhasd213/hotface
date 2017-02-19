"""Add user authentication infos

Revision ID: 221d918aa9f0
Revises: 127be3fb000
Create Date: 2016-06-06 13:45:52.915050

"""

# revision identifiers, used by Alembic.
revision = '221d918aa9f0'
down_revision = '127be3fb000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('activated', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('last_failed_login', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('login_attempts', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'activated')
    op.drop_column('users', 'login_attempts')
    op.drop_column('users', 'last_failed_login')
    ### end Alembic commands ###