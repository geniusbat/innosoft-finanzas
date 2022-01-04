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


class InventarioVisualTest(StaticLiveServerTestCase):
    def setUp(self):
        super().setUp()

        options = webdriver.ChromeOptions()
        options.headless = False
        options.add_argument('--disable-gpu')
        options.add_argument("--start-maximized")

        self.base = BaseTestCase()
        self.base.setUp()

        self.driver = webdriver.Chrome(options=options)

        self.vars = {}

    def tearDown(self):
        super().tearDown()
        self.driver.quit()
        self.base.tearDown()

    def get_rows_tabla(self, idTabla):
        tabla = self.driver.find_element(By.ID, idTabla)
        rows = len(tabla.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr'))

        rowsTablaEmpty = tabla.find_element(By.TAG_NAME, 'tbody').find_elements(By.CLASS_NAME, 'dataTables_empty')

        if rowsTablaEmpty is not None and len(rowsTablaEmpty) > 0:
            rows -= 1

        return rows

    def test_1_createCategoria(self):
        #self.driver.get('http://127.0.0.1:8000/inventario/productos')
        #self.driver.get(f'{self.live_server_url}/inventario/productos')
        self.driver.get(settings.BASE_LOCAL_URL + '/inventario/productos')

        rowsCategoriasBefore = self.get_rows_tabla('tablaCategorias')

        self.driver.find_element(By.ID, 'botonAniadirCategoria').click()

        time.sleep(1)

        self.driver.find_element(By.ID, 'categoria').click()
        self.driver.find_element(By.ID, 'categoria').send_keys("__TEST__CATEGORIA")
        self.driver.find_element(By.ID, '_saveCategoria').click()

        rowsCategoriasAfter = self.get_rows_tabla('tablaCategorias')

        self.assertGreater(rowsCategoriasAfter, rowsCategoriasBefore)

    def test_2_createProducto(self):
        # self.driver.get('http://127.0.0.1:8000/inventario/productos')
        # self.driver.get(f'{self.live_server_url}/inventario/productos')
        self.driver.get(settings.BASE_LOCAL_URL + '/inventario/productos')

        rowsProductosBefore = self.get_rows_tabla('tablaProductos')

        self.driver.find_element(By.ID, 'botonAniadirProducto').click()

        time.sleep(1)

        self.driver.find_element(By.ID, 'nombreInput').click()
        self.driver.find_element(By.ID, 'nombreInput').send_keys("__TEST__PRODUCTO")
        self.driver.find_element(By.ID, 'unidadesInput').click()
        self.driver.find_element(By.ID, 'unidadesInput').send_keys("10")
        self.driver.find_element(By.ID, 'valorMonetarioInput').click()
        self.driver.find_element(By.ID, 'valorMonetarioInput').send_keys("10")
        self.driver.find_element(By.ID, '_saveProducto').click()

        rowsProductosAfter = self.get_rows_tabla('tablaProductos')

        self.assertGreater(rowsProductosAfter, rowsProductosBefore)

    def test_3_eliminarProducto(self):
        #self.driver.get('http://127.0.0.1:8000/inventario/productos')
        #self.driver.get(f'{self.live_server_url}/inventario/productos')
        self.driver.get(settings.BASE_LOCAL_URL + '/inventario/productos')

        rowsCategoriasBefore = self.get_rows_tabla('tablaProductos')

        self.driver.find_element(By.CLASS_NAME, 'eliminarProducto').click()

        rowsCategoriasAfter = self.get_rows_tabla('tablaProductos')

        self.assertGreater(rowsCategoriasBefore, rowsCategoriasAfter)

    def test_4_eliminarCategoria(self):
        #self.driver.get('http://127.0.0.1:8000/inventario/productos')
        #self.driver.get(f'{self.live_server_url}/inventario/productos')
        self.driver.get(settings.BASE_LOCAL_URL + '/inventario/productos')

        rowsCategoriasBefore = self.get_rows_tabla('tablaCategorias')

        self.driver.find_element(By.CLASS_NAME, 'eliminarCategoria').click()

        rowsCategoriasAfter = self.get_rows_tabla('tablaCategorias')

        self.assertGreater(rowsCategoriasBefore, rowsCategoriasAfter)
