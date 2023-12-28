from youtubesearchpython import VideosSearch
from Database.Commands import select_show_by_id


def search_trailer(id_show, episode):
    show_name = select_show_by_id(id_show).name
    videos_search = VideosSearch(show_name + "episode" + episode + " trailer", limit=10)
    result = videos_search.result()
    for i in result['result']:
        print(i)
    print(result)
    if result['result']:
        return result['result'][0]['link']
    else:
        return None


trailer_link = search_trailer(1, "1")
if trailer_link:
    print(f"Trailer Link: {trailer_link}")
else:
    print("No trailer found.")
