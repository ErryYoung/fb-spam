import requests
import time

def get_reels(country, niche):
  """
  Mengembalikan list reels dari negara dan niche yang ditentukan

  Args:
    country: Negara target
    niche: Niche target

  Returns:
    List reels
  """

  url = "https://graph.facebook.com/v12.0/reels?fields=id,media_url,permalink,owner&country_code={country}&q={niche}"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    return data["data"]
  else:
    return []

def post_comment(reel_id, link):
  """
  Memposting komentar link di reel yang ditentukan

  Args:
    reel_id: ID reel
    link: Link yang akan diposting
  """

  url = "https://graph.facebook.com/v12.0/reels/{reel_id}/comments"
  data = {"text": link}
  response = requests.post(url, json=data)
  if response.status_code == 200:
    print(f"Komentar berhasil diposting di reel {reel_id}")
  else:
    print(f"Gagal memposting komentar di reel {reel_id}")

def spam_comments(link, country, niche):
  """
  Menjalankan script spam komentar link

  Args:
    link: Link yang akan dispam
    country: Negara target
    niche: Niche target
  """

  reels = get_reels(country, niche)
  for reel in reels:
    post_comment(reel["id"], link)
    time.sleep(1)

if __name__ == "__main__":
  link = "https://www.toprevenuegate.com/sgv3th8pw?key=54d1fb41974070027502357fe32b53c8"
  country = "us"
  niche = "sexy"
  spam_comments(link, country, niche)
