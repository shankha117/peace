import pytest
from app.flask_app import create_app


###*************************************************************

###***************************   Warning   *********************

###*************************************************************


## this test cases will affect the data


@pytest.fixture(scope="module")
def client():
    app = create_app()
    client = app.test_client()
    return client