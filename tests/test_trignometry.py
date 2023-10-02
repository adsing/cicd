from mymodule import trignometry


def test_tan_pass():
    x_radians = 0.23
    assert trignometry.sine(x_radians) / trignometry.cosine(
        x_radians
    ) == trignometry.tangent(x_radians)
