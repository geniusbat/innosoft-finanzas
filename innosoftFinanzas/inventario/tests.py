import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.tests import BaseTestCase
from innosoftFinanzas import settings
from inventario.models import Producto, Categoria
import json
# Create your tests here.
from django.test import TestCase


class InventarioTest(TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_create_categoria(self):
        c = Categoria(categoria="Prueba")
        c.save()
        self.assertTrue(Categoria.objects.all().filter(categoria="Prueba").exists())

    def test_create_producto(self):
        c = Categoria(categoria="Prueba")
        c.save()
        p = Producto(nombre="Prueba 1", categoria=c, unidades=1, valorMonetario=12, descripcion="holaaa")
        p.save()
        self.assertTrue(Producto.objects.all().filter(nombre="Prueba 1").exists())
        self.assertTrue(Producto.objects.all().filter(categoria=c).exists())

    def test_create_producto_from_form(self):
        c = Categoria(categoria="Prueba")
        c.save()
        p = Producto(nombre="Prueba 1", categoria=c, unidades=1, valorMonetario=12, descripcion="holaaa")
        p.save()
        self.assertTrue(Producto.objects.all().filter(nombre="Prueba 1").exists())
        self.assertTrue(Producto.objects.all().filter(categoria=c).exists())

    def test_list_productos(self):
        resp = self.client.get('/inventario/productos')
        self.assertEqual(resp.status_code, 200)

    def test_form_categoria(self):
        resp = self.client.post('/inventario/nuevaCategoria', {'categoria': 'fred'})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Categoria.objects.all().filter(categoria="fred").exists())

    def test_form_producto(self):
        c = Categoria(categoria="Prueba")
        c.save()
        resp = self.client.post('/inventario/nuevoProducto',
                                {'nombre': 'probando', 'categoria': "Prueba", 'unidades': '12', 'valorMonetario': '12',
                                 'descripcion': 'a'})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Producto.objects.all().filter(nombre="probando").exists())

    def test_edit_producto(self):
        c = Categoria(categoria="Prueba")
        c.save()
        p = Producto(nombre="Prueba 1", categoria=c, unidades=1, valorMonetario=12, descripcion="holaaa")
        p.save()
        resp = self.client.get('/inventario/modificarProducto/' + str(p.id))
        data = json.loads(resp.content)
        s = json.dumps(data, indent=4, sort_keys=True)
        y = json.loads(s)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(y["nombre"], 'Prueba 1')
