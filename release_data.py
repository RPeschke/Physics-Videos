from googleapiclient.discovery import build

# Your API key goes here - keep it secret!
api_key = 'YOUR_API_KEY'

# The YouTube video ID you want the release date for
video_id = 'VIDEO_ID'

youtube = build('youtube', 'v3', developerKey=api_key)

# Make the API call to get video details
request = youtube.videos().list(
    part='snippet',
    id=video_id
)
response = request.execute()

# Extracting the release date
release_date = response['items'][0]['snippet']['publishedAt'] if response['items'] else None

if release_date:
    print(f"The video was released on {release_date}")
else:
    print("Could not find the video.")