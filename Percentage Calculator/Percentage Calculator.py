print("How many documents did we get today? ")
doc1 = int(input("EOB documents: "))
doc2 = int(input("EOBL documents: "))
doc3 = int(input("ERA documents: "))

total_docs = doc1 + doc2 + doc3

print(f'In total, we received {total_docs} documents.')

print("What was the percentage of each? ")

eob_docs = float(doc1/total_docs*100)
eobl_docs = float(doc2/total_docs*100)
era_docs = float(doc3/total_docs*100)

eob_docs_final = round(eob_docs, 2)
eobl_docs_final = round(eobl_docs, 2)
era_docs_final = round(era_docs, 2)

print(f'In total, EOB items make up {eob_docs_final}%, EOBL items make up {eobl_docs_final}%, and ERA items make up {era_docs_final}%')