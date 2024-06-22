# tests/conftest.py
import pytest
from app import create_app


@pytest.fixture
def app():
    application = create_app()
    application.config.update(
        {
            "TESTING": True,
            # add other testing configurations here if needed
        }
    )

    # other setup can go here

    yield application

    # clean up / reset resources here


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
