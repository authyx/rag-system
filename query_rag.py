import chromadb
from groq import Groq
import sys

def main():
    if len(sys.argv) < 2:
        print("Please provide a question!")
        return
    question = sys.argv[1]

    client = chromadb.PersistentClient()

    collection = client.get_collection("company_handbook")

    results = collection.query(query_texts=[question], n_results=4)

    # This extracts the retrieved text from the dictionary that ChromaDB returns
    retrieved_paragraphs = results['documents'][0]
    context_text = "\n\n".join(retrieved_paragraphs)
    
    print(f"--- Retrieved Context ---\n{context_text}\n-----------------------")

    
    groq_client = Groq()

    system_prompt = f"""
    You are a good reader
    Answer Only based on the contet, if there is no anwer in it say you do not know.
    CONTEXT:
    {context_text}
    """

    completion = groq_client.chat.completions.create(model="openai/gpt-oss-20b", messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": question}], temperature=0.2)

    print("\nAI Answer:")
    print(completion.choices[0].message.content)

if __name__ == "__main__":
    main()