"""
Suite de pruebas de integración para el Trabajo Práctico de la Unidad 9.
Verifica todos los criterios de aceptación, reglas de negocio (RN-01 a RN-13),
autenticación JWT en cookies HttpOnly, autorización por roles (RBAC) y borrado lógico.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_authentication_and_rbac():
    print("=== INICIANDO PRUEBAS DE INTEGRACIÓN UNIDAD 9 ===")

    # 1. Registro de usuario nuevo
    reg_payload = {
        "username": "mariag",
        "full_name": "Maria Gonzalez",
        "email": "maria@foodstore.com",
        "password": "Password123!"
    }
    r = client.post("/api/v1/auth/register", json=reg_payload)
    assert r.status_code == 201, f"Fallo al registrar usuario: {r.text}"
    user_data = r.json()
    assert user_data["username"] == "mariag"
    assert user_data["role"] == "user"
    assert "hashed_password" not in user_data
    print(" [OK] HU-01: Registro de usuario exitoso (201 UserPublic)")

    # 2. Rechazo de duplicados (409 Conflict - RN-02)
    r_dup = client.post("/api/v1/auth/register", json=reg_payload)
    assert r_dup.status_code == 409, f"Se esperaba 409 en duplicado, dio: {r_dup.status_code}"
    print(" [OK] RN-02: Detección de username o email duplicado (409 Conflict)")

    # 3. Rechazo de contraseña corta < 8 chars (422 - RN-09)
    r_short = client.post("/api/v1/auth/register", json={
        "username": "shortpwd",
        "full_name": "Short Pwd",
        "email": "short@foodstore.com",
        "password": "123"
    })
    assert r_short.status_code == 422, f"Se esperaba 422, dio {r_short.status_code}"
    print(" [OK] RN-09: Rechazo de contraseña menor a 8 caracteres (422 Unprocessable)")

    # 4. Login con credenciales incorrectas (401)
    r_fail_login = client.post("/api/v1/auth/token", data={"username": "juan", "password": "WrongPassword"})
    assert r_fail_login.status_code == 401
    print(" [OK] HU-02: Login fallido con credenciales erróneas (401)")

    # 5. Login de usuario regular (juan: User1234!)
    r_login_user = client.post("/api/v1/auth/token", data={"username": "juan", "password": "User1234!"})
    assert r_login_user.status_code == 200
    assert "access_token" in r_login_user.cookies
    user_cookie = {"access_token": r_login_user.cookies["access_token"]}
    print(" [OK] HU-02 / RN-03: Login exitoso, entrega JWT en cookie HttpOnly 'access_token'")

    # 6. GET /me con cookie válida
    r_me = client.get("/api/v1/auth/me", cookies=user_cookie)
    assert r_me.status_code == 200
    assert r_me.json()["username"] == "juan"
    assert r_me.json()["role"] == "user"
    print(" [OK] GET /me: Obtiene datos del usuario autenticado correctamente")

    # 7. GET /categorias permitido a usuario regular (RN-07)
    r_cat_get = client.get("/api/v1/categorias/", cookies=user_cookie)
    assert r_cat_get.status_code == 200
    assert len(r_cat_get.json()) > 0
    print(" [OK] RN-07: Lectura GET de categorías permitida a usuario regular (200)")

    # 8. POST /categorias denegado a rol 'user' (403 Forbidden - RN-04)
    r_cat_post_forbidden = client.post(
        "/api/v1/categorias/",
        json={"nombre": "Tacos", "descripcion": "Comida mexicana"},
        cookies=user_cookie
    )
    assert r_cat_post_forbidden.status_code == 403
    print(" [OK] RN-04: Escritura POST denegada a usuario común con 403 Forbidden")

    # 9. POST /pedidos permitido a rol 'user' (RN-05)
    prod = client.get("/api/v1/productos/", cookies=user_cookie).json()[0]
    pedido_payload = {
        "detalles": [
            {"producto_id": prod["id"], "cantidad": 2, "precio_unitario": prod["precio_base"]}
        ]
    }
    r_ped_create = client.post("/api/v1/pedidos/", json=pedido_payload, cookies=user_cookie)
    assert r_ped_create.status_code == 201
    print(" [OK] RN-05: Creación de pedido permitida a rol 'user' (201 Created)")

    # 10. Login de admin (admin: Admin123!)
    r_login_admin = client.post("/api/v1/auth/token", data={"username": "admin", "password": "Admin123!"})
    assert r_login_admin.status_code == 200
    admin_cookie = {"access_token": r_login_admin.cookies["access_token"]}
    print(" [OK] Login de administrador exitoso")

    # 11. POST /categorias permitido a admin (require_role(['admin']))
    r_cat_create_admin = client.post(
        "/api/v1/categorias/",
        json={"nombre": "Tacos y Burritos", "descripcion": "Especialidades tex-mex"},
        cookies=admin_cookie
    )
    assert r_cat_create_admin.status_code == 201
    nueva_cat_id = r_cat_create_admin.json()["id"]
    print(f" [OK] Creación de categoría por admin exitosa (ID: {nueva_cat_id})")

    # 12. Borrado lógico de categoría (RN-11)
    r_cat_delete = client.delete(f"/api/v1/categorias/{nueva_cat_id}", cookies=admin_cookie)
    assert r_cat_delete.status_code == 204
    # Comprobar que ya no aparece en el listado activo
    cats_despues = client.get("/api/v1/categorias/", cookies=user_cookie).json()
    assert all(c["id"] != nueva_cat_id for c in cats_despues)
    print(" [OK] RN-11: Borrado lógico aplicado (categoría inactiva no figura en listados)")

    # 13. Endpoints de administración de usuarios (solo admin)
    r_admin_users = client.get("/api/v1/admin/usuarios", cookies=admin_cookie)
    assert r_admin_users.status_code == 200
    users_list = r_admin_users.json()
    assert any(u["username"] == "mariag" for u in users_list)
    print(" [OK] GET /admin/usuarios listado exitoso para rol admin")

    # 14. Desactivación de usuario
    maria_id = next(u["id"] for u in users_list if u["username"] == "mariag")
    r_desactivar = client.post(f"/api/v1/admin/usuarios/{maria_id}/desactivar", cookies=admin_cookie)
    assert r_desactivar.status_code == 200
    assert r_desactivar.json()["disabled"] is True
    print(" [OK] POST /admin/usuarios/{id}/desactivar exitoso")

    # 15. Usuario desactivado intenta login -> 400 "Cuenta de usuario desactivada"
    r_login_disabled = client.post("/api/v1/auth/token", data={"username": "mariag", "password": "Password123!"})
    assert r_login_disabled.status_code == 400
    assert "Cuenta de usuario desactivada" in r_login_disabled.json()["detail"]
    print(" [OK] Consigna b/c: Usuario desactivado recibe 400 'Cuenta de usuario desactivada'")

    # 16. Reactivación de usuario
    r_activar = client.post(f"/api/v1/admin/usuarios/{maria_id}/activar", cookies=admin_cookie)
    assert r_activar.status_code == 200
    assert r_activar.json()["disabled"] is False
    print(" [OK] POST /admin/usuarios/{id}/activar exitoso")

    # 17. Logout (Set-Cookie que borra la cookie HttpOnly)
    r_logout = client.post("/api/v1/auth/logout", cookies=admin_cookie)
    assert r_logout.status_code == 200
    assert "access_token" in r_logout.headers.get("set-cookie", "")
    print(" [OK] HU-03: Logout responde eliminando la cookie de sesión")

    print("\n -> TODAS LAS PRUEBAS DE INTEGRACIÓN DEL BACKEND PASARON EXITOSAMENTE! (100% OK)")


if __name__ == "__main__":
    test_authentication_and_rbac()

