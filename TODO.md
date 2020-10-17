# Pipeline
- Adicionar arquivo do típo .ini

# PreProcessing
- Durante a tokenization das sentenças adicionar um id para cada uma.

# PosProcessing
- Adicionar um plugin para posprocessamento, onde recupera os dados do dataset processado
e agrupa em um único arquivo estruturado por camadas níveis de análise lingítica (léxico, sintático e semântico).

# Database
- Testar processamento utilizando banco de dados.
- Create plugin BaseX http://basex.org/

# Documentation
- Gerar o Diagrama de Classes Completo do DeepNLPF utilizando a ferramenta: 
https://gojs.net/latest/samples/umlClass.html

# Output
- Saída dos dados processados no navegador.

# API
- Configurar ip e port pelo terminal CLI.

# DashBoard

- Configura ip e port usando cache do navegador.
- Adicionar plugins pela interface do dashboard.
- Add View Parse Tree.
    - https://gojs.net/latest/samples/parseTree.html
- Add View Procesing Brat.
    - https://github.com/spyysalo/conllu.js
    - https://gojs.net/latest/index.html
    - http://spyysalo.github.io/conllu.js/

# PluginManager
- Instalação de plugins de forma automática. Quando o plugin for adcionado ao pipeline, ele é automaticamente instalado para o usuário.

- Install pip plugin via bash file. Isso evita o passo do usuário instalar a ferramenta.

# Notification
- Notification Speech: https://github.com/desbma/GoogleSpeech

# Otimização de desempenho

    subistituir json por [orjson](https://pypi.org/project/orjson/) 