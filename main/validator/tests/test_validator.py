import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class FormulaValidationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_valid_formula_with_brackets(self):
        data = {"formula": "(a + b)"}
        response = self.client.post("/formula_validation/", json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)

    def test_valid_formula_without_brackets(self):
        data = {"formula": "a + b"}
        response = self.client.post("formula_validation/", json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_formula(self):
        data = {"formula": "(a + b) * [c - {d / e}"}
        response = self.client.post("formula_validation/", json.dumps(data), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_empty_formula(self):
        data = {"formula": ""}
        response = self.client.post("formula_validation/", json.dumps(data), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_no_formula(self):
        data = {}
        response = self.client.post("formula_validation/", json.dumps(data), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
