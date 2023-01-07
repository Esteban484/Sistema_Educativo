try:
    from front import app
    import unittest
    import requests

except Exception as e:
    print("Módulos faltantes {}".format(e))

#CLASE PARA REALIZAR LAS PRUEBAS UNITARIAS POR FUNCIONES
class TestAPI(unittest.TestCase):
        URL = "http://127.0.0.1:5000/"

        update_data = {
            "name":"Updated",
            "apellido":"Pruebas"
        }
        def test_1_index(self):
            resp = requests.get(self.URL)
            self.assertEqual(resp.status_code,200)
            print("Test 1 Index completado")

        def test_2_cursos(self):
            resp = requests.get(self.URL+"/cursos")
            self.assertEqual(resp.status_code,200)
            print("Test 2 Cursos completado")

        def test_3_about(self):
            resp = requests.get(self.URL+"/about")
            self.assertEqual(resp.status_code,200)
            print("Test 3 About completado")
        
        def test_4_insc(self):
            resp = requests.get(self.URL+"/inscripciones")
            self.assertEqual(resp.status_code,200)
            print("Test 4 Inscripciones completado")
        
        def test_login(self):
            resp = requests.get(self.URL+"/login")
            self.assertEqual(resp.status_code,200)
            print("Test 5 LOGIN completado")
        
        def test_maestro(self):
            resp = requests.get(self.URL+"/maestro")
            self.assertEqual(resp.status_code,200)
            print("Test 6 Maestro completado")

        def test_admin(self):
            resp = requests.get(self.URL+"/administrador")
            self.assertEqual(resp.status_code,200)
            print("Test 7 Administrador completado")

        def test_admin_inscEstudiante(self):
            resp = requests.get(self.URL+"/inscribirEstudiante")
            self.assertEqual(resp.status_code,200)
            print("Test 8 Administrador/Inscribir Estudiante completado")

        def test_admin_inscDocente(self):
            resp = requests.get(self.URL+"/inscribirDocente")
            self.assertEqual(resp.status_code,200)
            print("Test 9 Administrador/Inscribir Docente completado")

        def test_info(self):
            resp = requests.get(self.URL+"/info")
            self.assertEqual(resp.status_code,200)
            print("Test 10 Informacion completado")

if __name__ == "__main__":
    tester = TestAPI()
    tester.test_1_index()
    tester.test_2_cursos()
    tester.test_3_about()
    tester.test_4_insc()
    tester.test_login()
    tester.test_maestro()
    tester.test_admin()
    tester.test_admin_inscEstudiante()
    tester.test_admin_inscDocente()
    tester.test_info()
