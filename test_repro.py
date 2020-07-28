import pytest
from flaky import flaky

pytestmark = pytest.mark.asyncio

@flaky
async def test_foo():
    assert False
