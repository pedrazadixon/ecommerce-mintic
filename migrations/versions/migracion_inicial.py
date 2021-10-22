from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash

revision = 'migracion_inicial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    table = op.create_table(
        'usuarios',
        sa.Column('usu_id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('usu_usuario', sa.String(), nullable=False),
        sa.Column('usu_email', sa.String(), nullable=False),
        sa.Column('usu_password', sa.String(), nullable=False),
        sa.Column('usu_rol', sa.String(), nullable=False),
        sa.Column('usu_nombres', sa.String(), nullable=False),
        sa.Column('usu_apellidos', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('usu_id')
    )

    op.bulk_insert(
        table,
        [
            {
                'usu_usuario': 'super',
                'usu_email': 'superadmin@localhost',
                'usu_password': generate_password_hash('super'),
                'usu_rol': 'superadministrador',
                'usu_nombres': "Super",
                'usu_apellidos': "Administrador"
            },
            {
                'usu_usuario': 'admin',
                'usu_email': 'admin@localhost',
                'usu_password': generate_password_hash('admin'),
                'usu_rol': 'administrador',
                'usu_nombres': "Administrador",
                'usu_apellidos': ""
            },
            {
                'usu_usuario': 'usuariofinal',
                'usu_email': 'usuariofinal@localhost',
                'usu_password': generate_password_hash('usuariofinal'),
                'usu_rol': 'usuariofinal',
                'usu_nombres': "Usuario",
                'usu_apellidos': "Final"
            },
        ]
    )

    table = op.create_table(
        'lista_de_deseos',
        sa.Column('lis_id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('lis_usuario_id', sa.Integer(), nullable=False),
        sa.Column('lis_producto_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('lis_id')
    )

    table = op.create_table(
        'productos',
        sa.Column('pro_id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('pro_nombre', sa.String(), nullable=False),
        sa.Column('pro_precio', sa.Float(), nullable=False),
        sa.Column('pro_descripcion', sa.Text(), nullable=False),
        sa.Column('pro_creado', sa.DateTime(), nullable=True),
        sa.Column('pro_img', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('pro_id')
    )

    table = op.create_table(
        'comentarios',
        sa.Column('com_id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('com_comentario', sa.Text(), nullable=False),
        sa.Column('com_usuario_id', sa.Integer(), nullable=False),
        sa.Column('com_producto_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('com_id')
    )


def downgrade():
    op.drop_table('usuarios')
