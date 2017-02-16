import json

from rest_service.resources import app
from rest_service.database import init_db

import unittest


class ArticleTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        init_db()

    def tearDown(self):
        pass

    def test_get_article(self):
        create_result = self._create_article(title='get_test_title',
                                             content='get_test_content')
        get_result = self.app.get('/article/get_test_title')
        self.assertDictEqual(json.loads(get_result.data),
                             json.loads(create_result.data))
        self.assertEqual(get_result.status_code, 200)

    def test_delete_article(self):
        create_result = self._create_article(title='delete_test_title',
                                             content='delete_test_content')
        delete_result = self.app.delete('/article/delete_test_title')
        self.assertDictEqual(json.loads(delete_result.data),
                             json.loads(create_result.data))
        self.assertEqual(delete_result.status_code, 202)

    def test_create_article(self):
        create_result = self._create_article(title='create_test_title',
                                             content='create_test_content')
        self.assertEqual(create_result.status_code, 201)
        list_result = self.app.get('/articles')
        self.assertEqual(len(json.loads(list_result.data)), 1)

    def test_list_articles(self):
        create_result_1 = self._create_article(title='list_test_title_1',
                                               content='list_test_content_1')
        create_result_2 = self._create_article(title='list_test_title_2',
                                               content='list_test_content_2')
        list_result = self.app.get('/articles')
        self.assertEqual(list_result.status_code, 200)

        list_data = json.loads(list_result.data)
        self.assertEqual(len(list_data), 2)

        for article in list_data:
            if article['title'] == 'list_test_title_1':
                self.assertDictEqual(article, json.loads(create_result_1.data))
            else:
                self.assertDictEqual(article, json.loads(create_result_2.data))

    def test_update(self):
        create_result = self._create_article(title='update_test_title',
                                             content='update_test_content')
        update_data = {'title': 'new_update_test_title',
                       'content': 'new_update_test_content'}
        update_result = self.app.post('/article/update_test_title',
                                      data=update_data)

        self.assertEqual(update_result.status_code, 200)
        self.assertDictContainsSubset(update_data,
                                      json.loads(update_result.data))
        self.assertEquals(json.loads(create_result.data)['created_at'],
                          json.loads(update_result.data)['created_at'])

    def _create_article(self, title, content):
        data = {'title': title,
                'content': content}
        return self.app.put('article/{0}'.format(title), data=data)
