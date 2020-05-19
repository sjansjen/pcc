favorite_language = 'python ' # there's extra space after string
print(favorite_language)
print(favorite_language.rstrip()) # strip temporarily
print(favorite_language) # back to original value

favorite_language = favorite_language.rstrip() # strip permanently
print(favorite_language)

favorite_language2 = ' python '
print(favorite_language2.rstrip()) # strip right side only
print(favorite_language2.lstrip()) # strip left side only
print(favorite_language2.strip()) # strip both side
