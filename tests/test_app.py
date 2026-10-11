
from app import app, calculate_result


def test_total_calculation():
    total, average, result = calculate_result(80, 75, 90)
    assert total == 245


def test_average_calculation():
    total, average, result = calculate_result(80, 75, 90)
    assert average == 245 / 3


def test_pass_result():
    total, average, result = calculate_result(80, 75, 90)
    assert result == "PASS"


def test_fail_result():
    total, average, result = calculate_result(20, 30, 35)
    assert result == "FAIL"


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Result Application" in response.data
