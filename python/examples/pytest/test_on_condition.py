import sys
import pytest

@pytest.mark.skipif(sys.platform != 'darwin', reason="Mac tests")
def test_mac():
    pass

@pytest.mark.skipif(sys.platform != 'linux', reason="Linux tests")
def test_linux():
    pass

@pytest.mark.skipif(sys.platform != 'win32', reason="Windows tests")
def test_windows():
    pass

@pytest.mark.skip(reason="To show we can skip tests without any condition.")
def test_any():
    pass
