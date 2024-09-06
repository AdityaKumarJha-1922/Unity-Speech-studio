# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:48:05 2024

@author: adity
"""

import openai
import os
import sys

# Fetch the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

if openai.api_key is None:
    raise ValueError("The OpenAI API key is missing. Please set the OPENAI_API_KEY environment variable.")

def generate_feedback(transcript):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert in speech evaluation. Analyze the conversation and provide feedback."},
            {"role": "user", "content": transcript}
        ],
        temperature=0.5,
        max_tokens=1024
    )

    feedback = response['choices'][0]['message']['content']
    return feedback

if __name__ == "__main__":
    # Read the transcript from the first command line argument
    transcript = sys.argv[1]

    # Generate feedback
    feedback = generate_feedback(transcript)

    # Output the feedback
    print(feedback)
