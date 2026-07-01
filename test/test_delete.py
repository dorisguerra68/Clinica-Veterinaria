import sys
import os
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_eliminar_raza_exitoso():

    nombre_unico = f"Raza Test {uuid.uuid4().hex[:6]}"
    raza_ficticia = {"nombre_raza": nombre_unico}

    # Registramos la raza
    response_create = client.post("/razas/", json=raza_ficticia)

    datos_creados = response_create.json()
    id_creado = datos_creados.get("id_raza")

    # Ejecutamos el borrado
    response_delete = client.delete(f"/razas/{id_creado}")

    # Comprobamos
    assert response_delete.status_code == 200
    assert response_delete.json() == {"mensaje": "Raza eliminada correctamente"}


def test_eliminar_raza_no_existente():
    id_falso = 99999
    response = client.delete(f"/razas/{id_falso}")

    assert response.status_code == 404
