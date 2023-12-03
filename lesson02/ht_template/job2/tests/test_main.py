"""
Tests for main.py
"""
from unittest import TestCase, mock

# NB: avoid relative imports when you will write your code
from .. import main


class MainFunctionTestCase(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        main.app.testing = True
        cls.client = main.app.test_client()

    def test_return_400_stg_dir_param_missed(self):
        """
        Raise 400 HTTP code when no 'date' param
        """
        resp = self.client.post(
            '/',
            json={
                'raw_dir': '/foo/bar/',
                # no 'date' set!
            },
        )

        self.assertEqual(400, resp.status_code)

    def test_return_400_raw_dir_param_missed(self):
        resp = self.client.post(
            '/',
            json = {
                'sth_dir': '/foo/bar/'
            }
        )

        self.assertEqual(400, resp.status_code)

    @mock.patch('lesson02.ht_template.job2.main.stage_sales_on_local_disk')
    def test_stage_sales_on_local_disk(
            self,
            stage_sales_on_local_disk_mock: mock.MagicMock
    ):
        """
        Test whether api.get_sales is called with proper params
        """
        fake_raw_dir = '/foo/bar/'
        fake_stg_dir = '/bar/foo/'
        self.client.post(
            '/',
            json={
                'raw_dir': fake_raw_dir,
                'stg_dir': fake_stg_dir,
            },
        )

        stage_sales_on_local_disk_mock.assert_called_with(
            raw_dir=fake_raw_dir,
            stg_dir=fake_stg_dir,
        )

    @mock.patch('lesson02.ht_template.job2.main.stage_sales_on_local_disk')
    def test_return_201_when_all_is_ok(
            self,
            stage_sales_on_local_disk_mock: mock.MagicMock
    ):
        resp = self.client.post(
            '/',
            json={
                'raw_dir': '/tmp/data-engineering/raw',
                'stg_dir': '/tmp/data-engineering/stg',
            },
        )
        self.assertEqual(201, resp.status_code)