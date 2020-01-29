import win32.com.client

speaker = win32.client.Dispatch("SAPI.SpVoice")

while 1:
    s = input("Digite uma frase ou palavra:\n")
    speaker.speak(s)
   #ssssssssswawazswa\ws3zaqwsaqwszawzs

teste github   