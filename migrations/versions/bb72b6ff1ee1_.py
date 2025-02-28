"""empty message

Revision ID: bb72b6ff1ee1
Revises: 3d5f08e1d388
Create Date: 2021-04-01 01:33:11.420915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb72b6ff1ee1'
down_revision = '3d5f08e1d388'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'people_sw', 'planets_sw', ['planets_id_fk'], ['id_planets'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'people_sw', type_='foreignkey')
    # ### end Alembic commands ###
