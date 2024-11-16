import calamity

# Just a basic shell
# The name calamity means:
# an event causing great and often sudden damage or distress; a disaster.
# Which is really just what this language is.

while True:
    text = input('Calamity> ')
    if text.strip() == "": continue
    result, error = calamity.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
