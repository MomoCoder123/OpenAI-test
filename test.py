import openai
import scratchattach as sa
import time

# Set up your OpenAI API credentials
openai.api_key = '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'
s = sa.login ("LightingGun_test", "yale1288")
conn = s.connect_cloud ("882220066")
word = {'a': '10', 'b': '11', 'c': '12', 'd': '13', 'e': '14', 'f': '15', 'g': '16', 'h': '17', 'i': '18', 'j': '19', 'k': '20', 'l': '21', 'm': '22', 'n': '23', 'o': '24', 'p': '25', 'q': '26', 'r': '27', 's': '28', 't': '29', 'u': '30', 'v': '31', 'w': '32', 'x': '33', 'y': '34', 'z': '35', " ":"36", "!":"37", "?":"38", ",":"39", ".":"40", "'":"41"}
 
def encode(value):
    global word
    val = value.lower()
    res = ""
    word = {'a': '10', 'b': '11', 'c': '12', 'd': '13', 'e': '14', 'f': '15', 'g': '16', 'h': '17', 'i': '18', 'j': '19', 'k': '20', 'l': '21', 'm': '22', 'n': '23', 'o': '24', 'p': '25', 'q': '26', 'r': '27', 's': '28', 't': '29', 'u': '30', 'v': '31', 'w': '32', 'x': '33', 'y': '34', 'z': '35', " ":"36", "!":"37", "?":"38", ",":"39", ".":"40", "'":"41"}     
    for w in val:
        res = res + word[w]
    res = res + "00"
    print(res)
    return res
    #Define a function to send a message and receive a response from ChatGPT
def chat_with_gpt(conversation):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=conversation,
        max_tokens=1000,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=None
    )
    return response.choices[0].text.strip()

def decode(value):
    decoded = ""
    a = list(value)
    for i in range(0,int(len(a)/2)-1):
        #print(str(a[i]+a[i+1]))
        decoded = decoded + list(word)[list(word.values()).index(str(a[2*i])+ str(a[2*i+1]))]
    return decoded
# Start a conversation with ChatGPT
def start_chat():
    print("Welcome to ChatGPT! Type 'exit' to end the conversation.")

    conversation = ""

    while True:
        while True:
           old = sa.get_var("882220066","to_host")
           time.sleep(1)
           if not old == sa.get_var("882220066","to_host"):
                print("not")
                break
        
        dec = decode(sa.get_var("882220066","to_host"))
        user_input = dec

        if user_input.lower() == 'exit':
            break

        # Concatenate user input and conversation history
        conversation += "You: " + user_input + "\n"
        conversation += "ChatGPT: "

        # Get response from ChatGPT
        response = chat_with_gpt(conversation)

        print("ChatGPT:", response)
        encoded = encode(response)
        conn.set_var("from_host", encoded)
        print("sent")

        # Add ChatGPT response to conversation
        conversation += response + "\n"

# Call the start_chat function to begin the conversation
start_chat()
