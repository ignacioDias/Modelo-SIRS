# Análisis del Modelo SIRS con Pérdida de Inmunidad

Este estudio analiza la evolución de una enfermedad infecciosa utilizando el modelo SIRS (Susceptible-Infectado-Recuperado-Susceptible), considerando que los individuos recuperados pierden su inmunidad después de un tiempo y pueden volver a infectarse.

## Ecuaciones del modelo

El sistema de ecuaciones diferenciales utilizado es:

\[
\begin{cases}
\dot{S}(t) = -\beta S(t) I(t) + \delta R(t) \\
\dot{I}(t) = \beta S(t) I(t) - \nu I(t) \\
\dot{R}(t) = \nu I(t) - \delta R(t)
\end{cases}
\]

Donde:
- \( S(t) \): número de susceptibles en el tiempo \( t \)
- \( I(t) \): número de infectados
- \( R(t) \): número de recuperados
- \( \beta = 0.0022 \): tasa de contagio
- \( \nu = 0.4477 \): tasa de recuperación
- \( \delta = 0.1 \): tasa de pérdida de inmunidad
- Población total constante: \( N = 764 \)
- Condiciones iniciales: \( S(0) = 763 \), \( I(0) = 1 \), \( R(0) = 0 \)

## Simulación

La simulación se realizó usando el método de Euler con paso \( h = 0.1 \) durante un período de 50 días. Se graficaron las funciones \( S(t), I(t), R(t) \) para observar el comportamiento del sistema.

## Observaciones

### ¿Convergencia o ciclos?

En la simulación con los parámetros dados, se observa que:
- Las funciones \( S(t) \), \( I(t) \) y \( R(t) \) **se aplanan gradualmente**.
- Los valores se estabilizan con el tiempo, sin mostrar oscilaciones marcadas ni reinfecciones recurrentes.

Por lo tanto, el sistema **converge hacia un equilibrio estable**, donde las tasas de infección, recuperación y pérdida de inmunidad se compensan mutuamente. Esto último se puede obsermar mejor si aumentamos el valor de N a un número muy grande.

### Impacto del parámetro \( \delta \)

Se exploró el efecto de distintos valores de \( \delta \) sobre el sistema:

| δ       | Comportamiento observado                                 |
|---------|----------------------------------------------------------|
| 0.01    | La inmunidad dura más tiempo, el sistema converge más rápido a un equilibrio con muy pocos infectados. |
| 0.1     | Se observa equilibrio estable con una pequeña población infectada constante. |
| 0.5     | La inmunidad dura poco, los recuperados regresan rápidamente a susceptibles. Esto mantiene una proporción significativa de la población infectada en forma constante. |

En resumen:
- **δ bajo** → facilita la **erradicación** o control de la enfermedad.
- **δ alto** → promueve la **persistencia de la enfermedad** debido a reinfecciones más frecuentes.

## Conclusión

El modelo SIRS simulado indica que, bajo ciertas condiciones, una enfermedad puede alcanzar un equilibrio estable sin presentar reinfecciones periódicas significativas. El parámetro \( \delta \), que modela la pérdida de inmunidad, es clave para determinar si la enfermedad desaparece o persiste en la población.

