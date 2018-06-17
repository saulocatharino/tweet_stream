# tweet_stream
Script para scraper no Twitter


Os scripts consultam e analisam os dados da transmissão em tempo-real no Twitter da seguinte forma:

(Precisa de "easy_install ouath2" para acessar o stream do Twitter)

1. ** print.py: ** imprime o texto dos tweets ao vivo. Salve os tweets com `$ python print.py> output.txt`.

2. ** twitterstream.py: ** acessa o stream do Twitter ao vivo e canaliza a saída para o output.txt. Deixe o script ser executado por 10 minutos e finalize com Crtl + c. Envie os tweets ao vivo como `$ python twitterstream.py> output.txt` ou` $ python twitterstream.py> output.json`.

3. ** tweet_sentiment.py: ** deriva o sentimento de cada tweet, atribuindo uma pontuação usando AFINN-111.txt. Execute o script como `$ python tweet_sentiment.py AFINN-111.txt output.txt`.

4. ** frequency.py: ** calcula o termo histograma de frequência dos dados do livestream em output.txt. Execute o script como `$ python frequency.py output.txt`.

5. ** top_ten.py: ** conta as 10 principais hash tags mais frequentes do output.txt. Execute o script como `$ python top_ten.py output.txt`.
