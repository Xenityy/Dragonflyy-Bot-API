import scratch3api as s,os,time
Login=s.Send('-Dragonflyy' ,os.environ['Password'])

project=522112754

def check():
  try:
    time.sleep(.5)
    if int(s.Get.Project(project).cloud()['Send']) == 0:
      user = s.Get.read(f'https://clouddata.scratch.mit.edu/logs?projectid={project}&limit=1000&offset=0')[0]['user']
      try:
        Info = s.Get.read(f'https://scratchdb.lefty.one/v3/user/info/{user}')['statistics']
        os.system('clear')
        Views = Info['views']
        Loves = Info['loves']
        Favorites = Info['favorites']
        Followers = Info['followers']
        Messages = s.Get.User(user).messages()
        Rank = Info['ranks']['followers']

        Login.cloud(project,'Views',Views)
        
        Login.cloud(project,'Loves',Loves)
        
        Login.cloud(project,'Favorites',Favorites)
        
        Login.cloud(project,'Followers',Followers)
        
        Login.cloud(project,'Messages',Messages)
        
        Login.cloud(project,'Rank',Rank)
        
      except:
        pass
      Login.cloud(project,'Send',1)
  except:
    pass