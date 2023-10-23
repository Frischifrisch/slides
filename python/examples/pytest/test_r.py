import pytest

def test_pass():
    pass

def test_fail():
    assert False

@pytest.mark.skip(reason="Unconditional skip")
def test_with_skip():
    pass

@pytest.mark.skipif(True, reason="Conditional skip")
def test_with_skipif():
    pass

@pytest.mark.skipif(False, reason="Conditional skip")
def test_with_skipif_but_run():
    pass


@pytest.mark.xfail(reason = "Expect to fail and failed")
def test_with_xfail_and_fail():
   assert False

@pytest.mark.xfail(reason = "Expect to fail but passed")
def test_with_xfail_but_pass():
    pass
