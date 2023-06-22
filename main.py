import datetime
import openai
import os

openai.api_key = ''  # your OpenAI API key

messages = [
    {"role": "system", "content": "You are a WB, specialised website builder, a help assistant who helps people to create Html pages,which includes html code, css code and java script code.You include all code in html code only so user does not any other file other than index.html like style.css , script.js.write css code inside <style></style> and js code in <script></script> You are created by Samarpan Mohanty."}
]

def generate_response(query):
    message = query
    if message:
        messages.append({"role": "user", "content": message})

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content
    while '`' in reply:
        reply = reply.replace('`', '')

    return reply

def greet():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        return "Good Morning!"
    
    elif hour >= 12 and hour < 18:
        return "Good Afternoon!"
    
    else:
        return "Good Evening!"

def create_files(file_data):
    for file_name, content in file_data.items():
        with open(file_name, "w") as file:
            file.write(content)

def main():
    greeting = greet()
    print(greeting)

    while True:
        query = input("User: ").lower()
        if query == "quit":
            print('WB: Sure, feel free to reach out to me if you need any assistance in the future. Have a good day!')
            break
        if query:
            response = generate_response(query)
            print(f"SVA: {response}")

            if "make a" in query and "website" in query:
                file_data = {
                    "index.html": "<!-- HTML code goes here -->"
                }
                create_files(file_data)

                # Write GPT-3 generated code into files
                file_data["index.html"] = response
                create_files(file_data)

                print("SVA: File created successfully.Check if the style and script code not written in script and style tag respectively.")
                continue

if __name__ == "__main__":
    main()
