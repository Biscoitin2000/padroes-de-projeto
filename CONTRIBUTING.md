 --- PULL REQUEST ---
 
# ESTRUTURA DO REPOSITÓRIO-
 
├── padroes-de-projeto/

│____├── README.md—------------------ -----------# Introdução geral e visão do projeto

│____├── CONTRIBUTING.md—------------------------# Diretrizes para contribuição

│_├── Factory/—------------------------------ # Pasta para o padrão Factory

│____│____├── UML_Factory—-----------------------# Diagrama UML do padrão

│____│____├── factory_example.py—----------------# Exemplo prático do padrão em Python

│_├── Singleton/------------------------------# Pasta para o padrão Singleton

│____│____├── UML_Singleton----------------------# Diagrama UML do padrão

│____│____├── singleton_example.py---------------# Exemplo prático do padrão em Python

│_├── Adapter/--------------------------------# Pasta para o padrão Adapter

│____│____├── UML_Adapter.png--------------------# Diagrama UML do padrão

│____│____├── adapter_example.py-----------------# Exemplo prático do padrão em Python

│_├── Visitor/--------------------------------# Pasta para o padrão Visitor

│____│____├── UML_Visitor------------------------# Diagrama UML do padrão

│____│____├── visitor_example.py-----------------# Exemplo prático do padrão em Python

│_├── Facade/---------------------------------# Pasta para o padrão Facade

│____│____├── UML_Facade-------------------------# Diagrama UML do padrão

│____│____├── facade_example.py------------------# Exemplo prático do padrão em Python

│_└── docs/-----------------------------------# Pasta opcional para documentação geral


# FORMAS DE DESCRIÇÃO DO PADRÃO-

- (nome do padrão);
EX: Facade

- Conceito
EX: O Facade atua como uma fachada (ou "frente") para um subsistema complexo, expondo uma 
interface simplificada para o cliente enquantomantém a complexidade oculta.

- Problema que Resolve;
EX: Facilita a interação com sistemas complexos ao oferecer uma interface única e clara, evitando que
os clientes lidem diretamente com várias interfaces e classes.


- Quando Usar;
EX:- Para simplificar o uso de um subsistema complexo.
   - Quando deseja criar uma abstração de nível mais alto para um conjunto de funcionalidades relacionadas.
   - Quando deseja reduzir o acoplamento entre clientes e classes internas de um subsistema.

- Vantagens;
EX: - Simplifica o uso de subsistemas complexos.
    - Reduz o acoplamento entre o cliente e os componentes internos do subsistema.
    - Permite alterar os subsistemas sem impactar o cliente.

 - Desvantagens
EX: - Pode se tornar um ponto de risco único (single point of failure) se concentrar muita lógica.
    - Pode esconder detalhes importantes de funcionamento do subsistema.   


# REQUISITOS PARA A IMPLEMENTAÇÃO DO PADÃO NO REPOSITÓRIO- 
Recriar em liguagem de programação py(pyton) um similar de seu padrão para sua ultilização em nosso repositório, fazer testes e verificar sua coerencia com o padrão desenvolvido pelo mesmo.

# DETALHES DO OQUE INCLUIR NA DOCUMENTAÇÃO-

Repetindo os passos amostrados anteriormente na pasta com seu projeto padrão deve conter a DESCRIÇÃO DE SEU PADRÃO cojunto com seu UML DO PADRÃO (EM DIAGRAMA), e por fim anexado na pasta ter um TESTE DE SEU PADRÃO EM PY (PYTON) conforme amostrado a baixo
EX:

├── padroes-de-projeto/

│_├── Facade/---------------------------------# Pasta para o padrão Facade

│____│____├── UML_Facade-------------------------# Diagrama UML do padrão

│____│____├── facade_example.py------------------# Exemplo prático do padrão em Python

 
