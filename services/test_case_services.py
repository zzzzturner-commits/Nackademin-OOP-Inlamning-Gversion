from models.test_case import TestCase
from repository.test_case_repository import TestCaseRepository
from models.test_case_result import TestCaseResult


class TestCaseService:
    def __init__(self, repository: TestCaseRepository):
        self.repository: TestCaseRepository = repository

    def create_test_case(self, testcase: TestCase) -> TestCaseResult:

       if not testcase.title:
           return TestCaseResult(False, "Title is required for the test case.", None)

       if not testcase.purpose:
            return TestCaseResult(False, "Purpose is required for the test case.", None)

       if not testcase.expected_result:
            return TestCaseResult(False, "Expected result is required for the test case.", None)
       
       self.repository.try_create_test_case(testcase)
       return TestCaseResult(True, f"Test case with the '{testcase.title}' has been added successfully.", testcase)
    
    def get_test_cases(self) -> list[TestCase]:
        return self.repository.get_all_test_cases()