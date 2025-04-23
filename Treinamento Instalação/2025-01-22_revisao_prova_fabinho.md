# 📌 **Diário de Bordo 22/01/2025**
## *Revisão para a prova de instalações do sistema* | Aplicador: **Fabinho**

- ### 📑 Revisão da Estrutura do Sistema

    - Cenários
    - Lógica de funcionamento

---

- ### Instalação do Banco de Dados

    - SQL Server
    - Versão que o coordenador recomendar
    - Versão Express para clientes pequenos, a partir de Standart para clientes maiores
    - Criar usuário `dbatak`
    - Restaurar as 3 bases padrão:
        - CEP_BR
        - LOGSISATAK
        - SATK[ NOME DO CLIENTE ]

---

- ### Solicitação de Licensas

    - Requisitos:
        - CNPJ do Cliente
        - Instância do banco
        - Para fazer o pedido, é necessário ser um `usuário @`
    - Serviço de licenças valida a quantidade de licenças contratadas

---

- ### Configuração do IIS

    - Criação do site
    - Conversão das pastas `API`, `APP` e `CORE` em aplicativos
    - Configuração das pools de aplicativos de forma individual para cada app e para o site principal
        - Campos para configurar:
            - Modo de Início: Always Running
            - Identidade: Local System
            - Intervalo de Tempo Regular (minutos): 480

---

- ### Instalação do ERP (Portal)
    - Criação das pastas `API`, `APP` e `CORE`

---

- ### Instalação do SisAtak
    - Mesmo processo de atualização de versão

---

- ### Criação das Rotinas de Backup

    - Criamos uma cópia da pasta ```BAT de BKP``` na pasta ```C:\MSSQL\BACKUP```
    - Essa pasta (```BAT de BKP```) possui 3 arquivos de rotinas de backup
    - Configuramos esses arquivos para realizar rotinas de backup no sistema (botão direito -> editar).
    - No arquivo alteramos todas as informações na frente dos comandos, o caminho do arquivo e o nome do banco no trecho ```NAME=```.
    - Depois disso copiamos de o que foi feito em um arquivo para outro, alterando apenas o nome do arquivo de saída.

    >### *Informações no arquivo:*
    >| Comando      |    Definição   |
    >|--------------|----------------|
    >| **-S**       | Conexão SQL    |
    >| **-d**       | Base de Dados  |
    >| **-P**       | Senha          |
    >| **-U**       | Usuário        |
    >| **-Q**       | Query          |

    - #### **Automatizando a rotina**

        - Agendador de Tarefas -> Criar Tarefa
        - **Nome:** BKP_[ Turno ]
        - **Marcar a opção:** Executar estando o usuário ou não
        - Disparadores -> Novo -> Diário -> [ Informar a hora ] -> repetir a cada 1 dia
        - Ações -> Novo -> Iniciar um programa -> Selecionar o arquivo que está na pasta ```C:\MSSQL\BACKUP```

---

### Backup manual

- Botão direito na base -> Tarefas -> Fazer Backup
- Tipo de backup: Completo
- Caminho: ```C:\MSSQL\BACKUP\[ NOME DO ARQUIVO ].BAK```

---

- ### Atualização de Versão do Sistema
    > "Sempre feita a quente"
    - #### ERP

        - Copy&Paste nas pastas `API`, `APP` e `CORE` e a pasta portal vai na raiz (ERPATAKX)
        - Parada dos serviços
        - Realização de um Migrate (na instalação do SisAtak ou manualmente)

    - #### SisAtak

        - Reinstalação do servidor sem dependências e instalação das dependências (no servidor)
        - Instalação do arquivo estação (para terminais)
        - Realização de um Migrate (na instalação do SisAtak ou manualmente)

---

- ### Atualização de Versão do Sistema
    - Mesmo processo da atualização de versão, porém sem o Migrate (ERP)
    - Instalação e execução do arquivo Update

---