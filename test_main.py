from main import main

import io

def test_main_with_two_test_cases(monkeypatch, capsys):
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

def test_main_with_invalid_numbers_in_number_of_cases(monkeypatch, capsys):
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

def test_main_with_invalid_numbers_in_test_case(monkeypatch, capsys):
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
    # Arrange
    monkeypatch.setattr('sys.stdin', io.StringIO("""0"""))

    # Act
    main()

    # Assert
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""

def test_main_with_negative_test_cases(monkeypatch, capsys):
    # Arrange
    monkeypatch.setattr('sys.stdin', io.StringIO("""-1"""))

    # Act
    main()

    # Assert
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
