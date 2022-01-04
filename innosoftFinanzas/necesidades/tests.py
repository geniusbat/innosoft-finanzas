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
class NecesidadesTest(TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()
    def testComite(self):
        "crear comite"
        c = Comite(comite="igualdad")
        c.save()
        self.assertTrue(Comite.objects.all().filter(comite="igualdad").exists())
    def testNecesidad(self):
        "crear necesidad"
        c = Comite(comite="igualdad")
        c.save()
        n = Necesidad(nombre="Prueba 1", cantidadNecesitada=2, comite=c, descripcion="test")
        n.save()
        self.assertTrue(Necesidad.objects.all().filter(nombre="Prueba 1").exists())
        self.assertTrue(Necesidad.objects.all().filter(comite=c).exists())
    def testfromformNecesidad(self):
        c = Comite(comite="igualdad")
        c.save()
        n = Necesidad(nombre="Prueba 1", cantidadNecesitada=2, comite=c, descripcion="test")
        n.save()
        self.assertTrue(Necesidad.objects.all().filter(nombre="Prueba 1").exists())
        self.assertTrue(Necesidad.objects.all().filter(comite=c).exists())
    def test_new_necesidades(self):
        "ver nueva necesidades"
        resp = self.client.get('/necesidades/nuevaNecesidad')
        self.assertEqual(resp.status_code, 200)

    def test_list_necesidades(self):
        "ver lista de necesidades"
        resp = self.client.get('/necesidades/necesidades')
        self.assertEqual(resp.status_code, 200)

    def test_form_comite(self):
        "creaar comite"
        resp = self.client.post('/necesidades/nuevoComite', {'comite': 'igualdad'})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Comite.objects.all().filter(comite="igualdad").exists())
    def test_form_necesidad(self):
        "creaar necesidad"
        c = Comite(comite="igualdad")
        c.save()
        resp = self.client.post('/necesidades/nuevaNecesidad', {'nombre':'probando', 'comite': "igualdad", 'cantidadNecesitada': '12', 'descripcion': 'a'})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Necesidad.objects.all().filter(nombre="probando").exists())

    def test_edit_necesidad(self):
        '''
        Edit necesidad
        comprueba el modal de modificar necesidad
        '''

        c = Comite(comite="igualdad")
        c.save()
        n = Necesidad(nombre="Prueba 1", cantidadNecesitada=2, comite=c, descripcion="test")
        n.save()
        resp = self.client.get('/necesidades/modificar/' + str(n.id))
        data = json.loads(resp.content)
        s = json.dumps(data, indent=4, sort_keys=True)
        y = json.loads(s)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(y["nombre"], 'Prueba 1')
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

    def test_createComite(self):
        #no hay delete comite por ahora
        #self.driver.get('http://127.0.0.1:8000/inventario/productos')
        #self.driver.get(f'{self.live_server_url}/inventario/productos')
        self.driver.get(settings.BASE_LOCAL_URL + '/necesidades/necesidades')

        self.driver.find_element(By.ID, 'botonAniadirComite').click()

        time.sleep(1)

        self.driver.find_element(By.ID, 'comite').click()
        self.driver.find_element(By.ID, 'comite').send_keys("comitePrueba")
        self.driver.find_element(By.ID, '_save').click()

        tablaCategoria = self.driver.find_element(By.ID, 'tablaComites')
        rowsCategorias = tablaCategoria.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

        self.assertTrue(len(rowsCategorias) > 0)

