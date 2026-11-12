from models.test_case import TestCase

class TestCaseRepository:
    def __init__(self):
        self.__cases: list[TestCase] = []
        
    def try_create_test_case(self, testcase: TestCase) -> None:
        self.__cases.append(testcase)

    def get_all_test_cases(self) -> list[TestCase]:
        return self.__cases.copy()