import matplotlib.pyplot as plt

# Parámetros del modelo
BETA = 0.0022
nu = 0.4477
DELTA = 0.1
h = 0.1  # paso de integración
DAYS = 50

# Condiciones iniciales
S = [763]
I = [1]
R = [0]
TOTAL_POPULATION = 764 #N

time = [0]

def euler_method():
    for _ in range(int(DAYS / h)):
        s, i, r = S[-1], I[-1], R[-1]
        
        dS = -BETA * s * i + DELTA * r
        dI = BETA * s * i - nu * i
        dR = nu * i - DELTA * r

        S.append(s + h * dS)
        I.append(i + h * dI)
        R.append(r + h * dR)
        time.append(time[-1] + h)

def graph_results():
    plt.plot(time, S, label="Susceptibles (S)")
    plt.plot(time, I, label="Infectados (I)")
    plt.plot(time, R, label="Recuperados (R)")
    plt.xlabel("Días")
    plt.ylabel("Población")
    plt.title("Modelo SIRS (Euler h=0.1)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

euler_method()
graph_results()