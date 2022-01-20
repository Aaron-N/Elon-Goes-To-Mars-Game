"""
Where that sweet, sweet text-parsing magic happens
"""

import parserVocabulary


class TextParser:

    def __init__(self):
        self.rooms = parserVocabulary.rooms
        self.actions = parserVocabulary.actions
        self.directions = parserVocabulary.directions
        self.features = parserVocabulary.features
        self.objects = parserVocabulary.objects
        self.prepositions = parserVocabulary.prepositions
        self.help = parserVocabulary.help

    # Get user input
    def getUserInput(self, prompt):
        userinput = input(prompt)
        return userinput

    # Convert user input to lowercase
    def inputToLowercase(self, userinput):
        lowercased = userinput.lower()
        return lowercased

    # Parse user input into a list of words
    def parseUserInput(self, lowercased):
        splitwordlist = lowercased.split()
        return splitwordlist

    # Remove any non-vocabulary words from list
    def removeInvalidWords(self, splitwordlist):
        vocabulary = self.rooms + self.actions + self.directions + \
                     self.features + self.objects + self.prepositions
        cleaned = []
        for word in splitwordlist:
            if word in vocabulary:
                cleaned.append(word)
        return cleaned

    # Convert cleaned list back into a string, remove 's or ', and return
    def backToString(self, cleaned):
        commandstring = ""
        for ele in cleaned:
            commandstring += ele
        commandstring = commandstring.replace("'s", "")
        commandstring = commandstring.replace("'", "")
        return commandstring

    # The all-encompassing text-parsing function
    def commandParser(self, prompt):
        inputcommand = self.getUserInput(prompt)
        loweredcommand = self.inputToLowercase(inputcommand)
        parsedcommand = self.parseUserInput(loweredcommand)
        scrubbedcommand = self.removeInvalidWords(parsedcommand)
        stringcommand = self.backToString(scrubbedcommand)
        return stringcommand

