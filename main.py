import gspread
from twitter import *


token = '1381354637928845321-rYBg8SW9EfN7HsmqqpEqHdNAzyC6L7'
token_secret = 'L7eVGxDoFnWRSQ7PXH2nvJUZgZtBo9t6vwmvK1T0yMDNw'
consumer_key= 'ilsHFdkemfpcfx2IZX3HQejlE'
consumer_secret= 'X9fflZ2BZBawyehNDqut6vv4MGObxBZPhRBs3w3U9KpG79QmWe'


# chave pega no site da api do google, so renomeei
gc = gspread.service_account('credentials.json')

t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# inicia um sheet, já criado, no programa
wks = gc.open('philosophy-girl').sheet1

# pegando o texto do campo A2 no sheets
next_tweet = wks.acell('A2').value

# postar tweet atraves da API do twitter

t.statuses.update(
    status= next_tweet)

# deleta linha se tiver sucesso
wks.delete_rows(2)


