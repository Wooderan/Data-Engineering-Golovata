import io
import json
from unittest import TestCase, mock
from lesson02.ht_template.job2.dal.local_disk import read_raw_from_disk, save_stg_to_disk, parsed_schema


class ReadRawFromDiskTestCase(TestCase):

    @mock.patch("builtins.open", mock.mock_open(read_data=json.dumps([{"key1": "value1"}, {"key2": "value2"}])))
    def test_successful_data_reading(self):
        # Test reading valid JSON content
        result = read_raw_from_disk("dummy_path.json")
        self.assertEqual(result, [{"key1": "value1"}, {"key2": "value2"}])

    @mock.patch("builtins.open", mock.mock_open(read_data="invalid json"))
    def test_invalid_json_content(self):
        # Test behavior with invalid JSON content
        with self.assertRaises(json.JSONDecodeError):
            read_raw_from_disk("dummy_path.json")

    @mock.patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found_error(self, mock_open):
        # Test behavior when file does not exist
        with self.assertRaises(FileNotFoundError):
            read_raw_from_disk("non_existent_path.json")


class SaveStgToDiskTestCase(TestCase):

    def setUp(self):
        self.json_content = [
            {'client': 'Client A', 'purchase_date': '2023-01-01', 'product': 'Product 1', 'price': 100},
            {'client': 'Client B', 'purchase_date': '2023-01-02', 'product': 'Product 2', 'price': 200}
        ]
        self.test_path = "test_file.avro"

    @mock.patch('lesson02.ht_template.job2.dal.local_disk.open', new_callable=mock.mock_open)
    @mock.patch('lesson02.ht_template.job2.dal.local_disk.writer')
    def test_write_to_file(self, mock_writer, mock_open):
        # Test if data is written to file
        save_stg_to_disk(self.json_content, self.test_path)

        # Check if file write was called
        mock_open.assert_called_with(self.test_path, 'wb')

    @mock.patch('lesson02.ht_template.job2.dal.local_disk.open', new_callable=mock.mock_open)
    @mock.patch('lesson02.ht_template.job2.dal.local_disk.writer')
    def test_avro_serialization(self, mock_writer, mock_open):
        # Test Avro serialization
        save_stg_to_disk(self.json_content, self.test_path)

        # Check if Avro writer was called with correct parameters
        mock_writer.assert_called_once()
        args, kwargs = mock_writer.call_args
        self.assertEqual(args[1], parsed_schema)          # Check if second arg is schema
        self.assertEqual(args[2], self.json_content)      # Check if third arg is data

    def test_handling_invalid_json_content(self):
        # Test behavior with invalid JSON content
        invalid_content = [{'invalid': 'data'}]  # Data that doesn't conform to the schema

        with self.assertRaises(ValueError):
            save_stg_to_disk(invalid_content, self.test_path)