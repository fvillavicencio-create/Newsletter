# Plan de trabajo · Regcheq al Día (quincenal)

Plan operativo para producir y enviar el newsletter general cada 15 días. Complementa la guía editorial del [README](../README.md) y usa la plantilla [`templates/regcheq-al-dia.html`](../templates/regcheq-al-dia.html).

## 1. Cadencia

- **Envío:** un martes sí y uno no, a las **9:00** (hora del centro de México), a toda la base.
- **Ciclo:** 10 días hábiles. El ciclo de una edición empieza el miércoles siguiente al envío de la anterior, así que nunca hay dos ediciones en producción al mismo tiempo.
- **Regla de oro:** el texto se congela el **miércoles previo al envío** (D-4). Lo que no esté validado para entonces pasa a la siguiente edición.

## 2. Ciclo de una edición (semana a semana)

`D-0` = martes de envío. Los días cuentan en días hábiles.

| Día | Cuándo | Tarea | Responsable | Entregable |
|---|---|---|---|---|
| D-9 | Mié · semana 1 | **Reunión de planeación** (30 min): temas de 01–05, tema central de 02, CTA de cierre, asunto tentativo | Marketing (lidera) + Cumplimiento + Producto | Brief de la edición |
| D-8 | Jue · semana 1 | Pedir los insumos: novedad de producto (Producto), caso de uso validado (Comercial), dudas frecuentes de clientes (CX), webinar o evento (Marketing) | Marketing | Solicitudes enviadas con fecha límite D-6 |
| D-7 | Vie · semana 1 | Revisar las métricas de la edición anterior (D+3) y empezar a redactar 01–03 | Marketing | Notas de métricas · borrador en curso |
| D-6 | Lun · semana 2 | Borrador completo de 01–04 · insumos de 05 recibidos | Marketing | Borrador 01–04 |
| D-5 | Mar · semana 2 | **Validación regulatoria** de 01 y 02: fuentes, etiquetas, fechas clave (plazo: 24 h) · redacción de 05–06 | Cumplimiento · Marketing | Comentarios de Cumplimiento · borrador 05–06 |
| D-4 | Mié · semana 2 | Correcciones · validación de 05 por Producto y del caso de uso por el cliente · **texto congelado** al cierre del día | Marketing + Producto + Comercial | Texto final |
| D-3 | Jue · semana 2 | Montaje en HubSpot: asunto (2 variantes A/B), preheader, enlaces con UTM, lista general | Marketing | Correo armado |
| D-2 | Vie · semana 2 | Pruebas en Gmail, Outlook y móvil · envío de prueba a revisores · **go / no-go** | Marketing (revisores: Cumplimiento y CX) | Aprobación final |
| D-1 | Lun · semana 3 | Programar el envío · día de colchón para imprevistos | Marketing | Envío programado |
| **D-0** | **Mar · semana 3, 9:00** | **Envío** · monitorear rebotes y respuestas | Marketing | Edición enviada |
| D+3 | Vie | Métricas: apertura, clics, demos, bajas (alimentan la planeación del D-9 siguiente) | Marketing | Reporte breve |

## 3. Roles

| Rol | Qué hace en cada ciclo | Tiempo estimado |
|---|---|---|
| **Marketing** (dueño del newsletter) | Lidera la planeación, redacta, monta, prueba, envía y mide | ~10 h por edición |
| **Cumplimiento** | Aporta noticias y fechas clave; valida 01 y 02 en un plazo de 24 h | ~2 h |
| **Producto** | Aporta y valida la novedad de la sección 05 | ~1 h |
| **CX** | Comparte las dudas frecuentes de clientes (insumo para 02) y revisa el envío de prueba | ~1 h |
| **Comercial** | Consigue el caso de uso y su validación con el cliente | ~1 h |

Hay que definir una persona responsable por área y un suplente de Marketing que cubra vacaciones.

## 4. Banco de contenidos (para no empezar de cero)

Para que el ciclo de 10 días sea viable, algunos contenidos se preparan **con una o dos ediciones de anticipación**:

| Contenido | Anticipación | Por qué |
|---|---|---|
| Artículos del blog (2 por edición) | Publicados a más tardar en D-3 | El correo enlaza a artículos que ya tienen que existir |
| Webinar (sección 04) | Registro abierto ≥ 2 semanas antes del evento | Se anuncia en la edición anterior al evento |
| Caso de uso | Validado 1 edición antes | La aprobación del cliente suele tardar |
| Tema central de 02 | Definido 2 ediciones antes (ver calendario) | Da tiempo a preparar el checklist y el descargable |

**Plan B:** si un insumo no llega a tiempo, se usa un contenido del banco. Si no hay caso de uso, la sección 05 sale solo con producto y marca. Las seis secciones no se eliminan; lo que puede reducirse es su extensión.

## 5. Convivencia con los comunicados a clientes

- No enviar un comunicado el mismo día que el newsletter ni el día anterior, salvo urgencia (incidencia o cambio regulatorio con plazo).
- Si un cambio de producto ya se comunicó a los clientes, en la sección 05 se menciona en una línea, contado por su beneficio.
- Producto avisa a Marketing con al menos 5 días hábiles de anticipación de los lanzamientos previstos.

## 6. Antes de la primera edición (una sola vez)

- [ ] Subir la plantilla a HubSpot como plantilla de correo reutilizable.
- [ ] Subir el logo al gestor de archivos de HubSpot y cambiar el `src` de la plantilla (hoy apunta a una rama de GitHub que puede desaparecer).
- [ ] Crear la lista general con la propiedad *tipo de contacto* (cliente / prospecto / aliado) para medir por audiencia.
- [ ] Confirmar las URLs fijas: agendar demo, contacto CX, baja y preferencias.
- [ ] Definir el formato de UTM (`utm_source=newsletter&utm_campaign=rad-NN`).
- [ ] Nombrar a los responsables por área y agendar las reuniones de planeación recurrentes (miércoles de por medio, 30 min).

## 7. Calendario de las primeras ediciones

Los temas siguen la línea editorial "Ruta al 1 de marzo". Los criterios para elegir el contenido, el banco de contenidos y el brief de edición están en [cómo se define el contenido](definicion-de-contenido.md).

| Edición | Planeación (D-9) | Texto congelado (D-4) | Envío (D-0) | Tema central (02) | Cierre |
|---|---|---|---|---|---|
| N.º 01 | Mié 21 oct | Mié 28 oct | **Mar 3 nov** | Lo que cambia el 30 de noviembre *(por confirmar)* | Demo |
| N.º 02 | Mié 4 nov | Mié 11 nov | **Mar 17 nov** | Beneficiario controlador con el umbral del 25 % | Webinar |
| N.º 03 | Mié 18 nov | Mié 25 nov | **Mar 1 dic** | Avisos e informes en ceros | Blog / recurso |
| N.º 04 | Mié 2 dic | Mié 9 dic | **Mar 15 dic** | Cierre de año: checklist y plan de capacitación anual | Demo |
| — | — | — | *29 dic: pausa por fiestas* | — | — |
| N.º 05 | Mié 30 dic\* | Mié 6 ene | **Mar 12 ene** | Enfoque basado en riesgos | Webinar |

Notas:
- **Lun 16 nov** es feriado (Revolución Mexicana) y es el D-1 de N.º 02: el envío se programa el viernes 13.
- Los avisos de cada mes vencen el **día 17**. La edición de inicio de mes es la que recuerda ese vencimiento en *Fechas clave*.
- \*La planeación de N.º 05 puede adelantarse al 16 de diciembre para no depender de la semana de fiestas.

## 8. Seguimiento y mejora

- **Cada edición (D+3):** reporte breve con apertura, CTR, demos agendadas, clics a CX y bajas, segmentado por tipo de contacto.
- **Cada 2 meses (4 ediciones):** retrospectiva de 45 min para ver qué secciones generan más clics, si conviene ajustar la hora o el día de envío y qué temas pide la audiencia.
- **Meta inicial de referencia:** apertura ≥ 30 %, CTR ≥ 3 %, bajas ≤ 0,5 % por envío. Se ajusta con los datos de las tres primeras ediciones.
