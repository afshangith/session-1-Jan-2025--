import pytest

@pytest.mark.usefixtures("set_up")
@pytest.mark.usefixtures("navigate_url")
class BaseTest:
    pass