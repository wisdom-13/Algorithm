import sys
input = sys.stdin.readline


# 1. songs 딕셔너리에서 음이름의 첫 3개와 search_pitch가 일치하는 노래를 체크
# 2. 없다면 !, 1개 이상이라면 ?, 1개라면 곡이름을 return
def search_song(songs, search_pitch):
    result = '!'
    for title, pitch in songs.items():
        if pitch[0:3] != search_pitch:
            continue

        if result != '!':
            result = '?'
            break

        result = title

    return result


def main():
    songs = {}
    N, M = map(int, input().rstrip().split())
    for _ in range(N):
        parts = input().rstrip().split()
        songs[parts[1]] = "".join(parts[2:])

    for _ in range(M):
        pitch = input().rstrip().replace(" ", "")
        print(search_song(songs, pitch))


if __name__ == "__main__":
    main()
