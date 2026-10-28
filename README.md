# Regcheq al Día

*Nombre provisional · Newsletter quincenal de Regcheq*

Un espacio para mantenerse al tanto de la actualidad regulatoria, aprender sobre las obligaciones de la Ley Antilavado y descubrir herramientas e ideas para gestionar mejor la operación.

| | |
|---|---|
| **Frecuencia** | Cada 15 días, con calendario editorial definido |
| **Audiencias** | Una sola edición para toda la base: clientes, prospectos y aliados |
| **Contenido** | Educación, noticias, blogs y recursos prácticos |
| **Objetivo** | Fidelización, posicionamiento y generación de demos |

## Modelo de comunicación

| Pieza | Audiencia | Periodicidad | Para qué |
|---|---|---|---|
| **Newsletter general** — *Regcheq al Día* | Toda la base | Cada 15 días | Contenido editorial: actualidad regulatoria, educación, blog, eventos y novedades |
| **Comunicado a clientes** | Solo clientes | Solo cuando hay una actualización | Avisar de un cambio que afecta su servicio y, si aplica, qué tienen que hacer |

Ya no hay versiones del newsletter por audiencia. Lo que antes era exclusivo de clientes se reparte así:

- **Fechas clave** → pasa al newsletter general (sirve a toda la base).
- **"💡 En tu plataforma"**, guías de uso y cambios de producto → van en un **comunicado a clientes** cuando hay algo nuevo.
- **Contacto con CX** → enlace secundario en la sección 06 del newsletter y bloque fijo en cada comunicado.

## Plantillas

| Archivo | Pieza |
|---|---|
| [`templates/regcheq-al-dia.html`](templates/regcheq-al-dia.html) | Newsletter general (quincenal) |
| [`templates/comunicado-clientes.html`](templates/comunicado-clientes.html) | Comunicado a clientes (bajo demanda) |

Ambas son HTML de email (tablas, estilos en línea, 600 px, responsivas y compatibles con Outlook), listas para pegar en HubSpot u otra herramienta de envío. Todo texto entre `[corchetes]` es un marcador que se reemplaza en cada envío.

## Paleta de color

Orden de color de todas las piezas (opción "Azul Regcheq"):

| Elemento | Color |
|---|---|
| Cabecera | Imagen de fondo celeste (`assets/header-fondo.jpg`, 1200 × 424 px mostrada a 600 × 212) con respaldo `#bfe4fa`, logo a color (`assets/regcheq-logo-color.png`), textos en azul marino y franja amarilla `#f4c542` |
| Títulos y texto destacado | Azul marino `#0a2342` |
| Etiquetas de sección y enlaces | Azul Regcheq `#1478c8` |
| Cajas destacadas (Fechas clave, Qué tienes que hacer, bloques especiales) | Amarillo suave `#fdf4d8` con texto azul marino |
| Cajas de apoyo (índice, checklist, datos clave) | Gris azulado `#f3f7fb` |
| Cierre · 06 Hablemos | Azul marino `#0a2342` con botón amarillo `#f4c542` |
| Firma | Azul marino `#0a2342` |

## Elementos visuales (doodles)

Los doodles están en [`assets/doodles/`](assets/doodles/): 47 ilustraciones PNG de 256 × 256 px, con fondo transparente y en la paleta de la marca. Vienen de la carpeta "Doodles" del Drive de Marketing, en dos familias: *regulación y producto* y *emociones y cercanía*.

**Reglas de uso**

- Un doodle por sección como máximo, alineado a la derecha del título, a 64 px.
- Sobre fondos de color (cajas destacadas), el doodle va dentro de un círculo blanco de 44 px.
- Junto a un texto (descargables, "En tu plataforma") se usa a 22 px, en lugar del emoji.
- Siempre se muestran a la mitad o menos de su tamaño real, para que se vean nítidos en pantallas retina.

**Asignación fija**

| Bloque | Doodle |
|---|---|
| Saludo | `hola` |
| 01 · Lo que tienes que saber | `regulacion` |
| Fechas clave | `fechas-clave` |
| 02 · En la práctica | `en-la-practica` · descargable: `descargable` |
| 03 · Lo nuevo en nuestro blog | `blog` |
| 04 · Próximamente en Regcheq | `webinar` |
| 05 · Novedades Regcheq | `novedades` · lanzamientos: `lanzamiento` |
| 06 · Hablemos | `hablemos` |
| Comunicado: Qué cambia / Qué tienes que hacer / En tu plataforma / Dudas | `novedades` / `checklist` / `plataforma` / `apoyo` |

**Por tema (para ediciones especiales o temas centrales):** `beneficiario-controlador`, `identificacion`, `listas-restrictivas`, `monitoreo`, `alertas`, `revision-documental`, `proteccion-datos`, `cumplimiento`, `institucion`. Para eventos y agradecimientos: `celebracion`, `fiesta`, `gracias`, `comunidad`, `logro`.

## Newsletter general: estructura fija de cada edición

La estructura se repite en todas las ediciones para que sea reconocible; lo que cambia es el contenido.

| # | Sección | Contenido |
|---|---|---|
| 01 | **Lo que tienes que saber** | Actualidad regulatoria: noticias etiquetadas + bloque **Fechas clave** (avisos y vencimientos) |
| 02 | **En la práctica** | Educación y recomendaciones: checklist + recurso descargable |
| 03 | **Lo nuevo en nuestro blog** | 2 artículos |
| 04 | **Próximamente en Regcheq** | Webinar, evento o formación |
| 05 | **Novedades Regcheq** | Caso de uso (validado), novedad de producto contada por su beneficio y noticia de marca |
| 06 | **Hablemos** | CTA principal (demo, webinar o contenido) + enlace "¿Ya eres cliente? Habla con tu equipo de CX" |

### Etiquetas de la sección 01

Cada noticia regulatoria lleva una etiqueta para distinguir su naturaleza:

- 🔵 **OFICIAL** — disposición publicada y vigente (citar fuente oficial).
- 🟡 **PROPUESTA** — anteproyecto o consulta pública; aún no es obligatoria.
- 🟢 **BUENA PRÁCTICA** — recomendación no obligatoria del sector o la autoridad.

## Comunicado a clientes

Se envía **solo cuando hay una actualización** que afecta a los clientes. Un comunicado = un tema.

**Cuándo enviar uno**

- 🚀 **Actualización de producto** — nueva funcionalidad o cambio en cómo se usa la plataforma.
- ⚖️ **Cambio regulatorio** — una disposición vigente que exige que el cliente haga algo (validado con Cumplimiento).
- 🛠️ **Aviso de servicio** — mantenimiento programado, incidencia o cambio en condiciones del servicio.

Si la novedad no exige ni cambia nada para el cliente, no amerita comunicado: va en la sección 05 del siguiente newsletter.

**Estructura**

| Bloque | Contenido |
|---|---|
| Cabecera | Etiqueta del tipo de comunicado, fecha y título claro del cambio |
| Resumen | Qué cambia, por qué y en qué beneficia, en 2–3 líneas |
| Datos clave | Desde cuándo · A quién aplica · ¿Requiere acción? |
| Qué cambia | 1–3 puntos explicados por su efecto en el día a día |
| Qué tienes que hacer | Pasos concretos con fecha límite (se elimina si no requiere acción) |
| En tu plataforma | Dónde está el cambio en Regcheq + botón a la guía |
| ¿Tienes dudas? | Contacto con CX / soporte |

**Flujo:** Producto o Cumplimiento avisa del cambio → Marketing redacta con CX → validación de Producto (y de Cumplimiento si es regulatorio) → envío a la lista de clientes, idealmente antes de que el cambio entre en vigor.

## Flujo de producción del newsletter

Ciclo de 10 días hábiles con envío un martes sí y uno no, a las 9:00. El detalle por día, los roles, el banco de contenidos y el calendario están en el **[plan de trabajo](docs/plan-de-trabajo.md)**.

| Día | Tarea | Responsable |
|---|---|---|
| D-9 (mié) | Planeación: temas 01–05, tema central y CTA de cierre | Marketing + Cumplimiento + Producto |
| D-6 (lun) | Borrador 01–04 e insumos de 05 recibidos | Marketing |
| D-5 (mar) | Validación regulatoria de 01 y 02 | Cumplimiento |
| D-4 (mié) | Validación de 05 y **texto congelado** | Marketing + Producto + Comercial |
| D-3 / D-2 | Montaje en HubSpot, pruebas y go / no-go | Marketing |
| **D-0 (mar)** | **Envío a toda la base, 9:00** | Marketing |
| D+3 (vie) | Revisión de métricas | Marketing |

## Calendario de las primeras ediciones

| Edición | Envío | Tema central (02 · En la práctica) | Cierre sugerido |
|---|---|---|---|
| N.º 01 | Mar 3 nov | Beneficiario controlador | Demo |
| N.º 02 | Mar 17 nov | Integración de expedientes de identificación | Webinar |
| N.º 03 | Mar 1 dic | Avisos e informes en ceros | Blog / recurso |
| N.º 04 | Mar 15 dic | Cierre de año: checklist de cumplimiento | Demo |
| N.º 05 | Mar 12 ene | Por definir | Webinar |

*No todas las ediciones necesitan vender directamente:* alternar el cierre entre demo, webinar y contenido.

## Métricas

- **Newsletter:** tasa de apertura y clics segmentados por audiencia (clientes / prospectos / aliados), clics a blog y descargables, registros a webinars, **demos agendadas**, clics a CX, bajas por edición y crecimiento de la base.
- **Comunicados:** tasa de apertura, clics a la guía, contactos a CX después del envío y, si requiere acción, % de clientes que la completaron a tiempo.

## Criterios editoriales

- Lenguaje claro y aplicado; evitar tecnicismos sin explicar.
- Toda información regulatoria se valida con Cumplimiento y cita su fuente.
- Casos de uso solo con información y cifras validadas por el cliente.
- El contenido es informativo y no sustituye asesoría legal (incluido en el footer).
