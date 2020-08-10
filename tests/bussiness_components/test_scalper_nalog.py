def test_get_request(bc_scalper_nalog):
    """
    Тест метода get_request.
    test_link - реальная ссылка на json.
    Ожидается: 200 статус код int.
    """
    test_link = 'https://bo.nalog.ru/nbo/organizations/search?query=5405956474'
    response = bc_scalper_nalog.get_request(test_link)
    expect_status_code = 200
    assert response.status_code == expect_status_code
