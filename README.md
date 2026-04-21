# cbr-sport-recommendation

Sistema de recomendação de esportes baseado em **Raciocínio Baseado em Casos (RBC)**, desenvolvido como projeto prático para a disciplina de **Inteligência Artificial**.

---

## Equipe

- Kirsten Luz Concepcion
- Pedro Henrique Schneider

---

## Descrição

O sistema recebe o perfil de um novo usuário e recomenda os três esportes mais adequados com base em casos anteriores armazenados em uma biblioteca. A similaridade entre casos é calculada por meio de **similaridade ponderada**, onde cada atributo possui um peso e uma função de similaridade local definida por conhecimento de domínio.

O sistema também aprende ao longo do uso: após cada recomendação, o caso resolvido é adicionado à biblioteca, expandindo a base de conhecimento automaticamente.

---

## Conceitos de RBC aplicados

| Etapa RBC | Como foi implementado |
|---|---|
| **Representação** | Casos descritos por 7 atributos categóricos |
| **Recuperação** | Similaridade ponderada com funções locais por atributo |
| **Reutilização** | Os 3 casos mais similares são apresentados como sugestão |
| **Revisão** | O usuário escolhe o esporte final |
| **Retenção** | O novo caso resolvido é salvo em `library.csv` |

---

## Estrutura do projeto

```
cbr-sport-recommendation/
│
├── requirements.txt  # Bibliotecas e versões usadas no projeto
├── viariables.txt    # Atributos, pesos e valores possíveis
├── tests.txt         # Caso previamente calculado para teste do programa
├── main.py           # Fluxo principal do sistema
├── similarity.py     # Dicionário de similaridades locais por atributo
├── library.csv       # Base de casos (biblioteca)
└── cases.csv         # Casos novos a serem resolvidos
```

---

## Atributos dos casos

| Atributo | Valores possíveis |
|---|---|
| Idade | Crianca, Adolescente, Adulto, Idoso |
| Problema_Fisico | Nenhum, Mental, Respiratorio, Mobilidade |
| Preferencia | Individual, Coletivo |
| Local | Aberto, Fechado, Indiferente |
| Disponibilidade | 1x, 2x, 3x, 4x, 5x (por semana) |
| Objetivo | Saude, Competicao, Lazer |
| Orcamento | Baixo, Medio, Alto |

---

## Pesos dos atributos

Os pesos somam **1.0** no total. Parte deles é fixa e parte é definida pelo usuário ao iniciar o sistema:

| Atributo | Peso |
|---|---|
| Idade | 0.20 (fixo) |
| Problema_Fisico | 0.20 (fixo) |
| Disponibilidade | 0.10 (fixo) |
| Orcamento | 0.10 (fixo) |
| Preferencia | definido pelo usuário |
| Local | definido pelo usuário |
| Objetivo | definido pelo usuário |

> O usuário distribui **0.30** entre Preferencia, Local e Objetivo ao iniciar a execução.

---

## Como executar

**Pré-requisitos:**
```bash
requirements.txt
```

**Execução:**
- Adicionar caso em `cases.csv`
```bash
python main.py
```

O sistema irá:
1. Solicitar a distribuição de pesos para os atributos variáveis
2. Para cada caso em `cases.csv`, calcular a similaridade com todos os casos da biblioteca
3. Recomendar os 3 esportes mais similares (sem repetição de esporte)
4. Solicitar que o usuário informe o esporte escolhido
5. Salvar o novo caso resolvido em `library.csv`

---

> Aamodt, A., & Plaza, E. (1994). Case-Based Reasoning: Foundational Issues, Methodological Variations, and System Approaches. *AI Communications*, 7(1), 39–59.
