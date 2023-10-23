import pytest

@pytest.mark.smoke
def test_database_read():
    pass

@pytest.mark.security
@pytest.mark.smoke
def test_database_write():
    pass

@pytest.mark.security
def test_database_forget():
    pass

@pytest.mark.smoke
def test_ui_access():
    pass

@pytest.mark.security
def test_ui_forget():
    pass

