##Conceito do Padrão##

O padrão de projeto Adapter é utilizado para conectar interfaces incompatíveis de modo que possam trabalhar juntas. Ele atua como um intermediário (“adaptador”) que converte a interface de uma classe existente (Adaptee) em outra interface esperada pelo cliente (Target), sem a necessidade de modificar nenhuma das classes diretamente.


##Problema que Ele Resolve##

Imagine que você tem uma classe existente que fornece funcionalidades úteis, mas sua interface não é compatível com o que seu cliente ou sistema espera. Alterar a classe original pode ser inviável, especialmente se:

Ela pertence a uma biblioteca de terceiros.

Existe código legado que não pode ser modificado.

O Adapter resolve isso fornecendo uma camada intermediária que converte chamadas de métodos da interface esperada em chamadas para os métodos reais da classe existente.

##Quando Usar o Padrão##

Quando você precisa integrar classes que têm interfaces incompatíveis.

Quando não é possível modificar diretamente a interface ou implementação da classe existente.

Quando deseja reutilizar uma classe existente em um novo sistema com uma interface diferente.

##Vantagens##

Reutiliza código existente: Permite usar classes legadas ou de terceiros sem modificação.

Desacoplamento: O cliente e a classe existente permanecem desacoplados.

Flexibilidade: Você pode criar vários adaptadores para diferentes contextos.

Facilita integração: Torna sistemas heterogêneos compatíveis.

##Desvantagens##

Complexidade adicional: Adiciona uma camada extra de abstração, o que pode dificultar a manutenção.

Desempenho: Pequena perda de desempenho devido ao uso do adaptador como intermediário.

Uso excessivo: Pode levar a um design confuso se usado de forma exagerada ou desnecessária.
