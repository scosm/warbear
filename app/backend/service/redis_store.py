import redis
from redis import Redis
import json

class RedisStore:
    """
    This class provides normal CRUD functionality to a redis database ("Remote Dictionary Service").
    See:
        https://redis.io/
        https://www.geeksforgeeks.org/introduction-to-redis-server/
        https://medium.com/wix-engineering/redis-as-a-database-f9df579b09c0 ("Redis as a Database").
    The methods take the id of a WorkItem and the WorkItem's data as payload,
    and each method executes its designated function for that WorkItem: id, content.
    Redis stores its content as key-value pairs, where id is the key,
    and the JSON content is the value saved at the location of that id key.
    As of redis-py 3.0, Redis is StrictRedis, hence follows the Redis API rigorously.
    """

    database: Redis  # Reference to the redis database via an abc (as interface).

    def __init__(self, host='localhost', port=6379):
        # Ensure we have a client reference defined for all subsequent calls to RedisStore.
        self.database = redis.Redis(host=host, port=port, decode_responses=True)

    def create_workitem(self, id: str, content: dict) -> bool:
        self.database.set(id, json.dumps(content))
        return True

    def read_workitem(self, id: str) -> dict:
        workitem = self.database.get(id)  # Content was stored as JSON.
        return json.loads(workitem) if workitem else None

    def update_workitem(self, id: str, new_content: dict) -> bool:
        # set() returns "OK" on success operation to update the value at that key (id).
        return self.database.set(id, json.dumps(new_content)) if self.database.exists(id) else False

    def delete_workitem(self, id: str) -> bool:
        """
        Deletes one key from our WorkItem store.

        Args:
            id (str): The UUID that uniquely identifies the WorkItem to delete.

        Returns:
            bool: True if the WorkItem was deleted successfully.
        """
        return self.database.delete(id) > 0 if self.database.exists(id) else False
