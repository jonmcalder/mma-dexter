"""raw html

Revision ID: 4437cb6ea605
Revises: 2a3bbd3d21d
Create Date: 2015-03-26 14:19:47.531372

"""

# revision identifiers, used by Alembic.
revision = '4437cb6ea605'
down_revision = '2a3bbd3d21d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('documents', sa.Column('raw_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('documents', 'raw_html')
    ### end Alembic commands ###