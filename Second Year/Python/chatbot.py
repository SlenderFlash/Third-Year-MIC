user_count = 0

def greeting(name):
    global user_count
    return "Bonjour " + name + ". Vous êtes l'utilisateur " + str(user_count)

def farewells():
    return "Au revoir !"

def chatbot():
    global user_count
    user_input = input("Vous : ")
    while "au revoir" not in user_input.lower() :
        if "bonjour" in user_input.lower() :
            user_count += 1
            name = input("Chatbot : Quel est votre nom ? ")
            print("Chatbot : " + greeting(name))
        else:
            print("Chatbot : Je ne comprends pas.")
        user_input = input("Vous : ")
    print("Chatbot " + farewells())
