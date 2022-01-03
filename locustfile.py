from re import T
from locust import HttpUser, task, between
import random

HOST = "http://127.0.0.1:8000/"
#Command:  locust --headless --users 1 --spawn-rate 1 -H "http://127.0.0.1:8000/"

class Test(HttpUser):
    wait_time = between(1, 4)
    def on_start(self):
        self.uvus = "testuvus"+str(random.randint(0,1000))
        self.password = "pass"
        self.logged = False
        #ALERTA: Para comenzar el test se debe tener en la base de datos una categoría llamada "testCategory"
    def on_stop(self):
        pass
    @task
    def login(self):
        response = self.client.get("login")
        csrftoken = response.cookies['csrftoken']
        response = self.client.post("handlelogin",{"uvus":self.uvus,"password":self.password},headers={"X-CSRFToken": csrftoken})
        self.logged=True
        if 'Error al logear' in response.text:
            ret = False
        else:
            ret = True
    @task
    def createUserAndLogIn(self):
        if not self.logged:
            response = self.client.get("admin/usuarios/nuevo")
            csrftoken = response.cookies['csrftoken']
            response = self.client.post("admin/usuarios/handlenuevo",{"uvus":self.uvus,"rol":"SU"},headers={"X-CSRFToken": csrftoken})
            if 'Error al logear' in response.text:
                ret = False
            else:
                ret = True
            print("Created user and was: ", ret)
            response = self.client.get("register")
            csrftoken = response.cookies['csrftoken']
            response = self.client.post("handleregistration",{"uvus":self.uvus,"password":self.password},headers={"X-CSRFToken": csrftoken})
            if 'Error al logear' in response.text:
                ret = False
            else:
                ret = True
            print("Registered user and got: ", ret)
            response = self.client.get("login")
            csrftoken = response.cookies['csrftoken']
            response = self.client.post("handlelogin",{"uvus":self.uvus,"password":self.password},headers={"X-CSRFToken": csrftoken})
            if 'Error al logear' in response.text:
                ret = False
            else:
                ret = True
            print("Logged user and was: ", ret)
            self.logged=True
    @task
    def viewUsers(self):
        self.client.get("admin/usuarios")
    @task 
    def fakeLogin(self):
        response = self.client.post("handlelogin",{"uvus":"hjfhjfdasjhfda","password":"pafdfdsafdasss"})
    @task 
    def viewProducts(self):
        self.client.get("inventario/productos")
    @task 
    def viewNecesidades(self):
        self.client.get("necesidades/necesidades")
    @task
    def viewIndex(self):
        self.client.get("")
    #@task 
    def empty(self):
            response = self.client.get("")
            csrftoken = response.cookies['csrftoken']
            response = self.client.post("",{},headers={"X-CSRFToken": csrftoken})