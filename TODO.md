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