#Conceito do Padrão Factory:

O padrão de projeto Factory é um padrão criacional que permite criar objetos sem especificar a classe exata do objeto que será instanciado. Ele encapsula o processo de criação do objeto em uma classe chamada fábrica, tornando o código mais flexível e desacoplado, já que o cliente não precisa saber como os objetos são criados.

#Problema que o Padrão Resolve:

Em cenários onde um sistema precisa criar objetos de várias classes relacionadas, o padrão Factory resolve os problemas de:
Acoplamento: O código do cliente fica desacoplado da criação dos objetos.

Flexibilidade: Permite alterar a criação de objetos sem alterar a lógica do cliente.

Complexidade: Em casos onde a criação do objeto envolve processos complexos, a fábrica pode esconder essa complexidade.

Sem o padrão Factory, o cliente teria que instanciar diretamente as classes concretas, o que faria o código ser mais rígido e difícil de manter.

#Quando Usar o Padrão:

Você precisa criar objetos de tipos relacionados, mas não sabe de antemão qual tipo será necessário.

Você deseja centralizar e esconder a lógica de criação dos objetos.
   
Você precisa de flexibilidade para adicionar novas classes de produtos sem modificar o código cliente.

#Vantagens:

Desacoplamento: O código cliente não depende de classes concretas e está desacoplado da criação dos objetos.
Flexibilidade: Facilidade para adicionar novos tipos de produtos (novas classes) sem modificar o código cliente.
Centralização: A lógica de criação dos objetos fica centralizada na fábrica, o que facilita a manutenção.
Extensibilidade: Novos tipos de produtos podem ser facilmente introduzidos sem modificar a lógica do cliente ou outras partes do código.

Desvantagens:

Complexidade Adicional: Introduz mais classes ao sistema, o que pode aumentar a complexidade, especialmente se a criação dos objetos for simples.
Dependência de Fábricas: O código cliente fica dependente da fábrica para criar os objetos, o que pode ser indesejável em sistemas muito simples.
Maior número de classes: Em sistemas pequenos, o padrão pode gerar uma quantidade excessiva de classes, tornando o sistema mais difícil de entender.
