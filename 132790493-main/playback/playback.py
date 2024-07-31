## Imput the text
playback = input("Text your phrase: ")

## Split the words to prepare the pauses
words = playback.split()

## Add pauses into the spaces
phrase_with_pause = '...'.join(words)

## Print with pauses
print(phrase_with_pause)

