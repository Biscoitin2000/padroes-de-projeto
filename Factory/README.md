    O padrão Factory é um padrão criacional que fornece uma interface para criar objetos em uma classe-mãe, permitindo que as subclasses alterem o tipo de objetos criados.

    Resolve problemas de acoplamento reduzindo-os, o cliente depende apenas da interface ou classe base. A Factory abstrai o processo de criação, tornando o cliente independente de implementações concretas.
    Resolve problema de encapsulamento, encapsula toda a lógica de criação dentro da Factory, deixando o cliente com um código mais simples e limpo.

    Vantagens:
         --> Facilita a reutilização de código, já que o cliente não precisa conhecer os detalhes das classes concretas.
         --> Permite adicionar novos produtos facilmente sem modificar o código existente.
    Desvantagens:
        --> Pode aumentar a complexidade inicial do código ao introduzir várias classes.
   
    Quando usar:
         Se criar objetos requer lógica complexa, como inicializações, validações ou configurações adicionais. 
         Se o tipo exato de objeto a ser criado só é conhecido em tempo de execução, com base em entradas do usuário, configuração ou estado.
