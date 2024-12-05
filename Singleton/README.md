# Singleton
## Conceito
Garante que uma classe tenha apenas uma instância em todo o programa e fornece um ponto de acesso global para essa instância.

## Problema que Resolve
Evita a criação de múltiplas instâncias de uma classe, especialmente em cenários onde isso poderia causar conflitos (exemplo: conexão com banco de dados).

## Quando Usar
- Para gerenciar configurações globais de um sistema.
- Em loggers, drivers de impressão, ou conexões com banco de dados.

## Exemplo em Python
Veja o código de exemplo no arquivo `main.py`.

## Vantagens
- Controle centralizado da instância.
- Reduz uso desnecessário de memória.

## Desvantagens
- Pode dificultar testes devido à dependência de estado global.

##Exemplos de uso: Muitos desenvolvedores consideram o padrão Singleton um antipadrão. É por isso que seu uso está diminuindo no código Python.

##Identificação: O Singleton pode ser reconhecido por um método de criação estático, que retorna o mesmo objeto em cache.  
