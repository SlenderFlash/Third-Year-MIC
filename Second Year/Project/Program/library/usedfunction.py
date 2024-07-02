import random


def questions():
    x = random.randint(0, 1)
    y = random.randint(0, 1)
    return (x, y)


def response(question, method):
    if method == 0:
        return 0
    elif method == 1:
        return 1
    elif method == 2:
        return question
    else:
        return 1 - question


def verifier_alea():
    gagner = 0
    for i in range(10000):
        question = questions()
        x = question[0]
        y = question[1]
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        if (a + b)%2 == x*y:
            gagner += 1
    print(f"Le valeur expecté pour stratégies aléatoire est: {gagner/100}%")


want = []
for i in range(4):
    want = [*want,[]]
    for j in range(4):
        gagner = 0
        for x in (0, 1):
            for y in (0, 1):
                a = response(x, i)
                b = response(y, j)
                if (a + b)%2 == x*y:
                    gagner += 1
        want[i] = [*want[i], gagner*25]


def verifier_det():
    real = []
    for i in range(4):
        real = [*real,[]]
        for j in range(4):
            gagner = 0
            for m in range(10000):
                question = questions()
                x = question[0]
                y = question[1]
                a = response(x, i)
                b = response(y, j)
                if (a + b)%2 == x*y:
                    gagner += 1
            real[i] = [*real[i], gagner/100]
    for i in range(4):
        for j in range(4):
            print(f"{real[i][j]}% / {want[i][j]}   ", end = "")
        print()


def verifier_class():
    gagner = 0
    ratioa = []
    for t in range(4):
        ratioa.append(random.randint(1,100))
    ratiob = []
    for t in range(4):
        ratiob.append(random.randint(1,100))
    for m in range(10000):
        question = questions()
        x = question[0]
        y = question[1]
        i = random.choices([0,1,2,3], weights = ratioa, k = 1)
        j = random.choices([0,1,2,3], weights = ratiob, k = 1)
        a = response(x, i[0])
        b = response(y, j[0])
        if (a + b) % 2 == x * y:
            gagner += 1
    estime = 0
    for i in range(4):
        for j in range(4):
            estime += (want[i][j]*ratioa[i]*ratiob[j])/(sum(ratioa)*sum(ratiob))
    print(f"Le possibilité estimé pour le distribution de stratégies de Alice {ratioa} et Bob {ratiob} est {int(estime*100)/100}%")
    print(f"La possibilité dans l'expériment: {gagner/100}")