"""Private Messages

Revision ID: 514ca0a3282c
Revises: 8ad96e49dc6
Create Date: 2015-03-22 21:57:57.444251

"""

# revision identifiers, used by Alembic.
revision = '514ca0a3282c'
down_revision = '8ad96e49dc6'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conversations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('from_user_id', sa.Integer(), nullable=True),
    sa.Column('to_user_id', sa.Integer(), nullable=True),
    sa.Column('shared_id', sqlalchemy_utils.types.uuid.UUIDType(binary=16), nullable=False),
    sa.Column('subject', sa.String(length=255), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('trash', sa.Boolean(), nullable=False),
    sa.Column('draft', sa.Boolean(), nullable=False),
    sa.Column('unread', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['from_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['to_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('conversation_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversations.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('privatemessages')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('privatemessages',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('from_user_id', sa.INTEGER(), nullable=True),
    sa.Column('to_user_id', sa.INTEGER(), nullable=True),
    sa.Column('subject', sa.VARCHAR(length=255), nullable=True),
    sa.Column('message', sa.TEXT(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('trash', sa.BOOLEAN(), nullable=False),
    sa.Column('draft', sa.BOOLEAN(), nullable=False),
    sa.Column('unread', sa.BOOLEAN(), nullable=False),
    sa.ForeignKeyConstraint(['from_user_id'], [u'users.id'], ),
    sa.ForeignKeyConstraint(['to_user_id'], [u'users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], [u'users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('messages')
    op.drop_table('conversations')
    ### end Alembic commands ###
