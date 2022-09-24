from asyncio import exceptions
import wikipedia

print('what page would you like to see')

user_input = input()
try:
    user_input = wikipedia.page(user_input)
    print(user_input.title)
    print(user_input.content)
except wikipedia.exceptions.PageError:
    print('that page does not exist')
except:
    print('sorry someting went wrong')
