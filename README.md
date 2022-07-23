# Boas Vindas ao repositório da dinâmica de lógica 👋

Durante este momento será realizada uma dinâmica envolvendo problemas lógicos, que devem ser solucionados em grupos durante o tempo de 30 minutos. O time de pessoas da Trybe avaliará as pessoas participantes durante a dinâmica e também depois, quando cada um dos grupos apresentarem seus avanços. Os seguintes critérios serão utilizados para avaliação:

- Trabalho em equipe;
- Comunicação;
- Solução final dos problemas;
- Solução dos problemas em mais de uma linguagem;
- Qualidade de código;
- Preparação e organização para apresentação;

---

# Programação do momento ⌚

1. Teremos um breve alinhamento ao iniciarmos o momento que não substitui a leitura deste readme;
2. Serão dividos os grupos de trabalho. Cada grupo terá 3 ou 4 integrantes na equipe;
3. Dentro de cada uma das breakouts, as equipes devem solucionar a maior quantidade de desafios que conseguirem dentro do tempo de 30 minutos;
4. Mais informações sobre os problemas lógicos serão colocados neste repositório no dia da dinâmica;
5. Todas as pessoas retornarão à sala principal e serão movidas para outras breakouts com o intuito de fazer a apresentação do seu desenvolvimento;
6. Cada grupo terá aproximadamente 5 minutos para mostrar o código desenvolvido e os testes sendo executados, a pessoa avaliadora poderá fazer perguntas exploratórias sobre o desenvolvimento de cada grupo.
7. Todos os grupos receberão um feedback relacionado à sua performance (acima da expectativa, dentro da expectativa ou abaixo da expectativa) para cada um dos critérios de avaliação;

---

# Resolução dos desafios 📝

Todos os desafios podem ser feitos resolvidos ou em javascript ou em python e será considerado um diferencial ter a solução em ambas as linguagens.


<details>
<summary><strong>Javascript</strong></summary>

</details>

<br>

<details>
<summary><strong>Python</strong></summary>


## Preparação do ambiente

1. **Criar o ambiente virtual**

```bash
$ python3 -m venv .venv
```

2. **Ativar o ambiente virtual**

```bash
$ source .venv/bin/activate
```

3. **Instalar as dependências no ambiente virtual**

```bash
$ python3 -m pip install -r requirements.txt
```

## Rodando os testes

Para executar todos os testes

```bash
$ python3 -m pytest
```

Para executar os testes relacionados a apenas um dos problemas (_para o problema 1, por exemplo_)

```bash
$ python3 -m pytest tests/test_problem1.py
```
</details>

---

# Entrega dos desafios 👾

Após clonar o repositório, desenvolva as soluções em uma _branch_ com o número do seu grupo. O número do seu grupo é dado pelo número da breakout room em que vocês estão. Exemplos:

- Grupo 1: _branch_ `grupo-1`
- Grupo 2: _branch_ `grupo-2`
- Grupo 3: _branch_ `grupo-3`
- Grupo 4: _branch_ `grupo-4`
- ...

Ao final, faça o _push_ com as alterações

---

# Desafios 🧠

<br>

<details>
<br>
<summary><strong>Problema 1 - Professor chateado</strong></summary>

Um professor universitário está chateado com o atraso das pessoas estudantes de sua aula. Decidiu então adotar a estratégia de não passar dever de casa, condicionado a que o número de pessoas atrasadas seja menor que um valor limite (k), estipulado por ele mesmo para cada diferente tema na aula. Para registrar a frequência das pessoas estudantes, registra em um array (a) a quantidade de minutos que as pessoas chegam antes(-) ou depois(+) dele.  

Implemente um algoritmo que recebe como parâmetros um array, com o tempo de chegada de cada pessoa estudante em relação ao início da aula, e um número inteiro limite estabelecido pelo professor. O algoritmo deve retornar "SIM" caso ele tenha passado dever de casa e "NÃO" caso contrário.

### Exemplo de entrada:
```bash
a = [-2, -1, 0, 1, 2]
k = 3
```

### Exemplos de saídas:
```bash
"NÃO"
```

### Explicação
Os valores -2 e -1 se referem a pessoas estudantes que chegaram 2 minutos e 1 minuto, respectivamente, antes do horário da aula. O valor 0 se refere à uma pessoa que chegou exatamente no horário da aula, portanto, nenhum dos 3 valores representam pessoas que chegaram atrasadas. os valores 1 e 2 se referem a pessoas estudantes que chegaram 1 minuto e 2 minutos depois do horário da aula, assim, pessoas atrasadas.

Como o valor limite espitulado foi 3 e só duas pessoas se atrasaram, o professor não passou dever de casa.

</details>

<br>
<br>

<details>
<br>
<summary><strong>Problema 2 - Pares de meias</strong></summary>

As meias de uma enorme pilha de meias devem ser organizadas em pares de acordo com sua cor. Dado um array com números inteiros que representam meias e suas respectivas cores. 

Implemente um algoritmo que recebe como parâmetro o array de números que representam as cores e retorna a quantidade de pares com mesma cor existem dentro do array.

### Exemplo de entrada:
```bash
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
```

### Exemplos de saídas:
```bash
3
```

### Explicação
É possível formar 3 pares distintos, dois pares de meias relacionadas à cor de número 10 e um par de meias relacionadas à cor de número 20. Todos os demais números do arrays não formam pares.

![alt text](pares-de-meias.png "Formação dos pares de meia - 2 pares de meias 10 e 1 par de meias 20")

</details>

<br>
<br>

<details>
<br>
<summary><strong>Problema 3 - Dia da pessoa desenvolvedora</strong></summary>

O dia da pessoa desenvolvedora é sempre o 256º dia do ano, contudo, sabemos que alguns anos são bissextos, isto é, há o dia 29 de fevereiro.

O ano é considerado bissexto se uma das seguintes condições é seguida:

- O inteiro que representa o ano é divisível por 400;
- O inteiro que representa o ano é divisível por 4 mas não por 100;

Considerando as informações dadas, implemente um algoritmos que recebe como parâmetro um inteiro representando o ano e retorna a data referente ao dia da pessoa programadora no seguinte formato: DD.MM.AAAA, onde D representa o dia, M representa o mês e A representa o ano.

### Exemplo de entrada:
```bash
year = 2016
```

### Exemplos de saídas:
```bash
12.09.2016
```

### Explicação
2016 é divisível por 4, portanto, é um ano bissexto. Sendo assim, o 256º dia desse ano será 12 de setembro de 2016.

</details>
