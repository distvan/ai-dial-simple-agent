from typing import Any

from task.tools.users.base import BaseUserServiceTool


class DeleteUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        #Provide tool name as `delete_users`
        return "delete_users"

    @property
    def description(self) -> str:
        #Provide description of this tool
        return "Deletes user from the system"

    @property
    def input_schema(self) -> dict[str, Any]:
        # Provide tool params Schema. This tool applies user `id` (number) as a parameter and it is required
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "User ID"
                }
            },
            "required": ["id"]
        }

    def execute(self, arguments: dict[str, Any]) -> str:
        try:
            # 1. Get int `id` from arguments
            id = int(arguments["id"])
            # 2. Call user_client delete_user and return its results
            return self._user_client.delete_user(id)
        # 3. Optional: You can wrap it with `try-except` and return error as string `f"Error while deleting user by id: {str(e)}"`
        except Exception as e:
            return f"Error while deleting user by id: {str(e)}"