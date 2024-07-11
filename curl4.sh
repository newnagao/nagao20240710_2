#!/bin/bash

url="https://onsei-kensho.openai.azure.com/openai/deployments/tts-model/audio/speech?api-version=2024-02-15-preview"
key_pm="api-key:ffec39680f7b4946a392784be5798e72"
json="{\"model\": \"tts\", \"input\": \"$1\", \"voice\": \"alloy\"}"
outputfilename="$2"

curl -k "$url" -H "$key_pm" -H "Content-Type:application/json" -d "$json" --output "$outputfilename"
