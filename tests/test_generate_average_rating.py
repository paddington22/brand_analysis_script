import pytest
from src.reports.reports import AverageRatingReport


def test_generate_average_rating():
    report = AverageRatingReport()

    test_data = [
        {"brand": "Brand A", "rating": "4.5"},
        {"brand": "Brand A", "rating": "4.0"},
        {"brand": "Brand B", "rating": "3.0"},
        {"brand": "Brand B", "rating": "5.0"},
        {"brand": "Brand C", "rating": "4.0"},
        {"brand": "Brand C", "rating": "5.0"},
    ]

    result = report.generate(test_data)

    assert len(result) == 3

    brand_ratings = dict(result)
    assert brand_ratings["Brand A"] == 4.25
    assert brand_ratings["Brand B"] == 4.0
    assert brand_ratings["Brand C"] == 4.5


def test_generate_empty_data():
    report = AverageRatingReport()

    result = report.generate([])
    assert result == []


def test_display_empty_result(capsys):
    report = AverageRatingReport()
    report.display([])

    captured = capsys.readouterr()
    assert "Empty result" in captured.out


def test_display_with_data(capsys):
    report = AverageRatingReport()
    test_result = [("Brand A", 4.5), ("Brand B", 3.8)]

    report.display(test_result)

    captured = capsys.readouterr()
    assert "Brand A" in captured.out
    assert "Brand B" in captured.out
    assert "4.5" in captured.out
    assert "3.8" in captured.out
