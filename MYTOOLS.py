PI_INT = 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
E_INT = 7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274

def pi_real(n : int):
    if n <= 1 or n >= 100:
        return "Insira um número natural maior que 0 e menor que 100."
    pi_rep = '3,' + str(PI_INT)[0:n]
    return pi_rep

def e_real(n : int):
    if n <= 1 or n >= 100:
        return "Insira um número natural maior que 0 e menor que 100."
    e_rep = '2,' + str(E_INT)[0:n]
    return e_rep

print(e_real(4))
    