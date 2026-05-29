from first_app.queue.in_memory_queue import InMemoryQueue
from first_app.models.corporate_actions import CorporateAction


# Validates adding a corporate action to the queue works as expected
def test_enqueue_and_size():
    q = InMemoryQueue()
    action = CorporateAction(action_type="DIVIDEND")

    q.enqueue(action)

    assert q.size() == 1
    assert not q.is_empty()


# Validates that corporate actions added to the queue are stored and processed in the expected order
def test_dequeue_returns_items_in_order():
    q = InMemoryQueue()
    a1 = CorporateAction(action_type="DIVIDEND")
    a2 = CorporateAction(action_type="SPLIT")

    q.enqueue(a1)
    q.enqueue(a2)

    assert q.dequeue() == a1
    assert q.dequeue() == a2
    assert q.is_empty()


# Validates that peek() functions as expected and does not modify the queue order
def test_peek_does_not_remove_item():
    q = InMemoryQueue()
    action = CorporateAction(action_type="DIVIDEND")

    q.enqueue(action)

    assert q.peek() == action
    assert q.size() == 1
