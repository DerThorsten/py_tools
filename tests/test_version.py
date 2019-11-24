import py_tools


class TestVersion(object):

    def test_version(self):
        v = py_tools.__version__
        assert v == '0.1.132'
