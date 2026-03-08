import json
from typing import Any

from fastmcp import FastMCP
from course_store import store

mcp = FastMCP("My MCP Server")
@mcp.tool
def search_courses(course_id: str) -> Any:
    course_info = store.search_courses(course_id)
    if course_info is None:
        return {"error": "Course not found"}
    return course_info


if __name__ == "__main__":
    mcp.run()
