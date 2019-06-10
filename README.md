# Python Crawler - Resultados de Futebol

Um pequeno crawler para pegar resultados de futebol ao vivo.
O crawler coleta as informações do site: https://www.placardefutebol.com.br/

## Funções

* `jogos_de_hoje(format='dict')` - Retorna todos os jogos de hoje (Que aconteceram, que estão acontecendo e os que irão acontecer).
O format indica o tipo de saída.
O format aceita como parâmetro 'json', 'xml' e o padrão 'dict'.

* `jogos_ao_vivo(format='dict')` - Retorna os jogos que estão acontecendo no momento.
O format indica o tipo de saída.
O format aceita como parâmetro 'json', 'xml' e o padrão 'dict'.

* `buscar_jogo_por_time(time)` - Retorna o jogo do time especificado.
retorna vazio se não houver jogos hoje para o time.


## Como instalar?

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