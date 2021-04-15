import keep_alive,scratch3api,os,time,datetime
from replit import db
keep_alive.keep_alive()
password = os.environ['Password']
Login=scratch3api.Send('-Dragonflyy',password)
os.system('clear')

replies = {"does this work()()()", "yes it does"}

while True:
  #Profile comments
  try:
    Info=scratch3api.Get.User('-Dragonflyy').comment()
    if not Info==db['last']:
      db['last']=Info
      Author=Info['Author']
      Message=Info['Message'].lower()
      os.system('clear')
      print(str(Author),str(Message),sep=': ')
      with open('History.txt','r') as file:
        text=file.read()
        with open('History.txt','w') as file:
          file.write(text+'\n'+Author+': '+Message)
      
      #Follows a user
      if 'follow me' in Message:
        Login.follow(Author)

      #Unfollows a user
      elif 'unfollow me' in Message:
        Login.unfollow(Author)
        
      #Gives..

      #stats of a Project
      elif Message.startswith('project stats: '):
        ProjID=int(Message.split(sep=':')[1])
        Login.comment(scratch3api.Get.Project(ProjID).main(),'Profile',Author)
      
      #Stats of a user
      elif Message.startswith('user stats: '):
        User=Message.split(sep=':')[1].strip()
        Login.comment(scratch3api.Get.User(User).main(),'Profile',Author)

      #Stats of a Studio
      elif Message.startswith('studio stats: '):
        StudioID=Message.split(sep=':')[1].strip()
        Login.comment(scratch3api.Get.Studio(StudioID).main(),'Profile',Author)
      
      #Random Test Commands
      elif Message.lower() == 'developers':
        Login.comment('-Dragonflyy Developers: @-Xenity-,@PikachuB2005,@Classfied3D','Profile',Author) #there

      elif Message.lower() == 'e':
        Login.comment('e' ,'Profile',Author)

      #--> kinda like this <--
      elif Message.lower() == 'admincmd':
        with open('Admin.txt','r') as file:
          if Author in file.read():
            Login.comment('This Works!','Profile',Author)
      
      elif Message.lower() in replies:
        Login.comment(replies[Message.lower()] ,'Profile',Author)
        print("a")
  except:
    Login.comment('An error occured.','Profile','-Dragonflyy')