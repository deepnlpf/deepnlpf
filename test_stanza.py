import stanza

#stanza.download('en')
nlp = stanza.Pipeline('en')
doc = nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")
doc.sentences[0].print_dependencies()