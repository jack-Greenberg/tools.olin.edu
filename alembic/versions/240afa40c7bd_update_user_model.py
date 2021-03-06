"""Update user model

Revision ID: 240afa40c7bd
Revises: 758b92a5a1b5
Create Date: 2020-07-26 00:12:27.729840

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "240afa40c7bd"
down_revision = "758b92a5a1b5"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_role",
        sa.Column("user_id", sa.Integer(), nullable=False),
        # sa.Column('role', sa.Enum('BASE', 'STUDENT', 'NINJA', 'FACULTY', 'ADMIN', name='role'), nullable=True),
        sa.PrimaryKeyConstraint("user_id"),
    )
    op.drop_table("tool_level")
    op.drop_table("user_tool_level")
    op.add_column("training", sa.Column("name", sa.String(), nullable=True))
    op.add_column("training", sa.Column("prerequisite", sa.Integer(), nullable=True))
    op.drop_constraint("training_tool_id_fkey", "training", type_="foreignkey")
    op.drop_constraint("training_user_id_fkey", "training", type_="foreignkey")
    op.create_foreign_key(None, "training", "training", ["prerequisite"], ["id"])
    op.drop_column("training", "tool_id")
    op.drop_column("training", "user_id")
    op.add_column("user", sa.Column("user_id", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "user_id")
    op.add_column(
        "training",
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "training",
        sa.Column("tool_id", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.drop_constraint(None, "training", type_="foreignkey")
    op.create_foreign_key(
        "training_user_id_fkey", "training", "user", ["user_id"], ["id"]
    )
    op.create_foreign_key(
        "training_tool_id_fkey", "training", "tool", ["tool_id"], ["id"]
    )
    op.drop_column("training", "prerequisite")
    op.drop_column("training", "name")
    op.create_table(
        "user_tool_level",
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("tool_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "tool_level",
            postgresql.ENUM("BASIC", "INTERMEDIATE", "CNC", name="traininglevel"),
            autoincrement=False,
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["tool_id"], ["tool.id"], name="user_tool_level_tool_id_fkey"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name="user_tool_level_user_id_fkey"
        ),
        sa.PrimaryKeyConstraint("user_id", "tool_id", name="user_tool_level_pkey"),
    )
    op.create_table(
        "tool_level",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "level",
            postgresql.ENUM("BASIC", "INTERMEDIATE", "CNC", name="traininglevel"),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("tool_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("prerequisite", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["prerequisite"], ["tool_level.id"], name="tool_level_prerequisite_fkey"
        ),
        sa.ForeignKeyConstraint(
            ["tool_id"], ["tool.id"], name="tool_level_tool_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="tool_level_pkey"),
    )
    op.drop_table("user_role")
    # ### end Alembic commands ###
