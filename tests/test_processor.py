from datetime import date

from first_app.queue.in_memory_queue import InMemoryQueue
from first_app.processor.action_processor import ActionProcessor
from first_app.models.corporate_actions import (
    CorporateAction,
    CorporateActionStatus,
)


# Validate a valid corporate action object will be fully processed by the processor
def test_processor_completes_valid_action():
    q = InMemoryQueue()
    processor = ActionProcessor(q)

    action = CorporateAction(
        action_type="DIVIDEND",
        metadata={"amount": 1.23},  # required for DIVIDEND
        record_date=date.today(),
        payable_date=date.today(),  # valid date relationship
    )
    q.enqueue(action)

    processed = processor.process_next()

    assert processed is True
    assert action.status == CorporateActionStatus.COMPLETED


# Validate that an invalid corporate action object will fail as expected
def test_processor_handles_validation_failure():
    q = InMemoryQueue()
    processor = ActionProcessor(q)

    # Missing action_type triggers validation failure
    action = CorporateAction(action_type="")
    q.enqueue(action)

    processed = processor.process_next()

    assert processed is False
    assert action.status == CorporateActionStatus.FAILED


# Validate that the processor behaves as expected when provided an empty queue
def test_processor_returns_false_on_empty_queue():
    q = InMemoryQueue()
    processor = ActionProcessor(q)

    processed = processor.process_next()

    assert processed is False
