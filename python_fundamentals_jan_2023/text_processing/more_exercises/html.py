def add_text(text, tag):
    return f"<{tag}>\n    {text}\n</{tag}>"


title = input()
article = input()
title_tag = "h1"
article_tag = "article"
comment_tag = "div"
print(add_text(title, title_tag))
print(add_text(article, article_tag))
while True:
    comment = input()
    if comment == "end of comments":
        break

    print(add_text(comment, comment_tag))