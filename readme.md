# MRE for pytest-asyncio ⨯ flaky bug

Somehow latest `pytest`, `pytest-asyncio` and `flaky` just can't live happily together.

When a flaky test repeatedly fails, an error is reported instead of failure.

```
> pytest test_repro.py
========================================================== test session starts ===========================================================
platform darwin -- Python 3.8.5, pytest-6.0.0, py-1.9.0, pluggy-0.13.1
rootdir: /Users/dima.tisnek/mre-loop-closed
plugins: flaky-3.7.0, asyncio-0.14.0
collected 1 item

test_repro.py                                                                                                                      [100%]F [100%]

================================================================ FAILURES ================================================================
________________________________________________________________ test_foo ________________________________________________________________

kwargs = {}

    @functools.wraps(func)
    def inner(**kwargs):
>       coro = func(**kwargs)

../Library/Caches/pypoetry/virtualenvs/mre-loop-closed-qryTT9qY-py3.8/lib/python3.8/site-packages/pytest_asyncio/plugin.py:175:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
../Library/Caches/pypoetry/virtualenvs/mre-loop-closed-qryTT9qY-py3.8/lib/python3.8/site-packages/pytest_asyncio/plugin.py:177: in inner
    task = asyncio.ensure_future(coro, loop=_loop)
/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/asyncio/tasks.py:661: in ensure_future
    task = loop.create_task(coro_or_future)
/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/asyncio/base_events.py:429: in create_task
    self._check_closed()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <_UnixSelectorEventLoop running=False closed=True debug=False>

    def _check_closed(self):
        if self._closed:
>           raise RuntimeError('Event loop is closed')
E           RuntimeError: Event loop is closed

/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/asyncio/base_events.py:508: RuntimeError
===Flaky Test Report===

test_foo failed (1 runs remaining out of 2).
	<class 'AssertionError'>
	assert False
	[<TracebackEntry /Users/dima.tisnek/mre-loop-closed/test_repro.py:8>]
test_foo failed; it passed 0 out of the required 1 times.
	<class 'RuntimeError'>
	Event loop is closed
	[<TracebackEntry /Users/dima.tisnek/Library/Caches/pypoetry/virtualenvs/mre-loop-closed-qryTT9qY-py3.8/lib/python3.8/site-packages/pytest_asyncio/plugin.py:175>, <TracebackEntry /Users/dima.tisnek/Library/Caches/pypoetry/virtualenvs/mre-loop-closed-qryTT9qY-py3.8/lib/python3.8/site-packages/pytest_asyncio/plugin.py:177>, <TracebackEntry /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/asyncio/tasks.py:661>, <TracebackEntry /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/asyncio/base_events.py:429>, <TracebackEntry /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/asyncio/base_events.py:508>]

===End Flaky Test Report===
======================================================== short test summary info =========================================================
FAILED test_repro.py::test_foo - RuntimeError: Event loop is closed
=========================================================== 1 failed in 0.12s ============================================================
```
