import chromadb



def split_text_into_paragraphs(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    # print(content)
    return content.split('\n\n')




def main():

    paragraphs = split_text_into_paragraphs("handbook.txt")
    print(f"Found {len(paragraphs)} paragraphs.")
    
    client = chromadb.PersistentClient()
    
    collection = client.create_collection('company_handbook')
    
    # We need unique IDs for every paragraph so the database can keep track of them
    ids = [f"para_{i}" for i in range(len(paragraphs))]
    
    collection.add(ids=ids, documents=paragraphs)
    
    print("[ Success ] Handbook embedded and saved to local vector database.")



if __name__ == "__main__":
    main()

