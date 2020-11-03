# Desafio Make Magic

O Desafio não foi concluido por completo

A ideia era fazer um CRUD utilizando a API do https://www.potterapi.com/

# Tecnologias Usadas

FrontEnd
- HTML
- CSS

BackEnd
- Postgres
- Python
- Django

# Objetivos Alcançados

- CRUD
- Tratamento de erros nas requisições

# Dificuldades Encontradas

- Pouco conhecimento em criação de APIs REST
- Tempo
- Necessidade de Migração do MYSQL pro Postgres devido a problemas de incompatibilidade do MySQL

# Estrutura do Projeto
<pre>
- desafio_dextra2 
|  
+--- configuracao (Dados Sensíveis)
|   |  
|   |-- .databaseconfig.json  
|   |-- configuracao.py   
|  
+--- desafio_dextra2 (app)  
|   |  
|   |-- settings.py  
|   |-- urls.py  
|   |-- wsgi.py  
|  
+--- personagemapi (app)  
|   |  
|   +-- migrations (arquivos de migração)  
|   |      
|   |-- admin.py
|   |-- apps.py  
|   |-- models.py  
|   |-- pagination.py
|   |-- serializers.py
|   |-- tests.py      
|   |-- urls.py  
|   |-- views.py  
|  
</pre>
