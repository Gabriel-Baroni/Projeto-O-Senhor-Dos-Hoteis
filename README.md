<h1 align="center"> O SENHOR DOS HOTÉIS </h1>
<p align="center">Um trabalho para a disciplina de DESENVOLVIMENTO DE APLICAÇÕES COM BANCO DE DADOS - 3º Informática do IFSP-Jacareí</p>
<br>
<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>

<h1>👨‍🏫 Professores responsáveis</h1> 

-  Carlos Eduardo Duque Polito
-  Olavo Olimpo de Matos Junior 

<h1>🎯 Objetivo do projeto</h1> 
O objetivo desse projeto é construir um site de reserva para uma hotelaria fictícia, que no caso é a hotelaria "O Senhor Dos Hotéis". Esta, possui a temática inspirada no vasto universo pertencente a franquia de "O Senhor dos Anéis". 
<br>

<h1>✖️ O que não é o objetivo do projeto</h2>
Por se tartar de um protótipo e um trabalho em pequena escala, somente com fim de teste de conhecimentos, o site não contará com:

- `Escabilidade` Os desenvolvedores não estaram preocupados com a escabilidade do projeto 
- `Métodos de pagamento`: O site conterá com uma página para pagamento da reserva, porém por se tratar de uma hotelaria fictícia, não será possível realizar nenhuma espécie de pagamento. 

<h1>👥 Público-alvo</h2>
O tema do hotel e, consequentemente, do site será, como já mencionado, sobre "O Senhor dos Anéis". O público-alvo desse site será aventureiros que sempre quiseram se sentir neste universo rico em magia e mistérios. 

<h1>:hammer: Funcionalidades do projeto</h2>

- `Registro de clientes`: Um sistema de cadastro de clientes à um banco de dados.
- `Autenticação de conta`: Uma vez já cadastrado, o usuário poderá fazer login no site sem precisar refazer o cadastro. 
- `Reserva de um quarto de hotel `: Um sistema de busca por quartos disponíveis para serem reservados. Essa busca ocorrerá na base de dados da hotelaria.
  
<h1>☑️ Requisitos não funcionais para o site</h1> 
Para o total funcionamento, a aplicação deve conter:

- `Desempenho`: O site deve funcionar sem travamentos e com agilidade de resposta.
- `Segurança`: O site deve garantir que os dados do cliente estejam em segurança.

<h1>📑 Matriz de Requisitos</h1>
<img src="https://github.com/user-attachments/assets/2743c732-f86c-4b2d-82a0-d9670abd84e6" width=1000> 

<h1>📊 Modelagem do Banco de Dados</h1> 
<img src="https://github.com/user-attachments/assets/f478260d-83f6-4f89-89a6-bb44cc65bb63" width=1000> 
<img src="https://github.com/user-attachments/assets/01773011-fe08-4dcf-ba66-b3a0956053bc" width=1000> 

<h1>📖 Dicionário de Dados</h1> 

Esse projeto contará com as seguintes Entidades e atributos

<h2>Entidade Usuário</h2>
 Essa entidade é necessária para cadastrar o cliente (quem realiza a reserva) e seus dados, possuindo os campos id, email, nome, telefone e senha. 
 <br><br>
 
- `idUsuário`: É um atributo do tipo INT. É o responsável por criar um **Id único** para o usuário, que no caso é o cliente que fará a reserva (**CHAVE PRIMÁRIA**).
- `email`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar o e-mail que o usuário cadastrou.
- `nome`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar o nome do usuário.
- `telefone`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar o número de telefone do usuário.
- `senha`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar a senha que o usuário cadastrou.
- `created_at`: É um atributodo tipo DATE. É o responsável por armazenar a data em que o usuário realizou o cadastro.
  
<h2>Entidade Quarto</h2>
Essa entidade é responsável por armazenar as características dos quartos, contendo campos relacionados ao id, capacidade de ocupação do quarto, o preço da diária e a disponibilidade do mesmo.
<br><br>

- `idQuartos`: É um atributo do tipo INT. É o responsável por criar um **Id único** (**CHAVE PRIMÁRIA**).
- `capacidade`: É um atributo do tipo INT. É o responsável por armazenar a capacidade máxima de pessoas em um quarto.
- `preco_diaria`: É um atributo do tipo FLOAT. É o responsável por armazenar o preço de uma diária do quarto.
- `nome`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar o nome do quarto.
- `Disponibilidade`: É um atributo do tipo INT. É o responsável por armazenar a disponibilidade do quarto, se for igual a 1 significa que o quarto esta disponível, se for igual a zero significa que esta indisponível.
- `imagem`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. é o responsável por armazear o relative path da imagem específica do quarto.

<h2>Entidade Reserva</h2>
Essa entidade é a responsável por fazer a relação entre as outras demais tabelas, onde possui os campos id, checkin, checkout, preco_total, e os id's da tabela quarto e usuário. 
<br><br>

- `IdReserva`: É um atributo do tipo INT. É o responsável por criar um **Id único** (**CHAVE PRIMÁRIA**).
- `checkin`: É um atributo do tipo DATE. É o responsável por armazenar a data em que o usuário irá começar sua estadia no hotel.
- `checkout`: É um atributo do tipo DATE. É o responsável por armazenar a data em que o usuário irá terminar sua estadia no hotel.
- `preco_total`:  É um atributo do tipo FLOAT. É o responsável por armazenar o preço total de uma reserva, ou seja, o número de dias da estadia vezes o preco da diária.
- `Usuário_IdUsuário`: É um atributo do tipo INT. É o responsável por relacionar a tabela Reversa com a tabela Usuário através do id (**CHAVE ESTRANGEIRA**).
- `Quartos_IdQuartos`: É um atributo do tipo INT. É o responsável por relacionar a tabela Reversa com a tabela Quartos através do id (**CHAVE ESTRANGEIRA**).
- `data_reserva`: É um atributo do tipo DATE. É o responsável por armazenar a data em que o usuário efetuou a reserva.

<h2>Entidade Reserva Expirada</h2>
Essa entidade é a responsável por armazenar todas as reservas em que a data de check-out é mais velha que a data atual, ou seja, reservas que já acabaram. Os atributos da entidade possuem tipos e funções iguais a da entidade Reserva.

<h1>🧍Diagramas UML</h1>
<h2>Tela de Login e Cadastro</h2>
<img src="https://github.com/user-attachments/assets/cb65be56-2ea6-4079-b689-b70429d4490b" width=1000>
<h2>Tela inicial, quartos e reserva</h2>
<img src="https://github.com/user-attachments/assets/3afa9e98-c9fa-416e-a6ac-0a7eca64ab13" width=1000>



<h1>🧰 Tecnologias Utilizadas</h1> 

`Front-end`:
<br><br>
<img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E">

`Back-end`:
<br><br>
<img src="https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">

`Banco de Dados`:
<br><br>
<img src="https://img.shields.io/badge/supabase-%2300C4B7.svg?style=for-the-badge&logo=supabase&logoColor=white">
<img src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white">

`Diagramas e Mockups`:
<br><br>
<img src="https://img.shields.io/badge/Cisco%20Packet%20Tracer-%23049fd9.svg?style=for-the-badge&logo=cisco&logoColor=white">
<img src="https://img.shields.io/badge/Miro-%23000000.svg?style=for-the-badge&logo=miro&logoColor=white">
<img src="https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=canva&logoColor=white">
<img src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white">

<h1>🏗️ Arquitetura da Aplicação</h1> 
<h2>Arquitetura do Software</h2>
<img src="https://github.com/user-attachments/assets/49e11b13-c231-4ae7-ae38-222c95d66f3e" width=1000> 
<h2>Arquitetura de Rede da Hotelaria</h2>
<img src="https://github.com/user-attachments/assets/8de6fe1c-e573-4cf2-98cb-f2a7a5097bda" width=1000> 

<p>Adicionar diagram UML, estudo de caso e matriz de requisito</p>

# 🧑‍💻 Desenvolvedores

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/111576177?v=4" width=115><br><sub>Gabriel de Paula Baroni</sub>](https://github.com/Gabriel-Baroni) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/184117774?v=4" width=115><br><sub>Vinícius Ferreira Guimarães Maximo</sub>](https://github.com/vinimaxi) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/184420136?v=4" width=115><br><sub>Renan Alexandre Morais de Souza</sub>](https://github.com/renan-alexandre-morais) |
| :---: | :---: | :---: |










