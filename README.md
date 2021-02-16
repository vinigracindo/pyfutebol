# Python Crawler - Resultados de Futebol

Um pequeno crawler para pegar resultados de futebol ao vivo.
O crawler coleta as informações do site: https://www.placardefutebol.com.br/

## Funções

* `jogos_de_hoje(format='dict', cache=True)` - Retorna todos os jogos de hoje (Que aconteceram, que estão acontecendo e os que irão acontecer).
O format indica o tipo de saída.
O format aceita como parâmetro 'json', 'xml' e o padrão 'dict'.
O cache é uma parâmetro que evita consultas ao site toda vez que os métodos forem invocados. Caso você invoque o método com cache=False
o crawler faz uma consulta novamente ao site atualizando os dados.

* `jogos_ao_vivo(format='dict', cache=True)` - Retorna os jogos que estão acontecendo no momento.
O format indica o tipo de saída.
O format aceita como parâmetro 'json', 'xml' e o padrão 'dict'.
O cache é uma parâmetro que evita consultas ao site toda vez que os métodos forem invocados. Caso você invoque o método com cache=False
o crawler faz uma consulta novamente ao site atualizando os dados.

* `buscar_jogo_por_time(time, cache=True)` - Retorna o jogo do time especificado.
retorna vazio se não houver jogos hoje para o time.
O cache é uma parâmetro que evita consultas ao site toda vez que os métodos forem invocados. Caso você invoque o método com cache=False
o crawler faz uma consulta novamente ao site atualizando os dados.


## Como instalar?

Instale as dependências

```console
pip install dicttoxml
pip install lxml
```

Para instalar usando pip:

```console
pip install pyfutebol
```

## Como utilizar?

```python
from pyfutebol import crawler
resultados = crawler.jogos_de_hoje()
for resultado in resultados:
	print(resultado)
```

```python
from pyfutebol import crawler
resultados = crawler.jogos_ao_vivo()
for resultado in resultados:
	print(resultado)
```

```python
from pyfutebol import crawler
resultados = crawler.jogos_ao_vivo(format='json')
print(resultado) # saída em formato json
```

```python
from pyfutebol import crawler
resultado = crawler.buscar_jogo_por_time('flamengo')
print(resultado)
```

## Parâmetro cache

```python
from pyfutebol import crawler
crawler.jogos_de_hoje() # Faz uma consulta no site https://www.placardefutebol.com.br/ e pega os resultados.
crawler.jogos_ao_vivo() # Não faz consulta no site e utiliza os dados obtidos quando o método anterior foi executado.
crawler.jogos_ao_vivo(cache=False) # Faz uma consulta no site https://www.placardefutebol.com.br/ e pega os resultados.
