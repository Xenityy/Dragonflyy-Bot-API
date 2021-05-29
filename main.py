import keep_alive,scratch3api,os, time
import Messages,Stats, Top
keep_alive.keep_alive()
Login=scratch3api.Send('-Dragonflyy' ,os.environ['Password'])
os.system('clear')

while True:
  os.system('clear')
  print('Updating message count...')
  Messages.update()
  time.sleep(.5)
  print('Checking for user stats...')
  Stats.check()
  time.sleep(.5)
  print('Updating top scratchers...')
  Top.update()
  time.sleep(.5)

#yo
#wassup
