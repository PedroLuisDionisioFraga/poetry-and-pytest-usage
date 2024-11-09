class BaseTest:
    def assert_equal(self, value, expected, message=None):
        assert value == expected

    def assert_not_equal(self, value, expected, message=None):
        assert value != expected
