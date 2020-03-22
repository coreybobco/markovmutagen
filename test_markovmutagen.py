import os
import tempfile

import pytest

from server import server


@pytest.fixture
def client():
    db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
    server.app.config['TESTING'] = True

    with server.app.test_client() as client:
        with server.app.app_context():
            server.init_db()
        yield client

    os.close(db_fd)
    os.unlink(server.app.config['DATABASE'])

def test_index(client):
    """Start with a blank database."""

    rv = client.get('/')
    import ipdb; ipdb.set_trace()