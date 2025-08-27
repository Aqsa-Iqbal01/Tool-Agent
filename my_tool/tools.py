from agents import function_tool


@function_tool
async def add(a:int, b:int) -> str:
    """This is plus function
    arg:
         a:int
         b:int
        return str
"""
    print("plus tool fire ----->")
    return f"Your answer is {a + b}"




@function_tool
async def subtract(a:int, b:int) -> str:
    """This is plus function
    arg:
         a:int
         b:int
        return str
"""

    print("subtract tool fire ----->")
    return f"Your answer is {a - b}"