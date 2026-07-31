def ler_dados(N, T):
    alunos = []
    times = []

    for _ in range(T):
        times.append([])

    for _ in range(N):
        nome_aluno, H = input().split()
        H = int(H)
        nome_aluno = nome_aluno.lower()
        alunos.append((nome_aluno, H))

    return alunos, times


def distribuir_times(alunos, times):
    alunos_ordenados = sorted(alunos, key=lambda aluno: aluno[1], reverse=True)
    for indice, aluno in enumerate(alunos_ordenados):
        indice_time = indice % len(times) # O operador módulo (%) faz com que os times sejam escolhidos ciclicamente

        times[indice_time].append(aluno) # Adiciona o aluno ao time correspondente
    
    return times


def ordenar_times(times):
    for time in times:
        time.sort(key=lambda aluno: aluno[0])
    
    return times

def imprimir_times(times):
    for indice, time in enumerate(times):
        print(f"Time {indice + 1}")

        for aluno in time:
            print(aluno[0])

        print()


def main():

    N, T = map(int, input().split())
    
    alunos, times = ler_dados(N, T)

    times = distribuir_times(alunos, times)

    times = ordenar_times(times)

    imprimir_times(times)

if __name__=="__main__":
    main()