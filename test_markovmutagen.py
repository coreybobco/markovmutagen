import os
import tempfile

import pytest

import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    with server.app.test_client() as client:
        yield client

def test_markov(client):
    """Start with a blank database."""
    input = "".join(['Alice was beginning to get very tired of sitting by her sister on the bank, and of having, '
                     'noting to do: once or twice she had peeped into the book her sister was reading, but it '
                     'had no pictures or conversations in it, “and what is the use of a book,” thought Alice',
                     '“without pictures or conversations?"'])
    input += "".join(['An unnamed narrator spends an evening getting drunk with a group of friends; as the party ',
                      'becomes intoxicated and exuberant, the narrator embarks on a journey that ranges from seeming ',
                      'paradises to the depths of pure hell. The fantastic world depicted in A Night of Serious ',
                      'Drinking is actually the ordinary world turned upside down. The characters are called the ',
                      'Anthographers, Fabricators of useless objects, Scienters, Nibblists, Clarificators, and ',
                      'other absurd titles. Yet the inhabitants of these strange realms are only too familiar: ;,'
                      ';scientists dissecting an animal in their laboratory, a wise man surrounded by his devotees, ',
                      'politicians, poets expounding their rhetoric. These characters perform hilarious antics and ',
                      'intellectual games, which they see as serious attempts to find meaning and freedom.'])
    response = client.post('/markov', data=input, follow_redirects=True)
    assert response.split(' ')[0] in ['Alice', 'An', 'The', 'These']
