import sys
input = sys.stdin.readline


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
