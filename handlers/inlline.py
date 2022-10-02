from youtube_search import YoutubeSearch as YT
import hashlib
from aiogram import types, Dispatcher


def finder(text):
    return YT(text, max_results=10).to_dict()


# async def inline_youtube_handler(query: types.InlineQuery):
#     text = query.query or "echo"
#     links = finder(text)
#     articles = [types.InlineQueryResultArticle(
#         id=hashlib.md5(f"{link['id']}".encode()).hexdigest(),
#         title=link['title'],
#         url=f"https://www.youtube.com{link['url_suffix']}",
#         thumb_url=f"{link['thumbnails'][0]}",
#         input_message_content=types.InputMessageContent(
#             message_text=f"https://www.youtube.com{link['url_suffix']}"
#         )
#     ) for link in links]
#     await query.answer(articles, cache_time=60)


async def inline_google_handler(query: types.InlineQuery):
    text = query.query or "echo"
    link = f"https://www.google.ru/search?q{text}"
    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(text.encode()).hexdigest(),
        title="Google: ",
        url=link,
        input_message_content=types.InputMessageContent(
            message_text=link
        )
    )]
    await query.answer(articles, cache_time=60)

def register_handlers_inline(dp: Dispatcher):
    # dp.register_inline_handler(inline_youtube_handler)
    dp.register_inline_handler(inline_google_handler)