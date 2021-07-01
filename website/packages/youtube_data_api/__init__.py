from youtube_transcript_api import YouTubeTranscriptApi

def getVideoTranscript(video_id):
    yt_transcript = YouTubeTranscriptApi.get_transcript(video_id)

    return yt_transcript