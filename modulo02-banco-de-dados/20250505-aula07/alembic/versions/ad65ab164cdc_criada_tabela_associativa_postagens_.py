"""criada tabela associativa postagens_categorias

Revision ID: ad65ab164cdc
Revises: ab703705a71d
Create Date: 2025-05-02 21:33:33.778958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad65ab164cdc'
down_revision: Union[str, None] = 'ab703705a71d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('postagens_categorias',
    sa.Column('postagem_id', sa.Integer(), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['categorias.id'], ),
    sa.ForeignKeyConstraint(['postagem_id'], ['postagens.id'], ),
    sa.PrimaryKeyConstraint('postagem_id', 'categoria_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('postagens_categorias')
    # ### end Alembic commands ###
