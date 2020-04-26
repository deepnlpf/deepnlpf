# Pipeline
- Adicionar suporte a um pipeline mais simples, construido com base em um arquivo .ini 

# PosProcessing
- Adicionar um plugin para posprocessamento, onde recupera os dados do dataset processado
e agrupa em um único arquivo estruturado por camadas níveis de análise lingítica (léxico, sintático e semântico).

# Database
Da suporte a armazenamento de dados do tipo documento no formato XML e JSON.
Para isso, será usado a arquitetura de plugins, onde terá plugins construidos 
para banco de dados especificos.

- Plugin: BaseX http://basex.org/
- Plugin: MongoDB

# OUTPUT
- Saída dos dados processados no navegador.
- Saída das análise no modelo Brat.

# Erro no armazenamento das anotações
- ERROR: BSON document too large (25507068 bytes) - the connected server supports BSON document sizes up to 16793598 bytes.

# Time processing 
Processing sentence(s): 8000it [6:22:03,  2.87s/it]

- Adicionar Plugins no site para compatilhamento com os usuários do framework.
- Adicionar plugins pela interface do dashboard.
- Contrubue com uma anotador com base no pipeline custom selecionado pelo usuário.
- Adicionar leitura de arquivos JSON e CSV na classe load_file.
- Escrever documentação com base na documentação do Stanford CoreNLP.

- Add View Tree Brat
https://gojs.net/latest/index.html
http://spyysalo.github.io/conllu.js/

- View DataBase DeepNLPF
https://gojs.net/latest/samples/umlClass.html

- Add View Parse Tree
https://gojs.net/latest/samples/parseTree.html

- Annotation Dataset Como Brat

- Notification Speech
https://github.com/desbma/GoogleSpeech

- [ ] Add Key in API RESTFul

- [ ] TODO Adicionar Pool de processamento paraleno na classe statistics para otimizar as anĺises para corpus longo.

- [ ] TODO: Adicionar uma CLI Interface de Linha de Comando 
<https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df>
<https://realpython.com/command-line-interfaces-python-argparse/> 

- [ ] TODO: Corrigir erro no armazenamento armazenamento dos dados para o CogComp.

- [ ] File config load external tools auto.

- [ ] https://realpython.com/pyspark-intro/

- [ ] [MVC for Flask Application](https://medium.com/@shravan007.c/mvc-for-flask-application-a636e6f58d72)

- [ ] [GraphQL](https://graphql.org/)
https://graphene-python.org/

- [ ] [SSplit StanfodCoreNLP]()
    Pré processamento de dados usando o ssplit do corenlp para identificar as sentenças e salvr no banco de dados. Devido a limitação do tamanho do burf, ele deve analizar o tamanho do documento e dividir quando for necessário.

- [ ] [Clear Data]()
    No pré processamento, o usuário deve informar se deseja limpar os dados que serão salvos, e informar que tipo de limpesa deve ser considerada.

- [ ] []()
    Adicionar WordNet Similaridade.

- [ ] Verify that third party tool is enabled before running.

- [ ] Only upload user-selected plugins into your custom pipeline.

- [ ] Put error handling here to identify when no corpus has been selected.

- [ ] Criar um Doc Code no guia do usuário no site usando Pycco


# API
- Configurar ip e port pelo terminal CLI.

# DashBoard

- Configura ip e port usando cache do navegador.
- 


# PluginManager
- Instalação de plugins de forma automática. Quando o plugin for adcionado ao pipeline, ele é altomaticamente instalado para o usuário.