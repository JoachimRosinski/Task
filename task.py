import os
from openai import OpenAI

openaiapi_key = os.getenv("OPENAI_API_KEY")
# alternative without system env:
# openaiapi_key = "<your_api_key>"
client = OpenAI(api_key=openaiapi_key)


def read_article(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File {filepath} not found.")
    except Exception as e:
        raise Exception(f"Error while reading the file: {e}")


def format_prompt(article_content):
    return (
        "Please convert the following article into HTML with the following requirements:\n"
        "- Structure the content using appropriate HTML tags.\n"
        "- Mark recommended locations for images using <img> tags with src='image_placeholder.jpg' and in alt text, "
        "write a detailed prompt in that can be used to generate the image. The prompt should describe the image in "
        "detail, for example, 'A serene landscape with mountains in the background, a clear blue sky, and a small "
        "river running through the foreground, in the style of a realistic painting'. \n"
        "- Under each image, generate a caption in Polish that fits the context of the image.\n"
        "- Exclude any CSS or JavaScript code.\n"
        "Return only the content that should go between <body> and </body> tags, dont include <body> and </body> "
        "tags.\n"
        "Here is the article:\n\n"
        f"{article_content}"
    )


def generate_html_article(article_content):
    prompt = format_prompt(article_content)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for converting text to HTML."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()


def save_html(filepath, content):
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        raise Exception(f"Error while saving the file: {e}")


def main():
    try:
        article_path = "art.txt"
        article_content = read_article(article_path)
        html_content = generate_html_article(article_content)
        output_path = "artykul.html"
        save_html(output_path, html_content)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
