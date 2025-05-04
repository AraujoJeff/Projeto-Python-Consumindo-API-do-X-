import tweepy
import os

# pip install python-dotenv
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Pega o token da variável de ambiente
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

if not BEARER_TOKEN:
     raise ValueError("O token de acesso (BEARER_TOKEN) não foi definido no arquivo .env")

def search_tweets_tweepy(query, max_results=10):
     client = tweepy.Client(bearer_token=BEARER_TOKEN)

     try:
          response = client.search_recent_tweets(
          query=query,
          tweet_fields=['created_at', 'author_id'],
          max_results=max_results
          )

     except tweepy.TooManyRequests:
          print("Limite de requisições atingido. Tente novamente mais tarde.")
          return
     
     if not response.data:
         print("Nenhum tweet encontrado.")
         return
 
     for tweet in response.data:
         print(f"{tweet.created_at} - {tweet.text}")


# Exemplo de uso
if __name__ == "__main__":
     termo_busca = input("Digite o termo que deseja buscar no Twitter: ")
     search_tweets_tweepy(query=termo_busca, max_results=10)