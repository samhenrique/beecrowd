N1, N2, N3, N4 = input().split(" ", 3)
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

print("Media: {:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")

if media < 5.0:
    print("Aluno reprovado.")

if media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: {:.1f}".format(exame))
    mediafinal = (exame+media)/2

    if mediafinal < 4.9:
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(mediafinal))

    else:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(mediafinal))
