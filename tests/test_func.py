from pfirsich.func import Func

@Func
def foo(a: int):
    return a + 1

@Func
def bar(a: int) -> str:
    return f"{a}"


def test_add():
    f = foo | bar
    assert f(1) == "2"
