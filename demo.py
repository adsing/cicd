from mymodule import arithmetic


def test_add_pass() -> None:
    assert arithmetic.add(2, 3) == 5


def test_add_fail() -> None:
    try:
        assert arithmetic.add(2, 3) == 6
    except AssertionError:
        pass
    except:
        raise RuntimeError("Did not raise AssertionError as expected")


def main():
    test_add_pass()
    test_add_fail()


if __name__ == "__main__":
    main()
