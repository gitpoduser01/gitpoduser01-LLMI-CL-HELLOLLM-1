"""
This file will contain test cases for the automatic evaluation of your
solution in main/lab.py. You should not modify the code in this file. You should
also manually test your solution by running main/app.py.
"""
import os
import unittest
import requests
# import sys
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
# sys.path.append(project_root)

from src.main.lab import sample, lab


class TestLLMResponse(unittest.TestCase):
    """
    This test will verify that the provided sample LLM API call works. If it does not
    work, this may be because the API key is invalid, or the service may be down.
    If that is the case, this lab may not be completable.
    """

    def test_llm_sanity_check(self):
        result = sample()
        self.assertIsInstance(result, requests.models.Response)
        self.assertTrue(result.status_code == 200)

    """
    The variable returned from the lab1 method should be an HTTP response, with a status
    200. If the status is 400, then your request was incorrectly formatted.
    """

    def test_lab1_200_response(self):
        result = lab()
        self.assertIsInstance(result, requests.models.Response)
        self.assertTrue(result.status_code == 200)

    """
    The JSON of the response returned from the lab1 method should contain "hello world"
    (not case or punctuation sensitive.)
    """

    def test_hello_world_response(self):
        result = lab()
        result = str(result.json()).lower()
        self.assertIn("hello", result)  # Verifies if "hello" is present in the result
        self.assertIn("world", result)  # Verifies if "world" is present in the result

    """
        The variable returned from the lab1 method should be an HTTP response, with a status
        200. If the status is 400, then your request was incorrectly formatted.
        """


if __name__ == '__main__':
    unittest.main()
