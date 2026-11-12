# Plan de trabajo · Regcheq al Día (quincenal)

Sistema para planear, recabar, producir y enviar el newsletter cada dos semanas, con fechas fijas, un responsable por área y un solo lugar donde llega la información. Se complementa con [cómo se define el contenido](definicion-de-contenido.md), que explica cómo se elige qué se publica, y con la plantilla [`templates/regcheq-al-dia.html`](../templates/regcheq-al-dia.html).

## 1. El sistema en una línea

**Las áreas cargan sus insumos en un solo formulario → Marketing planea con un brief → se produce sobre la plantilla → Cumplimiento y Producto validan → se envía el martes → se mide el viernes.** Las fechas no cambian de un ciclo a otro, así que cada área sabe qué día le toca sin que nadie se lo pida.

## 2. Cadencia

- **Envío:** martes de por medio, a las **9:00** (hora del centro de México), a toda la base.
- **Ciclo:** 10 días hábiles, en 5 fases. El ciclo de una edición arranca el miércoles siguiente al envío de la anterior.
- **Regla de oro:** el texto se congela el **miércoles previo al envío** (D-4). Lo que no esté validado para entonces pasa a la siguiente edición.

`D-0` = martes de envío. Los días cuentan en días hábiles.

| Fase | Día | Qué pasa | Quién | Entregable |
|---|---|---|---|---|
| **1 · Planeación** | D-10 · mar (día de envío de la edición anterior) | Barrido automático de novedades regulatorias y propuesta de brief | Claude → Marketing | Noticias candidatas calificadas |
| | D-9 · mié | **Reunión de planeación** (30 min): se cierra el brief con temas de las 6 secciones y el cierre | Marketing (lidera) + Cumplimiento + Producto | Brief de edición |
| **2 · Recabación** | D-8 · jue | Se abre la ventana de insumos: llega a las áreas el recordatorio automático con el formulario y lo que se les pide | Marketing (automático) | Solicitudes enviadas |
| | D-7 · vie | Reporte de métricas de la edición anterior · recordatorio a quien no ha enviado | Marketing | Reporte D+3 |
| | D-6 · lun, 12:00 | **Cierre de insumos.** Lo que no llegó se cubre con el banco de contenidos (plan B) | Todas las áreas | Insumos completos |
| **3 · Producción** | D-6 · lun (tarde) | Borrador completo de las 6 secciones sobre la plantilla, con doodles y paleta | Marketing (con apoyo de Claude) | Borrador HTML |
| **4 · Validación** | D-5 · mar | **Bloque de validación** (30 min): Cumplimiento revisa 01 y 02 (fuentes, etiquetas, fechas) | Cumplimiento | Comentarios |
| | D-4 · mié | Producto valida 05 · Comercial confirma el caso de uso · correcciones · **texto congelado** al cierre del día | Marketing + Producto + Comercial | Texto final |
| **5 · Envío y medición** | D-3 · jue | Montaje en HubSpot: asunto A/B, preheader, UTM, lista general · PDF para revisión | Marketing | Correo armado |
| | D-2 · vie | Pruebas en Gmail, Outlook y móvil · envío de prueba · **go / no-go** (15 min) | Marketing + Cumplimiento + CX | Aprobación |
| | D-1 · lun | Programar envío · día de colchón | Marketing | Envío programado |
| | **D-0 · mar, 9:00** | **Envío** · monitoreo de rebotes y respuestas | Marketing | Edición enviada |
| | D+3 · vie | Métricas por sección y por tipo de contacto | Marketing | Reporte breve |

## 3. Mapa de secciones: qué se necesita y quién lo da

| Sección | Qué se necesita en cada edición | Área que lo entrega | Fecha límite | Quién valida |
|---|---|---|---|---|
| **01 · Lo que tienes que saber** | 2–3 noticias (disposiciones, modificaciones, propuestas o buenas prácticas) con fuente oficial y etiqueta · fechas clave del periodo | **Cumplimiento** (a partir del barrido automático del D-10) | D-8 | Cumplimiento |
| **02 · En la práctica** | Tema del calendario · checklist o guía · 3 dudas frecuentes de la quincena · descargable si aplica | **CX** (dudas reales de clientes) + **Cumplimiento** (contenido técnico) | D-7 | Cumplimiento |
| **03 · Lo nuevo en nuestro blog** | 2 artículos: uno que amplíe el tema central y uno de actualidad | **Marketing / contenidos** | Títulos en D-9 · publicados a más tardar en D-3 | Marketing |
| **04 · Próximamente en Regcheq** | Webinar, taller o evento con aliados: fecha, hora, ponentes, URL de registro | **Alianzas** + **Marketing** | D-8 | Alianzas |
| **05 · Novedades Regcheq** | Funcionalidad o mejora ya disponible · caso de uso validado · participación del equipo o noticia de marca | **Producto** (lanzamientos) · **Comercial** (casos de uso) · **Dirección / Alianzas** (marca y eventos) | D-6 | Producto y Comercial |
| **06 · Hablemos** | CTA según rotación (demo, webinar o contenido) · URL activa | **Marketing** · **Comercial** confirma capacidad de demos | D-9 (en la planeación) | Marketing |

## 4. Qué entrega cada área cada quincena

Cada área tiene **un responsable y un suplente**, y responde las mismas preguntas en el formulario de insumos. Si no hay nada que reportar, lo indica ("sin novedades"), para que nadie quede esperando.

| Área | Responsable · suplente | Qué responde en el formulario | Cuándo | Tiempo estimado |
|---|---|---|---|---|
| **Cumplimiento** | [Nombre] · [Nombre] | ¿Qué noticias del barrido van y con qué etiqueta? · ¿Falta alguna? · Fechas clave de las próximas 4 semanas · Puntos técnicos del tema de 02 | D-8 · valida en D-5 | ~2 h |
| **CX** | [Nombre] · [Nombre] | Las 3 dudas más repetidas de la quincena (con ejemplo real, sin datos del cliente) · ¿Algún tema que esté generando tickets? | D-7 | ~30 min |
| **Producto** | [Nombre] · [Nombre] | ¿Hay algo disponible para todos los clientes? Nombre, beneficio en una línea, guía o URL · Lanzamientos de las próximas 2 quincenas | D-6 · valida en D-4 | ~30 min |
| **Comercial** | [Nombre] · [Nombre] | Caso de uso candidato y estado de validación con el cliente · Preguntas frecuentes de prospectos · Capacidad de demos para la semana del envío | D-6 | ~30 min |
| **Alianzas** | [Nombre] · [Nombre] | Eventos, webinars o participaciones confirmadas (fecha, ponentes, registro) · Novedades de aliados | D-8 | ~20 min |
| **Marketing / contenidos** | [Nombre] · [Nombre] | Artículos publicados o por publicar · Descargables · Estado del webinar | D-9 | Incluido en las ~10 h de Marketing |

## 5. Herramientas: cómo se sistematiza

| Pieza | Para qué | Cómo funciona |
|---|---|---|
| **Formulario de insumos** (Google Forms) | Un solo punto de entrada para todas las áreas | Una sección por área con las preguntas de la tabla anterior. Cada respuesta se guarda en el banco de contenidos |
| **Banco de contenidos** (hoja en Drive) | Todas las ideas e insumos en un lugar, con su estado | Columnas definidas en [cómo se define el contenido](definicion-de-contenido.md#4-banco-de-contenidos). Cualquiera puede agregar ideas en cualquier momento |
| **Tablero por edición** (ClickUp o la herramienta de tareas del equipo) | Saber en qué va cada edición | Una plantilla de tarea "Edición N.º XX" con subtareas por día (D-10 a D+3), ya asignadas a cada área. Se duplica cada ciclo y se ajusta solo la fecha de envío |
| **Calendario compartido** | Que las fechas estén en la agenda de todos | Tres eventos recurrentes cada dos semanas: planeación (mié D-9, 30 min), validación de Cumplimiento (mar D-5, 30 min) y go / no-go (vie D-2, 15 min) |
| **Recordatorios automáticos** (correo o Slack) | Que nadie tenga que perseguir a las áreas | D-8: aviso con el enlace al formulario · D-7: recordatorio a quien no ha enviado · D-6, 12:00: cierre |
| **HubSpot** | Montaje, envío y métricas | Plantilla reutilizable, lista general segmentada por tipo de contacto, asunto A/B y UTM `rad-NN` |
| **Claude** | Reducir el trabajo manual | D-10: barrido regulatorio y propuesta de brief · D-6: borrador HTML a partir del brief y el banco · D-3: PDF y revisión de enlaces y marcadores · D+3: reporte de métricas desde HubSpot |

## 6. Reglas de juego

- **No se espera a nadie:** si un insumo no llega al cierre del D-6, la sección se cubre con el banco de contenidos. Las seis secciones siempre salen; lo que puede reducirse es su extensión.
- **Cumplimiento valida en 24 horas.** Una noticia sin validación no se publica.
- **Después del congelamiento (D-4)** solo entran cambios regulatorios críticos, con aprobación de Cumplimiento.
- **Producto avisa con 5 días hábiles de anticipación** los lanzamientos previstos. Si el cambio exige que el cliente haga algo, va además en un comunicado a clientes, nunca el mismo día que el newsletter ni el día anterior.
- **Casos de uso:** solo con información y cifras validadas por el cliente.

## 7. Checklists por fase

**Planeación (D-9)**
- [ ] Brief lleno: tema de 02, noticias candidatas con puntaje, artículos, evento, novedad de producto y cierre
- [ ] Asunto con dos variantes A/B y preheader
- [ ] Doodles elegidos
- [ ] Solicitudes a las áreas programadas para el D-8

**Producción (D-6)**
- [ ] Seis secciones completas, sin `[corchetes]` pendientes
- [ ] Cada noticia con su etiqueta (Oficial, Propuesta o Buena práctica) y su fuente
- [ ] Fechas clave verificadas

**Montaje y pruebas (D-3 a D-2)**
- [ ] Imágenes servidas desde HubSpot
- [ ] Todos los enlaces probados, con UTM
- [ ] Revisión en Gmail, Outlook y móvil
- [ ] Enlace de baja y pie legal

**Después del envío (D+3)**
- [ ] Reporte: entregados, clics por sección, demos, registros a webinar, clics a CX y bajas
- [ ] Aprendizajes anotados para la planeación siguiente

## 8. Calendario hasta el 1 de marzo

| Envío | Planeación (D-9) | Cierre de insumos (D-6) | Validación (D-5) | Texto congelado (D-4) | Tema central (02) | Cierre |
|---|---|---|---|---|---|---|
| **Mar 1 dic** | Mié 18 nov | Lun 23 nov | Mar 24 nov | Mié 25 nov | Ya están vigentes las nuevas Reglas: notificaciones diarias y avisos por sospecha en 24 horas | Demo |
| **Mar 15 dic** | Mié 2 dic | Lun 7 dic | Mar 8 dic | Mié 9 dic | Cierre de año: checklist de cumplimiento y plan de capacitación anual | Contenido |
| *29 dic* | — | — | — | — | *Pausa por fiestas* | — |
| **Mar 12 ene** | Mié 16 dic\* | Lun 4 ene | Mar 5 ene | Mié 6 ene | Beneficiario controlador con el umbral del 25 % | Webinar |
| **Mar 26 ene** | Mié 13 ene | Lun 18 ene | Mar 19 ene | Mié 20 ene | Enfoque basado en riesgos: cómo clasificar a tus clientes | Demo |
| **Mar 9 feb** | Mié 27 ene | Vie 29 ene\*\* | Mar 2 feb | Mié 3 feb | Manual de políticas internas y conocimiento del cliente | Contenido |
| **Mar 23 feb** | Mié 10 feb | Lun 15 feb | Mar 16 feb | Mié 17 feb | Checklist final antes del 1 de marzo | Demo |

Notas:
- \*La planeación del 12 de enero se adelanta al 16 de diciembre para no depender de la semana de fiestas.
- \*\*El lunes 1 de febrero es feriado (Día de la Constitución), así que el cierre de insumos pasa al viernes 29 de enero.
- Los avisos de cada mes vencen el **día 17**. La edición de inicio de mes los recuerda en *Fechas clave*.
- Si la edición del 17 de noviembre ya está en producción, sale con el proceso actual. El sistema completo arranca con la edición del **1 de diciembre**, cuya planeación es el **miércoles 18 de noviembre**.

## 9. Puesta en marcha (una sola vez, antes del 18 de noviembre)

- [ ] Nombrar responsable y suplente por área (tabla 4)
- [ ] Crear el formulario de insumos y el banco de contenidos
- [ ] Crear la plantilla de tarea por edición en el tablero del equipo
- [ ] Agendar los tres eventos recurrentes en el calendario compartido
- [ ] Configurar los recordatorios automáticos del D-8, D-7 y D-6
- [ ] En HubSpot: plantilla reutilizable, imágenes en el gestor de archivos, lista segmentada por tipo de contacto y URLs fijas (demo, CX, baja y preferencias)
- [ ] Programar el barrido regulatorio quincenal de Claude (D-10)

## 10. Seguimiento y mejora

- **Cada edición (D+3):** reporte breve por sección y por tipo de contacto. Las aperturas se usan solo como referencia, porque los sistemas de privacidad del correo las distorsionan; las métricas principales son clics, demos y registros.
- **Cada 2 meses:** retrospectiva de 45 minutos con todas las áreas para revisar qué secciones funcionan, si los insumos llegan a tiempo y qué temas pide la audiencia.
- **Meta inicial de referencia:** CTR ≥ 3 % y bajas ≤ 0,5 % por envío. Se ajusta con los datos de las tres primeras ediciones.
