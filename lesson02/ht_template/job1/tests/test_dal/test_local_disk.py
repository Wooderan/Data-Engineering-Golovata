"""
Tests dal.local_disk.py module
"""
import json
import os
from unittest import TestCase, mock

from lesson02.ht_template.job1.dal.local_disk import save_to_disk


class SaveToDiskTestCase(TestCase):
    """
    Test dal.local_disk.save_to_disk function.
    """

    def setUp(self):
        # Setup a temporary file path
        self.test_path = "test_file.json"
        self.test_data = [{"key1": "value1"}, {"key2": "value2"}]

    def tearDown(self):
        # Clean up the file after each test
        if os.path.exists(self.test_path):
            os.remove(self.test_path)

    def test_write_json_to_file(self):
        # Test if JSON content is correctly written to the file
        save_to_disk(self.test_data, self.test_path)
        with open(self.test_path, "r") as f:
            content = f.read()
        self.assertEqual(content, json.dumps(self.test_data))

    def test_invalid_json_content(self):
        # Test behavior with invalid json content, e.g., a string instead of a list
        with self.assertRaises(TypeError):
            save_to_disk("invalid data", self.test_path)

    def test_file_creation(self):
        # Test if file is created
        save_to_disk(self.test_data, self.test_path)
        self.assertTrue(os.path.exists(self.test_path))

    def test_file_content_matches(self):
        # Test if file content matches the json content
        save_to_disk(self.test_data, self.test_path)
        with open(self.test_path, "r") as f:
            content = json.load(f)
        self.assertEqual(content, self.test_data)