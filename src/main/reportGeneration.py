import coverage
import os
import sys

def generate_coverage_report(main_code_path, test_code_path):
    # Initialize coverage
    cov = coverage.Coverage()

    # Start coverage measurement
    cov.start()

    # Import the test code
    test_directory = os.path.dirname(test_code_path)
    test_file_name = os.path.basename(test_code_path)
    test_module_name = os.path.splitext(test_file_name)[0]
    if test_directory not in sys.path:
        sys.path.append(test_directory)
    __import__(test_module_name)

    # Stop coverage measurement
    cov.stop()

    # Analyze coverage and generate report
    cov.save()
    cov.report()

if __name__ == "__main__":
    # File paths for main code and test code
    main_code_path = "/./src/main/main.py"
    test_code_path = "./test/testmain.py"

    generate_coverage_report(main_code_path, test_code_path)
