from youtubesearchpython import VideosSearch

def search_trailer(id_show, episode, query):
    videosSearch = VideosSearch(query + " trailer", limit = 3)
    result = videosSearch.result()
    print(result)
    if result['result']:
        return result['result'][0]['link']
    else:
        return None

# Usage
query = "star wars episode 1"
trailer_link = search_trailer(query)
if trailer_link:
    print(f"Trailer Link: {trailer_link}")
else:
    print("No trailer found.")
