import scratch3api as s, os

Characters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '-', '_',' ','0','1','2','3','4','5','6','7','8','9']
Login = s.Send('-Dragonflyy',os.environ['Password'])

def data():
  data = []
  page = s.Get.read('https://scratchdb.lefty.one/v2/user/rank/global/followers/0')['users']
  for user in page:
    data.append([user['info']['username'],user['followers']])
  return data

def encode(string):
  encoded=''
  for letter in range(len(string)):
    encoded += str(Characters.index(string[letter])+10)
  return encoded

def update():
  try:
    data1 = data()
    string = ''
    for i in data1[0:5]:
      string = ' '.join([string,i[0],str(i[1])])
    encoded = encode(string)
    Login.cloud(522564331,'Data',encoded)
    string = ''
    for i in data1[6:11]:
      string = ' '.join([string,i[0],str(i[1])])
    encoded = encode(string)
    Login.cloud(522564331,'Data2',encoded)
  except:
    pass
