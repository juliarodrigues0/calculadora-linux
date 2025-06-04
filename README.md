# Calculadora em Python com Shell Script

Este projeto automatiza a execução de uma calculadora escrita em Python utilizando um script `.sh` no Linux (WSL).

---

## 📁 Arquivos incluídos

- `calculadora.py` — script da calculadora
- `calculadora.sh` — script shell que executa a calculadora
- `comandos.txt` — comandos utilizados no terminal durante a atividade

---

## 🚀 Como executar o script `.sh`

1. No terminal, entre na pasta onde está o arquivo
2. Dê permissão de execução:

```bash
chmod +x calculadora.sh
./calculadora.sh
---

## 🧠 O que o código Python faz

O arquivo `calculadora.py` é uma calculadora simples de linha de comando, que executa as seguintes etapas:

1. Exibe um menu com 4 operações:
   - 1 → Adição
   - 2 → Subtração
   - 3 → Multiplicação
   - 4 → Divisão
2. Solicita ao usuário dois números reais (float)
3. Verifica qual operação foi escolhida e executa:
   - Soma, subtração, multiplicação ou divisão
   - Em caso de divisão por zero, exibe uma mensagem de erro
4. Mostra o resultado no terminal
5. Se o usuário digitar uma opção inválida, exibe uma mensagem apropriada

### 🧾 Exemplo de uso:
Escolha uma operação:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
Digite a operação: 1
Digite o primeiro número: 5
Digite o segundo número: 7
Resultado: 12.0
