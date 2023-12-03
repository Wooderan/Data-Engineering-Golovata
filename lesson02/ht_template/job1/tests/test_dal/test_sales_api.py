"""
Tests sales_api.py module.
"""
from unittest import TestCase, mock

# NB: avoid relative imports when you will write your code:
from lesson02.ht_template.job1.dal.sales_api import get_sales


class GetSalesTestCase(TestCase):
    """
    Test sales_api.get_sales function.
    """

    @mock.patch('lesson02.ht_template.job1.dal.sales_api.requests.get')
    def test_successful_data_retrieval(self, mock_get):
        # Define the sequence of responses: 200 on the first call, 404 on the second call
        mock_get.side_effect = [
            mock.Mock(status_code=200, json=lambda: {"data": "some data"}),
            mock.Mock(status_code=404)
        ]

        # Call the function
        result = get_sales("2023-01-01")

        # Assert the results
        self.assertEqual(result, [{"data": "some data"}])

    @mock.patch('lesson02.ht_template.job1.dal.sales_api.requests.get')
    def test_empty_results(self, mock_get):
        # Define the sequence of responses: 200 on the first call, 404 on the second call
        mock_get.side_effect = [
            mock.Mock(status_code=200, json=lambda: {}),
            mock.Mock(status_code=404)
        ]

        # Call the function
        result = get_sales("2023-01-01")

        # Assert that result is empty
        self.assertEqual(result, [{}])

    @mock.patch('lesson02.ht_template.job1.dal.sales_api.requests.get')
    def test_api_error_handling(self, mock_get):
        # Mock an API error response
        mock_get.return_value.status_code = 500

        # Call the function
        result = get_sales("2023-01-01")

        # Assert that result is empty or as expected in case of an error
        self.assertEqual(result, [])

    @mock.patch('lesson02.ht_template.job1.dal.sales_api.requests.get')
    def test_pagination_handling(self, mock_get):
        # Mock multiple page responses
        mock_get.side_effect = [
            mock.Mock(status_code=200, json=lambda: {"data": "page 1"}),
            mock.Mock(status_code=200, json=lambda: {"data": "page 2"}),
            mock.Mock(status_code=404)  # Simulate end of pages
        ]

        # Call the function
        result = get_sales("2023-01-01")

        # Assert the results are aggregated from multiple pages
        self.assertEqual(result, [{"data": "page 1"}, {"data": "page 2"}])

