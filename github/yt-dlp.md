### yt-dlp

Download videos from Internet, like YOUTUBE and BILIBILI.

#### Install yt-dlp in Linux

using Pip, install and update use the same command

```bash
$ python3 -m pip install -U yt-dlp
```

install yt-dlp official Linux repositories

#### Tutorial with Examples

Download a Video or Playlist

```bash
$ yt-dlp URL
```

Download with a custom name, use the `-o` flag

```bash
$ yt-dlp -o 'Lesen' URL
```

Download to a specific location, use the `-P` flag

```bash
$ yt-dlp -P ~/Videos URL
```

To include additional details in the filename, such as the title, uploaded name, upload date,and play-list name

```bash
$ yt-dlp -o `%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s` URL
```

Download Audio-only from a Video

```bash
$ yt-dlp -X URL
$ yt-dlp -X --audio-format mp3 URL
```

Display all available video or play-list formats

```bash
$ yt-dlp --list-formats URL
$ yt-dlp -F URL #-F is shorter
```

Download videos in specific quality and format

- best: selects the highest quality format available
- worst: picks the lowest quality format for both video and audio
- bestvideo: selects the best quality video-only format
- worstvideo: lowest quality video-only format
- bestaudio: best quality audio-only format
- worstaudio: lowest quality audio-only format

```bash
$ yt-dlp -f best URL
```

download video and audio separately, resulting in two files

```bash
$ yt-dlp -f 'bestvideo, bestaudio' URL
```

Downloading videos using format IDs, you can use a comma as separator. using `-f 22, 17, 18` will download three formats

discover IDs by listing

```bash
$ yt-dlp --list-formats URL
```

OR

```bash
$ yt-dlp -F URL
```

