
#!/usr/bin/env python
# coding: utf-8

from youtube_transcript_api import YouTubeTranscriptApi
from summarizer import Summarizer




def get_texts_by_id(video_id = 'kEMJRjEdNzM&list=PLoROMvodv4rOhcuXMZkNm7j3fVwBBY42z&index=2'):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

    full_text = gather_text(transcript_list)
    print(len(full_text))
    return full_text

def gather_text(transcript_list):
    full_text = []
    length = len(transcript_list)
    for i in range(length):
        #print(i)
        t = transcript_list[i]["text"]
        full_text.append(t)
    return full_text


def process_text(full_text):
    clean_text = "".join(map(str, full_text))
    return clean_text


def bert_model(clean_text):
    model = Summarizer()
    result = model(clean_text, min_length=60, max_length=500, ratio=0.2)
    summarized_text = "".join(result)
    return summarized_text

def main(video_id):

    raw_text = get_texts_by_id(video_id)
    clean_text = process_text(raw_text)
    return (bert_model(clean_text))



