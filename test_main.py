# -*- coding: utf-8 -*-
"""Test suite of the solution to ensure that it works as expected.

Solution and a small pytest suite can be found on Github.
See: https://github.com/OliverVea/hennge-test.
"""

import io

from main import main


def test_main_with_two_test_cases(monkeypatch, capsys):
    """Happy-path test confirming that the main method works as expected."""

    # Arrange
    monkeypatch.setattr('sys.stdin', io.StringIO("""2
    5
    17 -3 5 0 -100
    3
    14 14 -28"""))

    # Act
    main()

    # Assert
    out, err = capsys.readouterr()
    assert out == "22\n28\n"
    assert err == ""

def test_main_with_invalid_number_in_number_of_cases(monkeypatch, capsys):
    """Tests that the solution does not break with invalid input."""

    # Arrange
    monkeypatch.setattr('sys.stdin', io.StringIO("""a
    2
    5 7"""))

    # Act
    main()

    # Assert
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""

def test_main_with_invalid_number_in_test_case_numbers_count(monkeypatch, capsys):
    """Tests that the solution does not break with invalid input."""

    # Arrange
    monkeypatch.setattr('sys.stdin', io.StringIO("""1
    a
    5 7"""))

    # Act
    main()

    # Assert
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""

def test_main_with_invalid_numbers_in_test_case(monkeypatch, capsys):
    """Tests that the solution does not break with invalid input."""
    # Arrange
    monkeypatch.setattr('sys.stdin', io.StringIO("""1
    2
    5 a"""))

    # Act
    main()

    # Assert
    out, err = capsys.readouterr()
    assert out == "5\n"
    assert err == ""

def test_main_with_no_test_cases(monkeypatch, capsys):
    """Tests that the solution does not break with invalid input."""
    # Arrange
    monkeypatch.setattr('sys.stdin', io.StringIO("""0"""))

    # Act
    main()

    # Assert
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""

def test_main_with_negative_test_cases(monkeypatch, capsys):
    """Tests that the solution does not break with invalid input."""
    # Arrange
    monkeypatch.setattr('sys.stdin', io.StringIO("""-1"""))

    # Act
    main()

    # Assert
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
