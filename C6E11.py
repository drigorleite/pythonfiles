def generate_web_page():
    name = input("Enter your name: ")
    description = input("Enter a sentence that describes yourself: ")
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Personal Web Page</title>
    </head>
    <body>
        <h1>{name}</h1>
        <p>{description}</p>
    </body>
    </html>
    """
    with open("personal_page.html", "w") as file:
        file.write(html_content)
    print("HTML file generated successfully!")


generate_web_page()
