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

| Día | Tarea | Responsable |
|---|---|---|
| D-10 | Definir temas de la edición (01–05) y CTA de cierre | Marketing + Cumplimiento |
| D-7 | Redacción de las secciones 01–04 | Marketing |
| D-5 | Validación regulatoria de 01 y 02 | Cumplimiento |
| D-4 | Secciones 05–06 con Producto, CX y Comercial | Marketing |
| D-2 | Montaje en herramienta de envío, pruebas en Gmail / Outlook / móvil | Marketing |
| D-0 | Envío a toda la base (sugerido: martes o miércoles, 9:00–10:00) | Marketing |
| D+3 | Revisión de métricas | Marketing |

## Calendario editorial sugerido (primeras ediciones)

| Edición | Fecha | Tema central (02 · En la práctica) | Cierre sugerido |
|---|---|---|---|
| N.º 01 | 2.ª quincena oct | Beneficiario controlador | Demo |
| N.º 02 | 1.ª quincena nov | Integración de expedientes de identificación | Webinar |
| N.º 03 | 2.ª quincena nov | Avisos e informes en ceros | Blog / recurso |
| N.º 04 | 1.ª quincena dic | Cierre de año: checklist de cumplimiento | Demo |

*No todas las ediciones necesitan vender directamente:* alternar el cierre entre demo, webinar y contenido.

## Métricas

- **Newsletter:** tasa de apertura y clics segmentados por audiencia (clientes / prospectos / aliados), clics a blog y descargables, registros a webinars, **demos agendadas**, clics a CX, bajas por edición y crecimiento de la base.
- **Comunicados:** tasa de apertura, clics a la guía, contactos a CX después del envío y, si requiere acción, % de clientes que la completaron a tiempo.

## Criterios editoriales

- Lenguaje claro y aplicado; evitar tecnicismos sin explicar.
- Toda información regulatoria se valida con Cumplimiento y cita su fuente.
- Casos de uso solo con información y cifras validadas por el cliente.
- El contenido es informativo y no sustituye asesoría legal (incluido en el footer).
