import unittest


class Testdemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")


def setUp(self) -> None:
    print("setUp")


@classmethod
def tearDownClass(cls) -> None:
    print("tearDownClass")


def tearDown(self) -> None:
    print("tearDown")


def test_sum(self):
    print("test_sum")
    x = 1 + 2
    print(x)
    self.assertEquals(x, 3, f'x={x} expection=3')


def test_dem(self):
    print("test_dem")
    self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
