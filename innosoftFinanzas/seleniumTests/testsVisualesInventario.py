import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.tests import BaseTestCase


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

    def createCategoria(self):
        self.driver.get("{}/inventario/productos".format(self.live_server_url))

        rowsCategoriasBefore = self.get_rows_tabla('tablaCategorias')

        self.driver.find_element(By.ID, 'botonAniadirCategoria').click()

        time.sleep(1)

        self.driver.find_element(By.ID, 'categoria').click()
        self.driver.find_element(By.ID, 'categoria').send_keys("__TEST__CATEGORIA")
        self.driver.find_element(By.ID, '_saveCategoria').click()

        rowsCategoriasAfter = self.get_rows_tabla('tablaCategorias')

        self.assertGreater(rowsCategoriasAfter, rowsCategoriasBefore)

    def createProducto(self):
        self.driver.get("{}/inventario/productos".format(self.live_server_url))

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

    def editProducto(self):
        self.driver.get("{}/inventario/productos".format(self.live_server_url))

        rowsProductosBefore = self.get_rows_tabla('tablaProductos')

        self.driver.find_element(By.CLASS_NAME, 'modificarProducto').click()

        time.sleep(2)

        self.driver.find_element(By.ID, 'formModificarProducto').find_element(By.ID, 'nombreInput').click()
        self.driver.find_element(By.ID, 'formModificarProducto').find_element(By.ID, 'nombreInput').send_keys("__EDIT")
        self.driver.find_element(By.ID, 'formModificarProducto').find_element(By.ID, '_editProducto').click()

        rowsProductosAfter = self.get_rows_tabla('tablaProductos')

        tabla = self.driver.find_element(By.ID, 'tablaProductos')
        rows = tabla.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

        textoProducto = [r.text.split()[0] for r in rows]

        self.assertEqual(rowsProductosBefore, rowsProductosAfter)
        self.assertTrue('__TEST__PRODUCTO__EDIT' in textoProducto)

    def eliminarProducto(self):
        self.driver.get("{}/inventario/productos".format(self.live_server_url))

        rowsCategoriasBefore = self.get_rows_tabla('tablaProductos')

        self.driver.find_element(By.CLASS_NAME, 'eliminarProducto').click()

        rowsCategoriasAfter = self.get_rows_tabla('tablaProductos')

        self.assertGreater(rowsCategoriasBefore, rowsCategoriasAfter)

    def eliminarCategoria(self):
        self.driver.get("{}/inventario/productos".format(self.live_server_url))

        rowsCategoriasBefore = self.get_rows_tabla('tablaCategorias')

        self.driver.find_element(By.CLASS_NAME, 'eliminarCategoria').click()

        rowsCategoriasAfter = self.get_rows_tabla('tablaCategorias')

        self.assertGreater(rowsCategoriasBefore, rowsCategoriasAfter)

    def test_createCategoria(self):
        self.createCategoria()

    def test_createProducto(self):
        self.createCategoria()
        self.createProducto()

    def test_editProducto(self):
        self.createCategoria()
        self.createProducto()
        self.editProducto()

    def test_eliminarProducto(self):
        self.createCategoria()
        self.createProducto()
        self.eliminarProducto()

    def test_eliminarCategoria(self):
        self.createCategoria()
        self.eliminarCategoria()
