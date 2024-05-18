from twitch_chat_irc import twitch_chat_irc
from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

# def super2():
#   keyboard.press("s")
#   sleep(0.016)
#   keyboard.press("d")
#   sleep(0.016)
#   keyboard.release("s")
#   sleep(0.016)
#   keyboard.release("d")
#   keyboard.press("s")
#   sleep(0.016)
#   keyboard.press("d")
#   sleep(0.016)
#   keyboard.release("s")
#   sleep(0.016)
#   keyboard.release("d")
#   sleep(0.016)
#   keyboard.press("i")
#   sleep(0.016)
#   keyboard.release("i")

def downback():
  keyboard.press("a")
  keyboard.press("s")
  sleep(0.016)
  keyboard.release("a")
  keyboard.release("s")

def downforward():
  keyboard.press("s")
  keyboard.press("d")
  sleep(0.016)
  keyboard.release("s")
  keyboard.release("d")

def holddownback():
  keyboard.press("a")
  keyboard.press("s")
  sleep(2.0)
  keyboard.release("a")
  keyboard.release("s")

def holddown():
  keyboard.press("s")
  sleep(2.0)
  keyboard.release("s")

def holdleft():
  keyboard.press("a")
  sleep(2.0)
  keyboard.release("a")

def holdright():
  keyboard.press("d")
  sleep(2.0)
  keyboard.release("d")

def jump():
  keyboard.press(Key.space)
  sleep(0.016)
  keyboard.release(Key.space)

def jumpleft():
  keyboard.press(Key.space)
  keyboard.press("a")
  sleep(0.016)
  keyboard.release(Key.space)
  keyboard.release("a")

def jumpright():
  keyboard.press(Key.space)
  keyboard.press("d")
  sleep(0.016)
  keyboard.release(Key.space)
  keyboard.release("d")

def super1():
  keyboard.press("d")
  sleep(0.016)
  keyboard.press("s")
  sleep(0.016)
  keyboard.release("d")
  sleep(0.016)
  keyboard.press("a")
  sleep(0.016)
  keyboard.release("s")
  sleep(0.016)
  keyboard.release("a")
  sleep(0.016)
  keyboard.press("d")
  sleep(0.016)
  keyboard.press("i")
  sleep(0.016)
  keyboard.release("d")
  keyboard.release("i")
  sleep(0.016)

def super2():
  keyboard.press("d")
  sleep(0.016)
  keyboard.press("s")
  sleep(0.016)
  keyboard.release("d")
  sleep(0.016)
  keyboard.press("a")
  sleep(0.016)
  keyboard.release("s")
  sleep(0.016)
  keyboard.release("a")
  sleep(0.016)
  keyboard.press("d")
  sleep(0.016)
  keyboard.press("o")
  sleep(0.016)
  keyboard.release("d")
  keyboard.release("o")
  sleep(0.016)

def button(button):
  keyboard.press(button)
  sleep(0.016)
  keyboard.release(button)
  sleep(0.016)

def move(button):
  keyboard.press(button)
  sleep(0.016)
  keyboard.release(button)

def command_normal(button1, button2):
  keyboard.press(button1)
  keyboard.press(button2)
  sleep(0.016)
  keyboard.release(button1)
  keyboard.release(button2)

connection = twitch_chat_irc.TwitchChatIRC()

cookieonly = False

attack_conversion = {
  "p": "j",
  "k": "u",
  "s": "i",
  "h": "o",
  "d": "l",
  "e": "e",
  "q": "q",
  "t": "p"
}

def controls_processor(message):
  text = message["message"].lower()
  # print(message["display-name"] + ": " + text + "\n")

  if cookieonly == True and message["display-name"] != "ctrlaltCookie":
    return
  
  if "super1"in text:
    return super1()
  if "super2"in text:
    return super2()

  if "w6" in text: # wait  forward
    print("walking 6")
    holdright()
  if "w4" in text: # wait  backward
    print("walking 4")
    holdleft()
  if "w2" in text: # wait  backward
    print("holding down")
    holddown()
  if "e" in text: # faultless defense
    print("faultless defense yay")
    button("e")
  if "run" in text:
    print("running")
    button("k")

  if len(message["message"]) < 80:
    for x in range(len(message["message"])):
      try:
         do_move(text[x], x, text)
      except:
         print("some shit happened")

def do_move(message, pos, fullmessage):
  if "z" in message:
    print("sleep 80ms")
    sleep(0.080)
    return
  if "1" in message:
    print("1")
    downback()
  if "2" in message:
    if "2" in message and len(fullmessage) > pos + 1:
        if fullmessage[pos+1] in attack_conversion:
          print("2" + attack_conversion[fullmessage[pos+1]])
          return command_normal("s", attack_conversion[fullmessage[pos+1]])
    print("2")
    move("s")
  if "3" in message:
    print("3")
    downforward()
  if "4" in message:
    if "4" in message and len(fullmessage) > pos + 1:
        if fullmessage[pos+1] in attack_conversion:
          print("4" + attack_conversion[fullmessage[pos+1]])
          return command_normal("a", attack_conversion[fullmessage[pos+1]])
    print("4")
    move("a")
  if "6" in message:
    if "6" in message and len(fullmessage) > pos + 1:
        if fullmessage[pos+1] in attack_conversion:
          print("6" + attack_conversion[fullmessage[pos+1]])
          return command_normal("d", attack_conversion[fullmessage[pos+1]])
    print("6")
    move("d")
  if "7" in message:
     print("7")
     jumpleft()
  if "8" in message:
    print("8")
    jump()
  if "9" in message:
     print("9")
     jumpright()
  if "p" in message:
    print("punch")
    button("j")
  if "k" in message:
    print("kick")
    button("u")
  if "s" in message:
    print("slash")
    button("i")
  if "h" in message:
    print("heavyslash")
    button("o")
  if "d" in message:
    print("dust")
    button("l")
  if "t" in message: # taunt
    print("get taunted dickhead")
    button("p")
  if "q" in message: # romance cancel
    print("roman cancel")
    button("q")
  if "b" in message: # romance cancel
    print("roman cancel")
    holddownback()

## your username goes here
connection.listen('your username goes here', on_message=controls_processor)
