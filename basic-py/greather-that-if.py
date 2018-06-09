A = int(input("Ingrese primer numero: "))
B = int(input("Ingrese segundo numero: "))
C = int(input("Ingrese tercer numero: "))
D = int(input("Ingrese cuarto numero: "))
E = int(input("Ingrese quinto numero: "))

if (A > B and A > C and A > D and A > E):
    if (B > C and B > D and B > E):
        if (C > D and C > E):
            if (D > E):
                print(str(A)+ " " + str(B)+ " " + str(C)+ " " + str(D)+ " " + str(E))
            else:
                print(str(A)+ " " + str(B)+ " " + str(C)+ " " + str(E)+ " " + str(D))
        else:
            if (D > C):
                if (C > E):
                    print(str(A)+ " " + str(B)+ " " + str(D)+ " " + str(C)+ " " + str(E))
                else:
                    print(str(A)+ " " + str(B)+ " " + str(D)+ " " + str(E)+ " " + str(C))
            else :
                if (D > C):
                    print(str(A)+ " " + str(B)+ " " + str(E)+ " " + str(D)+ " " + str(C))
                else:
                    print(str(A)+ " " + str(B)+ " " + str(E)+ " " + str(C)+ " " + str(D))
    elif (C > B and C > D and C > E):
        if (B > D and B > E):
            if (D > E):
                print(str(A)+ " " + str(C)+ " " + str(B)+ " " + str(D)+ " " + str(E))
            else:
                print(str(A)+ " " + str(C)+ " " + str(B)+ " " + str(E)+ " " + str(D))
        else:
            if (D > B):
                if (B > E):
                    print(str(A)+ " " + str(C)+ " " + str(D)+ " " + str(B)+ " " + str(E))
                else:
                    print(str(A)+ " " + str(C)+ " " + str(D)+ " " + str(E)+ " " + str(B))
            else :
                if (D > B):
                    print(str(A)+ " " + str(C)+ " " + str(E)+ " " + str(D)+ " " + str(B))
                else:
                    print(str(A)+ " " + str(C)+ " " + str(E)+ " " + str(B)+ " " + str(D))
        
        

