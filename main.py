import gspread
from twitter import *
import secrets




# chave pega no site da api do google, so renomeei
gc = gspread.service_account('credentials.json')

t = Twitter(
    auth=OAuth(secrets.token, secrets.token_secret, secrets.consumer_key, secrets.consumer_secret))

# inicia um sheet, já criado, no programa
wks = gc.open('philosophy-girl').sheet1

# pegando o texto do campo A2 no sheets
next_tweet = wks.acell('A2').value

# postar tweet atraves da API do twitter

t.statuses.update(
    status= next_tweet)

# deleta linha se tiver sucesso
wks.delete_rows(2)


