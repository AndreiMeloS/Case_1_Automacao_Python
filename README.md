# Case_1_Automacao_Python
 Case 1 — Automação de Tarefa com Python

## 📌 Visão geral

Este projeto foi desenvolvido como parte do meu aprendizado em **Python aplicado à automação de processos**.

O objetivo foi automatizar o cadastro de **300 produtos/clientes em uma plataforma**, utilizando uma base de dados estruturada e reproduzindo automaticamente as ações que normalmente seriam realizadas de forma manual pelo usuário.

A solução utiliza **Python, Pandas e PyAutoGUI** para ler os dados da base e executar as etapas de cadastro no sistema.

> **Ideia central:** transformar uma tarefa operacional, repetitiva e baseada em regras em um processo automatizado.

---

## 🎯 Objetivo do projeto

Imagine uma situação em que um profissional precisa cadastrar manualmente 300 registros em um sistema.

O processo seria aproximadamente:

1. Abrir o sistema;
2. Fazer login;
3. Localizar o formulário de cadastro;
4. Digitar o código;
5. Digitar a marca/nome;
6. Digitar o tipo;
7. Digitar a categoria;
8. Digitar o preço;
9. Digitar o custo;
10. Inserir observações;
11. Salvar o cadastro;
12. Repetir o processo para o próximo registro.

Fazer isso 300 vezes representa uma atividade **repetitiva, operacional e sujeita a erros de digitação**.

A proposta do projeto foi utilizar Python para executar esse fluxo automaticamente.

---

# 🧠 Antes de automatizar: entender o processo

Uma das principais lições do projeto foi que **a automação não começa pelo código**.

Antes de pensar em Python ou em qualquer biblioteca, o primeiro passo é entender como a tarefa seria executada manualmente.

### Fluxo manual

```text
Abrir navegador
      ↓
Acessar sistema
      ↓
Fazer login
      ↓
Abrir formulário
      ↓
Pegar dados da base
      ↓
Preencher campos
      ↓
Salvar cadastro
      ↓
Voltar ao formulário
      ↓
Pegar próximo registro
      ↓
Repetir até o último cadastro
```

Somente depois de entender esse processo foi possível identificar **quais etapas poderiam ser executadas pelo computador** e quais ferramentas seriam necessárias.

---

# 🔎 Do processo manual para a automação

A lógica utilizada foi:

| Processo manual | Automação em Python |
|---|---|
| Abrir navegador | `pyautogui.press()` |
| Digitar endereço | `pyautogui.write()` |
| Clicar em campos | `pyautogui.click()` |
| Pressionar Tab | `pyautogui.press("tab")` |
| Fazer login | PyAutoGUI |
| Ler base de dados | Pandas |
| Selecionar registro | `tabela.loc[]` |
| Repetir cadastro | `for` |
| Verificar campo vazio | `if` |
| Salvar cadastro | PyAutoGUI |
| Passar para próximo registro | `for` |

Essa etapa de **mapear o processo antes de programar** foi um dos principais aprendizados do projeto.

---

# 🛠️ Tecnologias e bibliotecas utilizadas

### Python

Linguagem utilizada para construir a lógica da automação.

### PyAutoGUI

Biblioteca utilizada para controlar o computador por meio de:

- Mouse;
- Teclado;
- Cliques;
- Digitação;
- Atalhos;
- Navegação entre campos.

### Pandas

Biblioteca utilizada para trabalhar com a base de dados.

Neste projeto, o Pandas foi responsável por:

- Ler o arquivo CSV;
- Armazenar os dados em uma tabela;
- Localizar informações de cada registro;
- Disponibilizar os dados para o processo de automação.

### Time

Biblioteca utilizada para criar pausas durante a execução.

Isso é importante porque páginas e sistemas precisam de tempo para carregar.

---

# 📦 Principais conceitos de Python aprendidos

## 1. Importação de bibliotecas

```python
import pyautogui
import time
import pandas as pd
```

O comando `import` permite utilizar recursos desenvolvidos em outras bibliotecas.

---

## 2. Variáveis

Exemplo:

```python
link = "https://exemplo.com"
```

A variável funciona como uma "caixa" onde armazenamos uma informação que poderá ser utilizada posteriormente.

Outro exemplo:

```python
codigo = tabela.loc[linha, "codigo"]
```

Aqui, o código do registro atual é armazenado na variável `codigo`.

---

## 3. Funções

Durante o projeto foram utilizadas funções como:

```python
pyautogui.click()
pyautogui.write()
pyautogui.press()
time.sleep()
pd.read_csv()
```

Uma função pode ser entendida, de forma simplificada, como uma **ação que o programa sabe executar**.

Por exemplo:

```python
pyautogui.write("Produto")
```

significa:

> Execute a função `write` e escreva "Produto".

---

## 4. Estruturas de repetição — `for`

Um dos conceitos mais importantes do projeto foi o `for`.

```python
for linha in tabela.index:
```

Essa instrução significa:

> Para cada linha existente na tabela, execute as instruções abaixo.

Assim, não precisamos escrever 300 vezes o código responsável pelo cadastro.

O mesmo conjunto de instruções é reutilizado para todos os registros.

```text
Registro 1 → cadastrar
Registro 2 → cadastrar
Registro 3 → cadastrar
      ...
Registro 300 → cadastrar
```

---

## 5. Estrutura condicional — `if`

Também foi utilizado o `if` para tratar situações em que um campo poderia estar vazio.

```python
if not pd.isna(obs):
    pyautogui.write(str(obs))
```

Em linguagem simples:

> Se existir uma observação, escreva a observação.

Isso evita que o programa tente preencher um campo com uma informação inexistente.

---

## 6. Acesso aos dados com Pandas

Para buscar uma informação específica da tabela:

```python
tabela.loc[linha, "codigo"]
```

A lógica é:

```text
tabela
  ↓
linha atual
  ↓
coluna "codigo"
  ↓
valor do código
```

O mesmo princípio é utilizado para acessar:

- Código;
- Marca;
- Tipo;
- Categoria;
- Preço;
- Custo;
- Observação.

---

# 🔄 Funcionamento da automação

O funcionamento pode ser representado da seguinte forma:

```text
              BASE DE DADOS
                   │
                   ▼
             arquivo CSV
                   │
                   ▼
                Pandas
                   │
                   ▼
        Seleciona um registro
                   │
                   ▼
              PyAutoGUI
                   │
          ┌────────┴────────┐
          ▼                 ▼
      Preenche          Navega pelos
       campos             campos
          │                 │
          └────────┬────────┘
                   ▼
             Salva cadastro
                   │
                   ▼
           Próximo registro
                   │
                   ▼
              Repetição
                   │
                   ▼
             Último registro
```

---

# ⏱️ Impacto potencial da automação

O exercício teve como objetivo automatizar **300 cadastros**.

O tempo manual depende da quantidade de campos, velocidade do operador, sistema utilizado e necessidade de correções. Como esse tempo não foi cronometrado no exercício, o valor abaixo é uma **estimativa ilustrativa**, e não uma métrica medida.

### Exemplo de cenário

Considerando aproximadamente **1,5 a 2 minutos por cadastro manual**:

| Cenário | Tempo aproximado |
|---|---:|
| 1 cadastro | 1,5–2 min |
| 10 cadastros | 15–20 min |
| 100 cadastros | 2,5–3,3 h |
| 300 cadastros | **7,5–10 h** |

Além do tempo de execução, uma atividade repetitiva desse tipo pode gerar:

- Cansaço operacional;
- Erros de digitação;
- Esquecimento de campos;
- Retrabalho;
- Perda de produtividade.

A automação busca justamente reduzir a necessidade de execução manual dessas etapas repetitivas.

> **Importante:** os tempos acima são apenas uma referência para dimensionar o problema. Um próximo passo seria cronometrar o processo manual e a execução automatizada para medir o ganho real.

---

# 💡 Principal aprendizado: automatizar começa pelo processo

Antes deste projeto, poderia parecer que automação significa simplesmente:

> "Aprender Python e escrever código."

Na prática, o processo é diferente.

Aprendi que uma automação começa com uma pergunta:

> **"Como essa tarefa é realizada hoje?"**

Depois disso:

### 1. Mapear o processo

Descrever todas as etapas realizadas manualmente.

### 2. Identificar tarefas repetitivas

Verificar quais etapas seguem regras claras e podem ser executadas pelo computador.

### 3. Identificar os dados necessários

Entender de onde vêm as informações utilizadas no processo.

### 4. Escolher as ferramentas

A partir do problema, escolher as bibliotecas adequadas.

Neste caso:

```text
Dados → Pandas
Automação da interface → PyAutoGUI
Pausas → Time
Lógica → Python
```

### 5. Criar a automação

Transformar o processo manual em instruções que o computador consiga executar.

### 6. Testar

Executar inicialmente com poucos registros e verificar se o comportamento está correto.

### 7. Escalar

Depois de validar o processo, executar para toda a base.

---

# 📚 O que este projeto consolidou

Este projeto me permitiu praticar conceitos fundamentais de Python:

- `import`;
- Bibliotecas;
- Variáveis;
- Funções;
- Strings;
- Conversão de tipos com `str()`;
- Estruturas de repetição (`for`);
- Estruturas condicionais (`if`);
- Acesso a dados com Pandas;
- Leitura de arquivos CSV;
- Automação de mouse e teclado;
- Pausas e sincronização;
- Navegação por campos utilizando `Tab`;
- Tratamento básico de dados vazios.

Mais importante que memorizar cada comando foi entender **como transformar uma atividade operacional em um fluxo que pode ser executado por um programa**.

---

# 🎯 Conclusão

O principal aprendizado deste projeto foi entender que **programação e automação podem ser utilizadas para resolver problemas de processos**, e não apenas para desenvolver sistemas.

O fluxo aprendido foi:

```text
PROBLEMA
   ↓
MAPEAR PROCESSO MANUAL
   ↓
IDENTIFICAR REPETIÇÕES
   ↓
IDENTIFICAR DADOS
   ↓
ESCOLHER FERRAMENTAS
   ↓
DESENVOLVER AUTOMAÇÃO
   ↓
TESTAR
   ↓
MEDIR RESULTADO
   ↓
APRIMORAR
```

Este projeto representa meu primeiro contato prático com **Python aplicado à automação de processos**, conectando programação, manipulação de dados e melhoria de atividades operacionais.
