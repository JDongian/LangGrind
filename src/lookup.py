"""Test Vocab for UT
"""
import vocab

VOCAB = vocab.fetch_json()

if __name__ == "__main__":
    while True:
        #tags = input("EN->KO: ")
        #tags = re.split(r'\s*,+\s*', tags)
        #results = []
        #for term, data in VOCAB.items():
        #    missed_tag = False
        #    for tag in tags:
        #        if tag not in data['definitions']:
        #            missed_tag = True
        #            break
        #    if missed_tag:
        #        continue
        #    results.append(term)
        #print('{%s: %s}' % (tags, str(results)))
        try:
            print(VOCAB[input("KO->EN: ")]['data'])
        except KeyError:
            pass

