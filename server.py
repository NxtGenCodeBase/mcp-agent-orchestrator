from mcp.server.fastmcp import FastMCP

mcp = FastMCP("LocalHelper")


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b


if __name__ == "__main__":
    mcp.run(transport='stdio')
