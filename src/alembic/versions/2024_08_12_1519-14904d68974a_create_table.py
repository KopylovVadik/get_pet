"""create table

Revision ID: 14904d68974a
Revises: 
Create Date: 2024-08-12 15:19:21.932466

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = "14904d68974a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "owners",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=True, comment="Имя"),
        sa.Column("last_name", sa.String(), nullable=True, comment="Фамилия"),
        sa.Column(
            "phone_number",
            sa.String(),
            nullable=True,
            comment="Номер телефона",
        ),
        sa.Column(
            "email",
            sa.String(),
            nullable=True,
            comment="Адрес электронной почты",
        ),
        sa.Column("telegram", sa.String(), nullable=True, comment="Телеграм"),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_owners")),
        sa.UniqueConstraint("email", name=op.f("uq_owners_email")),
        sa.UniqueConstraint("id", name=op.f("uq_owners_id")),
        sa.UniqueConstraint(
            "phone_number", name=op.f("uq_owners_phone_number")
        ),
        sa.UniqueConstraint("telegram", name=op.f("uq_owners_telegram")),
    )
    op.create_table(
        "pets",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True, comment="Кличка"),
        sa.Column(
            "birth_date", sa.Date(), nullable=True, comment="Дата рождения"
        ),
        sa.Column("brand", sa.String(), nullable=True, comment="Порода"),
        sa.Column(
            "special_feature",
            sa.String(),
            nullable=True,
            comment="Особые приметы",
        ),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"], ["owners.id"], name=op.f("fk_pets_owner_id_owners")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_pets")),
        sa.UniqueConstraint("id", name=op.f("uq_pets_id")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("pets")
    op.drop_table("owners")
    # ### end Alembic commands ###
