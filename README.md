# Navegación autónoma simulada en Webots (seguidor de línea + A*)

Trabajo de la materia **Taller de Robótica** (9.º semestre, Tec de Monterrey). Serie de prácticas y un proyecto final sobre un robot móvil simulado en [Webots](https://cyberbotics.com/), progresando de control manual y seguimiento de línea hasta planificación de ruta con el algoritmo A* sobre posición global.

## Contenido

- `controllers/`: controladores en Python de cada práctica.
  - `Keyboard/`: control manual por teclado (base de las primeras pruebas).
  - `Practica1_equipo/` (dentro de esa carpeta) y `Final_delivery_Practice1/`: entrega final de la Práctica 1 (versión más reciente por fecha de todas las que existían).
  - `_versiones_anteriores_practica1/`: las otras 4 variantes de la Práctica 1 que se probaron antes de la entrega final; se conservan como historial, no hace falta abrirlas.
  - `Line_Follower_v1/`: seguidor de línea.
  - `my_controller_Practice2/`, `p2_controller.py`, `p3_controller/`: prácticas 2 y 3.
  - `Practice global position/A_star_base_code.py` y `Controller_practice4.py`: implementación de planificación de ruta A* sobre posición global (Práctica 4).
- `worlds/`: mundos de Webots (`.wbt`) de cada práctica.
- `Proyecto Final/World_pipes.wbt`: mundo del proyecto final del curso.
- `Fondos/`: imágenes de pista usadas por el seguidor de línea.
- `referencias/`: PDFs de instrucciones y presentación del curso.
- `examenes_no_publicar_sin_revisar/`: scripts de exámenes parciales. Está en `.gitignore`, así que se queda en tu disco pero no se sube al repositorio con `git add`/`commit`. Si en algún momento confirmas que publicarlos no entra en conflicto con el código de honor del Tec, quita esa línea del `.gitignore`.

## Tecnologías

Python, Webots (simulador robótico), controladores estándar de Webots.

## Qué se quitó de la carpeta original y por qué

- El video de demostración `Arbol A estrella.mp4` (1.1 GB) no se copió: es demasiado grande para un repositorio de Git normal. Si quieres mostrarlo, súbelo a YouTube o Google Drive y enlázalo aquí, o usa Git LFS.
- Las carpetas `plugins/`, `protos/` y `libraries/` que Webots crea por defecto en todo proyecto nuevo estaban vacías; se quitaron por no aportar nada.
- El mundo de tutorial (`worlds/tutorial.wbt`) es un ejemplo estándar que trae Webots, no es trabajo propio.
- Se eliminó un archivo duplicado exacto (`worlds/p1_2`, idéntico a `worlds/p1.wbt`).
- La carpeta con el nombre de equipo informal se renombró a `Practica1_equipo`.

## Cómo abrir

Instala Webots, abre el archivo `.wbt` del mundo que te interese (por ejemplo `Proyecto Final/World_pipes.wbt`), y Webots debería cargar automáticamente el controlador de Python correspondiente desde `controllers/`.

## Estado

El proyecto final (`World_pipes.wbt`) y la práctica de A* están completos y son ejecutables en Webots. Es el candidato más fuerte de todo el portafolio para mostrar robótica autónoma.
