from youtube_transcript_api import YouTubeTranscriptApi

def getVideoTranscript(video_id):
    try:
        yt_transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except: 
        yt_transcript = [{'start': 0, 'text': 'No Transcript'}]

    return yt_transcript