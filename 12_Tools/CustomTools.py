from langchain_core.tools import tool
from langchain_core.tools import StructuredTool
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
# @tool
# def add_numbers(a: int, b: int) -> int:
#     """Add two numbers together."""
#     return a + b

# result = add_numbers.invoke({"a":3, "b":5})

# print(result)


# print(add_numbers.name)
# print(add_numbers.description)
# print(add_numbers.args)
# print("**Args Schema:**")
# print(add_numbers.args_schema.model_json_schema())



# class MultiplyInput(BaseModel):
#     a: int = Field(description="The first number to add")
#     b: int = Field(description="The second number to add")



# def multiply_func(a: int, b: int) -> int:
#     return a * b


# multiply_tool = StructuredTool.from_function(
#     func=multiply_func,
#     name="multiply",
#     description="Multiply two numbers",
#     args_schema=MultiplyInput
# )



# result = multiply_tool.invoke({'a':3, 'b':3})

# print("**Tool Invocation Result:**")
# print(result)
# print("\n**Tool Name:**")
# print(multiply_tool.name)
# print("\n**Tool Description:**")
# print(multiply_tool.description)
# print("\n**Tool Arguments:**")  
# print(multiply_tool.args)


# arg schema using pydantic

# class MultiplyInput(BaseModel):
#     a: int = Field(description="The first number to add")
#     b: int = Field(description="The second number to add")

# class MultiplyTool(BaseTool):
#     name: str = "multiply"
#     description: str = "Multiply two numbers"

#     args_schema: Type[BaseModel] = MultiplyInput

#     def _run(self, a: int, b: int) -> int:
#         return a * b
    
# multiply_tool = MultiplyTool()

# result = multiply_tool.invoke({'a':3, 'b':3})
# print("**Tool Invocation Result:**")
# print(result)
# print("\n**Tool Name:**")
# print(multiply_tool.name)
# print("\n**Tool Description:**")
# print(multiply_tool.description)
# print("\n**Tool Arguments:**")
# print(multiply_tool.args)


# Custom tools toolkit
@tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

class MathToolkit:
    def get_tools(self):
        return [add, multiply]
toolkit = MathToolkit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.name, "=>", tool.description)