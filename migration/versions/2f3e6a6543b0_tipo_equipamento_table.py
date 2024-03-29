"""tipo_equipamento table

Revision ID: 2f3e6a6543b0
Revises: 
Create Date: 2024-01-04 16:42:36.155591

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '2f3e6a6543b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipo_equipamento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=False, unique=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tipo_equipamento')
    # ### end Alembic commands ###
