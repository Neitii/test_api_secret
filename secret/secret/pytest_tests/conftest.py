import pytest

from django.conf import settings


@pytest.fixture
def form_data():
    return {
        "secret": "secret_data",
        "passphrase": "passphrase_data"
    }

@pytest.fixture
def phrase_data():
    return {
        "passphrase": "passphrase_data"
    }

@pytest.fixture
def not_phrase_data():
    return {
        "passphrase": "not_passphrase_data"
    }
