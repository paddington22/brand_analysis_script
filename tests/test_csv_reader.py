import pytest
import os
import tempfile

from src.utils.csv_reader import read_csv_files


def test_read_csv_files_single_file():
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False
    ) as file:
        file.write("name,brand,price,rating\n")
        file.write("name A,brand A,100,1.0\n")
        file.write("name B,brand B,200,2.0\n")
        test_file = file.name

    try:
        data = read_csv_files([test_file])
        assert len(data) == 2
        assert data[0]["name"] == "name A"
        assert data[0]["brand"] == "brand A"
        assert data[0]["price"] == "100"
        assert data[0]["rating"] == "1.0"
        assert data[1]["name"] == "name B"
        assert data[1]["brand"] == "brand B"
        assert data[1]["price"] == "200"
        assert data[1]["rating"] == "2.0"
    finally:
        os.remove(test_file)


def test_read_csv_files_multiplie_files():
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False
    ) as file1:
        file1.write("name,brand,price,rating\n")
        file1.write("name A,brand A,100,1.0\n")
        file1.write("name B,brand B,200,2.0\n")
        test_file1 = file1.name

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False
    ) as file2:
        file2.write("name,brand,price,rating\n")
        file2.write("name C,brand C,300,3.0\n")
        file2.write("name D,brand D,400,4.0\n")
        test_file2 = file2.name

    try:
        data = read_csv_files([test_file1, test_file2])
        assert len(data) == 4
        assert data[0]["name"] == "name A"
        assert data[0]["brand"] == "brand A"
        assert data[0]["price"] == "100"
        assert data[0]["rating"] == "1.0"
        assert data[1]["name"] == "name B"
        assert data[1]["brand"] == "brand B"
        assert data[1]["price"] == "200"
        assert data[1]["rating"] == "2.0"
        assert data[2]["name"] == "name C"
        assert data[2]["brand"] == "brand C"
        assert data[2]["price"] == "300"
        assert data[2]["rating"] == "3.0"
        assert data[3]["name"] == "name D"
        assert data[3]["brand"] == "brand D"
        assert data[3]["price"] == "400"
        assert data[3]["rating"] == "4.0"
    finally:
        os.remove(test_file1)
        os.remove(test_file2)


def test_read_csv_files_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_csv_files(["nonexistent_file.csv"])


def test_read_csv_files_invalid_format():
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False
    ) as file:
        file.write("some data\n")
        test_file = file.name

    try:
        with pytest.raises(ValueError):
            read_csv_files([test_file])
    finally:
        os.unlink(test_file)
