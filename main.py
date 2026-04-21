# Import
import pandas as pd
import similarity as sy

# main


def main():
    # pegando os csvs da biblioteca e de casos
    library, cases = pd.read_csv('library.csv'), pd.read_csv('cases.csv')
    # print("Biblioteca inicial: ")
    # print(f'\n{library}')
    # print("Casos: ")
    # print(f'\n{cases}')

    # selecionando as colunas da biblioteca para usar como base,
    # exceto as soluções
    base = library.iloc[:, range(library.shape[1] - 1)]

    # print('Base: ')
    # print(f'\n{base}')

    # base = pd.get_dummies(base)
    # print(f'\n{base}')
    # problems = pd.get_dummies(cases)
    # print(f'\n{problems}')

    print("Distribua 0.30 de peso entre Preferencia, Local e Objetivo (ex: 0.10, 0.10, 0.10)")

    while True:
        preference = float(
            input("Peso para Preferencia (Individual/Coletivo): "))
        local = float(input("Peso para Local (Aberto/Fechado/Indiferente): "))
        goal = float(
            input("Peso para Objetivo (Saude/Competicao/Lazer): "))

        if round(preference + local + goal, 2) == 0.30:
            break
        else:
            print(
                f"A soma foi {round(preference + local + goal, 2)}, precisa ser 0.30. Tente novamente.")

    weights = {
        'Idade':           0.20,
        'Problema_Fisico': 0.20,
        'Preferencia':     preference,
        'Local':           local,
        'Disponibilidade': 0.10,
        'Objetivo':        goal,
        'Orcamento':       0.10
    }
    # print(weights)

    # testando dicionário
    # print(sy.similarity['Orcamento'])

    results = {}
    for i in range(cases.shape[0]):
        case_row = cases.loc[i, :]
        similarities = []  # guarda similaridade com cada caso da base
        for j in range(base.shape[0]):
            base_row = base.loc[j, :]

            calc = 0
            # Para cada atributo, pega os valores dos dois casos e busca a similaridade
            for atributo in weights.keys():
                valor_novo = case_row[atributo]   # ex: 'Adulto'
                valor_base = base_row[atributo]   # ex: 'Idoso'

                sim_value = sy.similarity_dict[atributo][(
                    valor_novo, valor_base)]  # ex: 0.5
                calc += round(sim_value * weights[atributo], 2)

            similarities.append(round(calc, 2))

        # print(similarities)

        # Ordena por similaridade (maior primeiro), preservando os índices originais
        indexed_similarities = sorted(
            enumerate(similarities), key=lambda x: x[1], reverse=True)

        # Pega os 3 melhores índices, garantindo esportes únicos
        chosen = []
        for idx, score in indexed_similarities:
            sport = library.iloc[idx]['Esporte']
            if sport not in [library.iloc[c[0]]['Esporte'] for c in chosen]:
                chosen.append((idx, score))
            if len(chosen) == 3:
                break

        first_option_index = chosen[0][0]
        second_option_index = chosen[1][0]
        third_option_index = chosen[2][0]

        # print(first_option_index,  chosen[0][1])
        # print(second_option_index, chosen[1][1])
        # print(third_option_index,  chosen[2][1])

        results[f'case_{i}'] = {
            'similaridades': similarities,
            # pega o esporte da linha mais similar
            'primeiro': library.iloc[first_option_index]['Esporte'],
            'segundo': library.iloc[second_option_index]['Esporte'],
            'terceiro': library.iloc[third_option_index]['Esporte']
        }

        print(f'Case {i+1}: similaridades = {similarities}\n')
        print(
            f'  → Melhor caso: {first_option_index+1}, Esporte: {results[f"case_{i}"]["primeiro"]}\n')
        print(
            f'  → Segundo melhor caso: {second_option_index+1}, Esporte: {results[f"case_{i}"]["segundo"]}\n')
        print(
            f'  → Terceiro melhor caso: {third_option_index+1}, Esporte: {results[f"case_{i}"]["terceiro"]}\n')

        sport_chosen = input("Qual esporte você escolheu? ")
        # print(sport_chosen)

        # Adiciona o novo caso na library
        new_case = case_row.copy()  # copia as features do caso atual
        new_case['Esporte'] = sport_chosen  # adiciona o esporte escolhido
        library = pd.concat(
            [library, pd.DataFrame([new_case])], ignore_index=True)

        # Salva no CSV
        library.to_csv('library.csv', index=False)

        print(f'\nCaso adicionado à library! Total de casos: {len(library)}\n')


# chamada
if __name__ == '__main__':
    main()
