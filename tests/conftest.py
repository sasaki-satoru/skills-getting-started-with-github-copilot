import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

# Snapshot of the original in-memory activities data used to reset state between tests
_BASELINE_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(copy.deepcopy(_BASELINE_ACTIVITIES))
    yield
    activities.clear()
    activities.update(copy.deepcopy(_BASELINE_ACTIVITIES))
