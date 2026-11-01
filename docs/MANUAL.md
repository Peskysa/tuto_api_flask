# Manual · API Flask de ejemplo

Ejecuta `python index.py` con el entorno instalado. Abre http://127.0.0.1:5000/.

- GET / conserva el saludo HTML original.
- GET /health devuelve estado y versión.
- POST /api/sumar recibe exactamente dos campos numéricos a y b y devuelve resultado. Ejemplo: {"a": 2, "b": 3} → {"resultado": 5}.
- Datos no válidos: HTTP 400. Tipo de contenido distinto de JSON: 415. Petición de más de 4 KB: 413.

El ejemplo no tiene persistencia, cuentas, CORS ni autenticación de producción. La página de GitHub Pages explica el contrato; el servidor Python se ejecuta localmente, no dentro de Pages.
