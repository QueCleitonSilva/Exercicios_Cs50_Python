# User text imput
text = input("Digite algo: ")

# Substitute ":)" to happy emoji
text = text.replace(":)", "🙂")

# Substitute ":(" to a sad emoji
text = text.replace(":(", "🙁")

# Print the imputed text with substitutes emojis
print(text)

