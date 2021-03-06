def test_404(client):
    response = client.get('/404')
    assert client.get('/404').status_code == 404
    assert b'Sowwy, there is nothing here' in response.data


def test_429(client):
    for x in range(0, 50):
        client.get('/')
    response = client.get('/')
    assert response.status_code == 429
    assert b'Sowwy, you exceeded your limit!' in response.data


def test_500(client):
    response = client.get('/500')
    assert client.get('/500').status_code == 500
    assert b'Sowwy, something went wrong' in response.data


def test_clear(client):
    response = client.get('/clear')
    # TODO upload some stuff


def test_clear_folder_empty(client):
    response = client.get('/clear')
    assert response.status_code == 200
    assert b'Nothing to remove.' in response.data


def test_clear_all(client):
    response = client.get('/clear_all/REALLY_SECRET')
    # TODO upload some stuff
    # assert response.status_code == 200
    # assert b'All files are successfully removed.' in response.data
    # assert client.get('/clear_all/WRONG_KEY').status_code == 302
    # assert client.get('/clear_all/REALLY_SECRET').status_code == 429


def test_clear_all_folder_empty(client):
    response = client.get('/clear_all/REALLY_SECRET')
    assert response.status_code == 302


def test_docx_folder_empty(client):
    assert client.get('/docx').status_code == 302


def test_index_folder_empty(client):
    assert client.get('/').status_code == 200


def test_pdf_folder_empty(client):
    assert client.get('/pdf').status_code == 302
