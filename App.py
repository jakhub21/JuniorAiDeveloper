from openai import OpenAI
import os
API_KEY = os.environ.get('GPT_API')

client = OpenAI(
    api_key = API_KEY
)

def read_article(path):
    '''Reads the article from the file'''
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def save_file(ai_content, path):
    '''Saves the AI generated content to a file'''
    with open(path, "w", encoding="utf-8") as file:
        file.write(ai_content)

def generate_summary(article):
    '''Generates a summary of the article using the OpenAI API'''
    prompt = (
            "Przekształć poniższy artykuł na kod HTML, używając odpowiednich tagów HTML do strukturyzacji treści. "
            "Dodaj miejsca na grafiki tam, gdzie są potrzebne, wstawiając tagi <img> z atrybutem src=\"image_placeholder.jpg\" "
            "oraz szczegółowym opisem w alt jako promptem do generowania obrazu."
            "\n\nDodatkowe wymagania dotyczące obrazów:\n"
            "- Wstaw tag <figcaption> pod każdym <img> z opisem grafiki lub zdjęcia oraz kontekstem do artykułu.\n"
            "- Obrazy mają odnosić się do tematów poruszanych w artykule (np. infografiki, ilustracje, zdjęcia związane z omawianymi tematami).\n\n"
            "Zwrócony kod HTML powinien zawierać wyłącznie treść do wstawienia wewnątrz <body> i </body>. Nie uwzględniaj tagów <html>, <head> ani <body>."
            "\n\nOto artykuł:\n\n" + article
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content.strip()

def replace_body_in_template(template_content, body_content):
    """Zastępuje sekcję <body> w szablonie wygenerowanym kodem HTML."""
    start_body = template_content.find("<body>") + len("<body>")
    end_body = template_content.find("</body>")

    if start_body == -1 or end_body == -1:
        raise ValueError("Szablon HTML musi zawierać tagi <body> i </body>.")
    new_content = template_content[:start_body] + "\n" + body_content + "\n" + template_content[end_body:]
    return new_content

def main():
    article = 'artykul.txt'
    html_article = 'artykul.html'
    template_path = 'szablon.html'
    output_path = 'podglad.html'

    article_content = read_article(article)
    template_content = read_article(template_path)

    html_content = generate_summary(article_content)

    save_file(html_content, html_article)

    new_content = replace_body_in_template(template_content, html_content)
    save_file(new_content, output_path)

if __name__ == "__main__":
    main()

