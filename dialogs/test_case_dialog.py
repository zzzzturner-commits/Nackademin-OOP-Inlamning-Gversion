from utils.console_helper import pause, clear_screen, required_input
from models.test_case import TestCase
from services.test_case_services import TestCaseService

class TestCaseDialog:
    def __init__(self, test_case_service: TestCaseService):
        self.test_case_service = test_case_service

    def main_menu(self):

        while True:
            clear_screen()

            print("#### Main menu - Test case registrator")
            print("1. Create a test case.")
            print("2. Show a list of test cases.")
            print("0. Exit")

            option = input("Choose an option: ").strip()

            match option:

                case "1":
                    self.show_create_test_case()

                case "2":
                    self.show_test_cases()

                case "0":
                    return

                case _:
                    print("Invalid option. Please try again.")
                    pause()

    def show_create_test_case(self):

        testcase = TestCase()
        testcase.title = required_input("Enter a title for the test case.")
        testcase.purpose = required_input("Enter a purpose for the test case.")
        testcase.expected_result = required_input("Enter the expected result of the test case.")

        result = self.test_case_service.create_test_case(testcase)
        print(result.message)
        pause()

    def show_test_cases(self):

        clear_screen()
        print("#### Test case list - Test case registrator ####")

        result = self.test_case_service.get_test_cases()

        for testcase in result:
            print(testcase.title)

        pause()