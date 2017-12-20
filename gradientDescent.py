"""
Implementação de um Gradiente Descentente
Calcula o mínimo de uma função diferenciável f(x)

"""

import random

def f(x):
    """
    Vamos supor uma função quadratica x²+5=0.
    Observa-se que existe um mínimo em x = 5, quando se faz lim x->0 y=5
    """
    return x**2 + 5

def df(x):
    """
    Derivada de f(x) em x
    df(x)/dx.
    """
    return 2*x

def gradient_descent_update(x, gradx, learning_rate):
    x = x - learning_rate*gradx
    return x

# Random number between 0 and 10,000. Feel free to set x whatever you like.
x = random.randint(0, 10000)
'''
Importante notar a influencia da taxa de aprendizado para que o 
gradiente convirja corretamente, taxas muito altas fazem o gradiente divergir
'''
learning_rate = 0.0049
epochs = 1000

for i in range(epochs+1):
    cost = f(x)
    gradx = df(x)
    print("EPOCH {}: Cost = {:.3f}, x = {:.3f}".format(i, cost, gradx))
    '''Calculando o gradiente calcula-se a variação em x para que seja localizado o minimo da função
    '''
    x = gradient_descent_update(x, gradx, learning_rate)
    
