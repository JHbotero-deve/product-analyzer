# Publicar la landing page (para tener una URL real)

Amazon Associates exige una URL pública y funcionando. La forma más rápida y
gratis de conseguirla con este archivo (`index.html`) es una de estas dos:

## Opción A — Netlify Drop (más rápido, sin cuenta de GitHub)

1. Entrá a **https://app.netlify.com/drop**
2. Arrastrá la carpeta `landing/` completa (o el archivo `index.html`) a la página.
3. En segundos te da una URL tipo `https://nombre-random.netlify.app` — esa es
   la URL real y pública que ponés en el formulario de Amazon.
4. (Opcional) Desde el panel de Netlify podés cambiarle el nombre a algo como
   `radar-de-producto.netlify.app`.

## Opción B — GitHub Pages (si ya usás GitHub)

1. Creá un repositorio nuevo, por ejemplo `radar-de-producto`.
2. Subí el archivo `index.html` a la raíz del repo.
3. Andá a **Settings → Pages**, elegí la rama `main` y carpeta `/root`.
4. GitHub te da una URL tipo `https://tu-usuario.github.io/radar-de-producto/`.

Cualquiera de las dos URLs sirve para completar el campo "Ingresa tu(s)
Sitio(s) Web" del registro de Amazon Associates — tiene que ser exactamente
esa URL completa, con `https://` incluido.
