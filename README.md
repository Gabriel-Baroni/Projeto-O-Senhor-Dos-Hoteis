<h1 align="center"> O SENHOR DOS HOTÉIS </h1>
<p align="center">Um trabalho para a disciplina de DESENVOLVIMENTO DE APLICAÇÕES COM BANCO DE DADOS - 3º Informática do IFSP-Jacareí</p>
<br>
<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>

<h1>👨‍🏫 Professores responsáveis</h1> 

-  Carlos Eduardo Duque Polito
-  Olavo Olimpo de Matos Junior 

<h1>🎯Objetivo do projeto</h1> 
O objetivo desse projeto é construir um site de reserva para uma hotelaria fictícia, que no caso é a hotelaria "O Senhor Dos Hotéis". Esta, possui a temática inspirada no vasto universo pertencente a franquia de "O Senhor dos Anéis". 
<br>
<h1>:hammer: Funcionalidades do projeto</h2>

- `Registro de clientes`: Um sistema de cadastro de clientes à um banco de dados.
- `Autenticação de conta`: Uma vez já cadastrado, o usuário poderá fazer login no site sem precisar refazer o cadastro. 
- `Reserva de um quarto de hotel `: Um sistema de busca por quartos disponíveis para serem reservados. Essa busca ocorrerá na base de dados da hotelaria.

<h1>✖️ O que não é o objetivo do projeto</h2>
Por se tartar de um protótipo e um trabalho em pequena escala, somente com fim de teste de conhecimentos, o site não contará com:

- `Escabilidade` Os desenvolvedores não estaram preocupados com a escabilidade do projeto 
- `Métodos de pagamento`: O site conterá com uma página para pagamento da reserva, porém por se tratar de uma hotelaria fictícia, não será possível realizar nenhuma espécie de pagamento.  

<h1>👥 Público-alvo</h2>
O tema do hotel e, consequentemente, do site será, como já mencionado, sobre "O Senhor dos Anéis". O público-alvo desse site será aventureiros que sempre quiseram se sentir neste universo rico em magia e mistérios.  

<h1>☑️ Requisitos não funcionais para o site</h1> 
Para o total funcionamento, a aplicação deve conter:

- `Desempenho`: O site deve funcionar sem travamentos e com agilidade de resposta.
- `Segurança`: O site deve garantir que os dados do cliente estejam em segurança. 

<h1>📊 Modelagem do Banco de Dados</h1> 
<img src="https://github.com/user-attachments/assets/62cb718a-212a-412c-9ae3-a1cea6efd21d" width=1000> 
<img src="https://github.com/user-attachments/assets/6c0889ea-e9b7-4b44-b8b8-c28147963b57" width=1000> 



Esse projeto contará com a seguinte modelagem de dados: 
<br><br> 

- `Tabela Usuários`: Essa tabela é necessária para cadastrar o usuário e seus dados, possuindo campos relacionados ao id, email, nome e telefone. O campo idUsuário é a chave primária da tabela.  
- `Tabela dos Quartos`: Essa tabela é responsável por armazenar as características dos quartos, contendo campos relacionados ao id, capacidade de ocupação do quarto e o preço da diária. O campo idQuartos é a chave primária.
- `Tabela dos Reservas`: Essa tabela é a responsável por fazer a relação entre as outras demais tabelas, onde possui os campos idReserva, checkin, checkout, preco_total, e os id's da tabela quarto e usuário. A chave primária é o campo idReserva, já as chaves estrangeiras são os campos Usuário_idUsuário e Quartos_idQuartos. 


# Desenvolvedores

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/111576177?v=4" width=115><br><sub>Gabriel de Paula Baroni</sub>](https://github.com/Gabriel-Baroni) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/184117774?v=4" width=115><br><sub>Vinícius Ferreira Guimarães Maximo</sub>](https://github.com/vinimaxi) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/184420136?v=4" width=115><br><sub>Renan Alexandre Morais de Souza</sub>](https://github.com/renan-alexandre-morais) |
| :---: | :---: | :---: |








