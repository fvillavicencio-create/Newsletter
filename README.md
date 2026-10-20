# Regcheq al Día

*Nombre provisional · Newsletter quincenal de Regcheq*

Un espacio para mantenerse al tanto de la actualidad regulatoria, aprender sobre las obligaciones de la Ley Antilavado y descubrir herramientas e ideas para gestionar mejor la operación.

| | |
|---|---|
| **Frecuencia** | Cada 15 días, con calendario editorial definido |
| **Audiencias** | Clientes, prospectos y aliados |
| **Contenido** | Educación, noticias, blogs y recursos prácticos |
| **Objetivo** | Fidelización, posicionamiento y generación de demos |

## Plantillas

| Archivo | Audiencia | Enfoque |
|---|---|---|
| [`templates/regcheq-al-dia-clientes.html`](templates/regcheq-al-dia-clientes.html) | Versión A · Clientes | Fidelización |
| [`templates/regcheq-al-dia-prospectos.html`](templates/regcheq-al-dia-prospectos.html) | Versión B · Prospectos y aliados | Atracción |

Ambas son HTML de email (tablas, estilos en línea, 600 px, responsivas y compatibles con Outlook), listas para pegar en HubSpot u otra herramienta de envío. Todo texto entre `[corchetes]` es un marcador que se reemplaza en cada edición.

## Iconografía

Dos sets de 24 iconos cada uno —**Regulación y producto** y **Emociones y cercanía**— en estilo dibujado a mano, cercano y amigable, con la paleta Regcheq (trazo `#0A2342` + manchas `#368FFF`, `#BCD9FF`, `#F4C542`, `#7FD8AA`). Vista previa en [`assets/icons/index.html`](assets/icons/index.html) / [`assets/icons/preview.png`](assets/icons/preview.png).

- `assets/icons/svg/` — vectoriales (web, diseño).
- `assets/icons/png/` — 256 × 256 con fondo transparente, para el email (Gmail y Outlook no muestran SVG). Usar a 48–64 px.
- Para editar o agregar iconos: modificar `assets/icons/build_icons.py` y ejecutar `CHROMIUM_PATH=/ruta/a/chromium python3 assets/icons/build_icons.py` (los PNG requieren Playwright).

Sugerencia por sección: saludo `hola` · 01 `alertas` / `regulacion` · 02 `en-la-practica` · 03 `blog` · 04 `webinar` · 05 `novedades` / `lanzamiento` · 06 `hablemos` · Fechas clave `fechas-clave` · 💡 `tip`.

El set de emociones (`cercania`, `gracias`, `celebracion`, `apoyo`, `te-cuidamos`, `felicidad`, etc.) sirve para saludos, agradecimientos, aniversarios, logros de clientes y mensajes de marca.

## Estructura fija de cada edición

La estructura se repite en todas las ediciones para que sea reconocible; lo que cambia es el contenido.

| # | Sección | Contenido | Versión A · Clientes | Versión B · Prospectos y aliados |
|---|---|---|---|---|
| 01 | **Lo que tienes que saber** | Actualidad regulatoria | Noticias + bloque **Fechas clave** (avisos y vencimientos) | Noticias oficiales, propuestas y buenas prácticas |
| 02 | **En la práctica** | Educación y recomendaciones | Checklist + "💡 En tu plataforma" (cómo hacerlo en Regcheq) | Checklist + recurso descargable |
| 03 | **Lo nuevo en nuestro blog** | Contenido editorial | 2 artículos | 2 artículos |
| 04 | **Próximamente en Regcheq** | Webinars, eventos y formación | Webinar especializado para clientes | Webinar gratuito |
| 05 | **Novedades Regcheq** | Producto y marca | Funcionalidades, mejoras, recursos | Caso de uso (validado) + noticia de marca |
| 06 | **Hablemos** | Cierre y llamada a la acción | Contactar a CX / soporte | Agendar una demo |

Las secciones 01–04 forman la **base editorial compartida**: se redactan una sola vez y se usan en ambas versiones. Solo se adaptan los módulos finales (05 y 06) y algunos bloques puntuales.

### Etiquetas de la sección 01

Cada noticia regulatoria lleva una etiqueta para distinguir su naturaleza:

- 🔵 **OFICIAL** — disposición publicada y vigente (citar fuente oficial).
- 🟡 **PROPUESTA** — anteproyecto o consulta pública; aún no es obligatoria.
- 🟢 **BUENA PRÁCTICA** — recomendación no obligatoria del sector o la autoridad.

## Flujo de producción por edición

| Día | Tarea | Responsable |
|---|---|---|
| D-10 | Definir temas de la edición (01–05) y CTA de cierre | Marketing + Cumplimiento |
| D-7 | Redacción de la base compartida (01–04) | Marketing |
| D-5 | Validación regulatoria de 01 y 02 | Cumplimiento |
| D-4 | Módulos por audiencia (05–06) con Producto, CX y Comercial | Marketing |
| D-2 | Montaje en herramienta de envío, pruebas en Gmail / Outlook / móvil | Marketing |
| D-0 | Envío de ambas versiones (sugerido: martes o miércoles, 9:00–10:00) | Marketing |
| D+3 | Revisión de métricas | Marketing |

## Calendario editorial sugerido (primeras ediciones)

| Edición | Fecha | Tema central (02 · En la práctica) | Cierre sugerido |
|---|---|---|---|
| N.º 01 | 2.ª quincena oct | Beneficiario controlador | A: CX · B: Demo |
| N.º 02 | 1.ª quincena nov | Integración de expedientes de identificación | Webinar |
| N.º 03 | 2.ª quincena nov | Avisos e informes en ceros | Blog / recurso |
| N.º 04 | 1.ª quincena dic | Cierre de año: checklist de cumplimiento | A: CX · B: Demo |

*No todas las ediciones necesitan vender directamente:* alternar el cierre entre demo, webinar y contenido.

## Métricas

- **Fidelización (A):** tasa de apertura, clics a guías de plataforma, contactos a CX, asistencia a webinars de clientes.
- **Atracción (B):** tasa de apertura, clics a blog y descargables, registros a webinars, **demos agendadas**.
- **Ambas:** bajas por edición y crecimiento de la base de suscriptores.

## Criterios editoriales

- Lenguaje claro y aplicado; evitar tecnicismos sin explicar.
- Toda información regulatoria se valida con Cumplimiento y cita su fuente.
- Casos de uso solo con información y cifras validadas por el cliente.
- El contenido es informativo y no sustituye asesoría legal (incluido en el footer).
