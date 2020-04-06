import io
import os
import tempfile
import pytest
import server
from formatter import *
from werkzeug.datastructures import FileStorage

@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    with server.app.test_client() as client:
        yield client


def test_clean():
    input = "The\t test input\n is..malformed---full .... of --- bad character combos .... to....replace""";
    clean_input = clean(input)
    assert clean_input == "The test input  is... malformed-- full ...  of --  bad character combos ...  to... replace"


# def test_markov(client):
#     """Start with a blank database."""
#     input = "".join(['Alice was beginning to get very tired of sitting by her sister on the bank, and of having, '
#                      'noting to do: once or twice she had peeped into the book her sister was reading, but it '
#                      'had no pictures or conversations in it, “and what is the use of a book,” thought Alice',
#                      '“without pictures or conversations?"'])
#     input += "".join(['An unnamed narrator spends an evening getting drunk with a group of friends; as the party ',
#                       'becomes intoxicated and exuberant, the narrator embarks on a journey that ranges from seeming ',
#                       'paradises to the depths of pure hell. The fantastic world depicted in A Night of Serious ',
#                       'Drinking is actually the ordinary world turned upside down. The characters are called the ',
#                       'Anthographers, Fabricators of useless objects, Scienters, Nibblists, Clarificators, and ',
#                       'other absurd titles. Yet the inhabitants of these strange realms are only too familiar: ;,'
#                       ';scientists dissecting an animal in their laboratory, a wise man surrounded by his devotees, ',
#                       'politicians, poets expounding their rhetoric. These characters perform hilarious antics and ',
#                       'intellectual games, which they see as serious attempts to find meaning and freedom.'])
#     for ngram_size in ['1','2','3']:
#         response = client.post('/markov?ngram_size=' + ngram_size, data=input, follow_redirects=True)
#         assert response.status_code == 200
#         assert response.data.decode('utf8').split(' ')[0] in ['Alice', 'An', 'The', 'Yet', 'These']


def test_sample_document(client):
    response = client.get('/sampledocument?format=random_paragraphs&sample_size=3')
    assert response.status_code == 200
    response = client.get('/sampledocument?format=random_sentences&sample_size=3')
    assert response.status_code == 200
    response = client.get('/sampledocument?format=document')
    assert response.status_code == 200
    response = client.get(
        '/sampledocument?url=https://www.gutenberg.org/files/11/11-h/11-h.htm&format=random_paragraphs&sample_size=3')
    assert response.status_code == 200
    response = client.get(
        '/sampledocument?url=https://www.gutenberg.org/files/11/11-h/11-h.htm&format=random_sentences&sample_size=3')
    assert response.status_code == 200
    response = client.get(
        '/sampledocument?url=https://www.gutenberg.org/files/11/11-h/11-h.htm&format=document')
    assert response.status_code == 200
    response = client.get('/sampledocument?' +
                          'url=https://archive.org/stream/CalvinoItaloCosmicomics/Calvino-Italo-Cosmicomics_djvu.txt' +
                          '&format=random_paragraphs&sample_size=3')
    assert response.status_code == 200
    response = client.get('/sampledocument?' +
                          'url=https://archive.org/stream/CalvinoItaloCosmicomics/Calvino-Italo-Cosmicomics_djvu.txt' +
                          '&format=random_sentences&sample_size=3')
    assert response.status_code == 200
    response = client.get('/sampledocument?' +
                          'url=https://archive.org/stream/CalvinoItaloCosmicomics/Calvino-Italo-Cosmicomics_djvu.txt' +
                          '&format=document')
    assert response.status_code == 200

def test_upload_document(client):
    file = open("tests/test.epub", "rb")
    upload = (io.BytesIO(file.read()), 'test.epub')
    response = client.post('/uploaddocument?format=document',
                             content_type='multipart/form-data',
                             data={'file': upload},
                             follow_redirects=True)
    assert response.data.decode('utf-8')[0:50] == '_Planus_ by Blaise Cendrars\n\nEdited and translated'
    file = open("tests/alice.txt", "rb")
    upload = (io.BytesIO(file.read()), 'alice.txt')
    response = client.post('/uploaddocument?format=document',
                           content_type='multipart/form-data',
                           data={'file': upload},
                           follow_redirects=True)
    assert response.data.decode('utf-8')[0:52] == "Project Gutenberg's Alice's Adventures in Wonderland"

