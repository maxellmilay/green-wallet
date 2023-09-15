# -*- coding:utf-8 -*-
from django.test import TestCase

from sileo.exceptions import APIException, PermissionDenied


class APIExceptionTestCase(TestCase):

    def test_init(self):
        """ Test case for APIException's init method """
        e = APIException()
        self.assertEqual({}, e.extras)
        self.assertEqual(404, e.status)
        self.assertEqual('', e.detail)
        self.assertEqual('', e.code)
        e = APIException(detail='Test', code='test', status=302,
                         extras={'test': 1})
        self.assertEqual({'test': 1}, e.extras)
        self.assertEqual('Test', e.detail)
        self.assertEqual('test', e.code)
        self.assertEqual(302, e.status)

    def test_get_full_detail(self):
        """ Test case for get_full_details method of the APIException """
        e = APIException(detail='Test', code='test', status=302,
                         extras={'test': 1})
        expected = {
            'test': 1,
            'detail': 'Test',
            'code': 'test'
        }
        self.assertEqual(expected, e.get_full_details())

    def test_get_context(self):
        """ Test case for get_context method of APIException """
        e = APIException(detail='Test', code='test', status=302,
                         extras={'test': 1})
        expected = {
            'status_code': 302,
            'data': {
                'test': 1,
                'detail': 'Test',
                'code': 'test'
            }
        }
        self.assertEqual(expected, e.get_context())


class APIExceptionSubclassTestCase(TestCase):

    def test_subclass_defaults(self):
        e = PermissionDenied()
        self.assertEqual({}, e.extras)
        self.assertEqual(403, e.status)
        self.assertEqual('You do not have permission to access the resource.',
                         e.detail)
        self.assertEqual('permission_denied', e.code)
