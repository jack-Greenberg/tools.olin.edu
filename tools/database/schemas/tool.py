from flask import g
from graphene import Field, Mutation, ObjectType, String, List
from graphene_sqlalchemy import SQLAlchemyObjectType

from tools.utils import Role
from tools.auth import scoped
from ..models import Tool as ToolModel, ToolCategory as ToolCategoryModel

"""
Schemas
"""


class Tool(SQLAlchemyObjectType):
    class Meta:
        model = ToolModel


class ToolCategory(SQLAlchemyObjectType):
    class Meta:
        model = ToolCategoryModel


"""
Queries
"""


class ToolQuery(ObjectType):
    tool = Field(Tool, name=String(required=True))
    tools = List(Tool)
    tools_by_category = List(Tool, category=String(required=True))

    @staticmethod
    def resolve_tool(self, info, name=""):
        return g.db_session.query(ToolModel).filter_by(name=name).first()

    @staticmethod
    def resolve_tools(self, info):
        return g.db_session.query(ToolModel).all()

    @staticmethod
    def resolve_tools_by_category(self, info, category):
        return (
            g.db_session.query(ToolModel)
            .filter(ToolModel.category.has(name=category))
            .all()
        )


"""
Mutations
"""


class AddTool(Mutation):
    class Arguments:
        name = String(required=True)
        category = String()

    Output = Tool

    @staticmethod
    @scoped(Role.ADMIN)
    def mutate(self, info, **kwargs):
        # TODO: name to lower case and underscores for commas,
        # both for tool and category
        category_name = kwargs.pop("category")
        new_tool = ToolModel(**kwargs)

        category = (
            g.db_session.query(ToolCategoryModel).filter_by(name=category_name).first()
        )

        if not category:
            category = ToolCategoryModel(name=category_name)
            g.db_session.add(category)

        new_tool.category = category
        g.db_session.add(new_tool)
        g.db_session.flush()

        return new_tool


class ToolMutation(ObjectType):
    add_tool = AddTool.Field()
