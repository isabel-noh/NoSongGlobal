import requests
import pprint

def popular_movies():

    BASE_URL = 'http://api.themoviedb.org/3'

    # 1. URL 정보 설정
    # http://developers.themoviedb.org/3/movies/get-popular-movies
    # path = '/movie/popular'
    url = "https://api.themoviedb.org/3/movie/top_rated?api_key=9aef886051103d6c65ad737f677114e5&language=ko-KR&page="
    # params = {
    #     'api_key': '9aef886051103d6c65ad737f677114e5',
    #     'language': 'ko',
    #     'region': 'KR',
    # }

    #2. 요청 및 응답
    response = requests.get(BASE_URL + path, params=params).json()
    results = response.get('results')

    return results


if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    for i in popular_movies():
        print(i)