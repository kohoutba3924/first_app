from collections import deque
from typing import Optional

from first_app.models.corporate_actions import CorporateAction


# Define the corporate actions queue logic and features
class InMemoryQueue:
    def __init__(self):
        self._queue = deque()

    def enqueue(self, action: CorporateAction) -> None:
        self._queue.append(action)

    def dequeue(self) -> Optional[CorporateAction]:
        if not self._queue:
            return None
        return self._queue.popleft()

    def peek(self) -> Optional[CorporateAction]:
        if not self._queue:
            return None
        return self._queue[0]

    def size(self) -> int:
        return len(self._queue)

    def is_empty(self) -> bool:
        return len(self._queue) == 0

    def items(self):
        return list(self._queue)

    def update(self, action):
        # No persistence needed for in-memory queue
        pass
