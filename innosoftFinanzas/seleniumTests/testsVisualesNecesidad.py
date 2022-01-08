from django.test import TestCase
from necesidades.models import Comite, Necesidad
import json
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
class NecesidadVisualTest(StaticLiveServerTestCase):
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

    def createComite(self):
        #no hay delete comite por ahora asi que da error si se hace otro test
        #self.driver.get('http://127.0.0.1:8000/inventario/productos')
        #self.driver.get(f'{self.live_server_url}/inventario/productos')
        self.driver.get("{}/necesidades/necesidades".format(self.live_server_url))

        self.driver.find_element(By.ID, 'botonAniadirComite').click()

        time.sleep(1)

        self.driver.find_element(By.ID, 'comite').click()
        self.driver.find_element(By.ID, 'comite').send_keys("comitePrueba")
        self.driver.find_element(By.ID, '_save').click()

        tablaCategoria = self.driver.find_element(By.ID, 'tablaComites')
        rowsCategorias = tablaCategoria.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

        self.assertTrue(len(rowsCategorias) > 0)

    def createNecesidad(self):
        #no hay delete necesidad por ahora
        #self.driver.get('http://127.0.0.1:8000/inventario/productos')
        #self.driver.get(f'{self.live_server_url}/inventario/productos')
        self.driver.get("{}/necesidades/necesidades".format(self.live_server_url))

        self.driver.find_element(By.ID, 'botonAniadirNecesidad').click()

        time.sleep(1)

        self.driver.find_element(By.ID, 'nombreInput').click()
        self.driver.find_element(By.ID, 'nombreInput').send_keys("nombrePrueba1")
        self.driver.find_element(By.ID, 'comiteInput').click()
        self.driver.find_element(By.ID, 'comitePrueba').click()
        self.driver.find_element(By.ID, 'cantidadInput').click()
        self.driver.find_element(By.ID, 'cantidadInput').send_keys("21")
        self.driver.find_element(By.ID, 'descripcionInput').click()
        self.driver.find_element(By.ID, 'descripcionInput').send_keys("DescripcionPrueba1")
        time.sleep(1)
        self.driver.find_element(By.ID, 'save').click()

        tablaCategoria = self.driver.find_element(By.ID, 'tablaNecesidad')
        rowsCategorias = tablaCategoria.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

        self.assertTrue(len(rowsCategorias) > 0)

    def editNecesidad(self):
        self.driver.get("{}/necesidades/necesidades".format(self.live_server_url))

        rowsNecesidadesBefore = self.get_rows_tabla('tablaNecesidad')

        self.driver.find_element(By.CLASS_NAME, 'modificarNecesidad').click()

        time.sleep(2)

        self.driver.find_element(By.ID, 'formModificarNecesidad').find_element(By.ID, 'nombreInput').click()
        self.driver.find_element(By.ID, 'formModificarNecesidad').find_element(By.ID, 'nombreInput').send_keys("__EDIT")
        self.driver.find_element(By.ID, 'formModificarNecesidad').find_element(By.ID, '_editNecesidad').click()

        rowsNecesidadesAfter = self.get_rows_tabla('tablaNecesidad')

        tabla = self.driver.find_element(By.ID, 'tablaNecesidad')
        rows = tabla.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

        textoNecesidad = [r.text.split()[0] for r in rows]

        self.assertEqual(rowsNecesidadesBefore, rowsNecesidadesAfter)
        self.assertTrue('nombrePrueba1__EDIT' in textoNecesidad)

    def eliminarNecesidad(self):
        self.driver.get("{}/necesidades/necesidades".format(self.live_server_url))

        rowsCategoriasBefore = self.get_rows_tabla('tablaNecesidad')

        self.driver.find_element(By.CLASS_NAME, 'eliminarNecesidad').click()

        rowsCategoriasAfter = self.get_rows_tabla('tablaNecesidad')

        self.assertGreater(rowsCategoriasBefore, rowsCategoriasAfter)

    def test_create_comite(self):
        self.createComite()

    def test_create_necesidad(self):
        self.createComite()
        self.createNecesidad()

    def test_edit_necesidad(self):
        self.createComite()
        self.createNecesidad()
        self.editNecesidad()

    def test_eliminar_necesidad(self):
        self.createComite()
        self.createNecesidad()
        self.eliminarNecesidad()