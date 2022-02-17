import unittest

def unique(str):
    char_set = {}
    for char in str:
        if char in char_set:
            return False
        char_set[char] = True
    return True
class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4321'), ('4518'), ('')]
    dataF = [('232ds2'), ('sfsgasga')]

    def test_unique(self):
        #true check
        for test_case in self.dataT:
            actualResult = unique(test_case)
            self.assertTrue(actualResult)
        #false
        for test_case in self.dataF:
            actualResult = unique(test_case)
            self.assertFalse(actualResult)
if __name__ == "__main__":
    # str = '214652'
    # print(unique(str))
    unittest.main()