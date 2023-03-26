"""upgraded6

Revision ID: 361aeba1c608
Revises: fc3a19e684d6
Create Date: 2023-03-23 20:17:08.231972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '361aeba1c608'
down_revision = 'fc3a19e684d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.Enum('planning', 'shopping', 'delivered_unpaid', 'delivered_paid', name='orderstatus'), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('status')

    # ### end Alembic commands ###
