from collections import deque

def bfs_find_answer(faq_graph, query):
    queue = deque([query])  # Inisialisasi queue dengan pertanyaan awal
    visited = set()  # Menyimpan node yang sudah dikunjungi

    while queue:
        node = queue.popleft()  # Ambil elemen pertama dalam queue
        
        # Jika node memiliki jawaban dalam dictionary "answers"
        if node in faq_graph.get("answers", {}):
            return faq_graph["answers"][node]

        if node not in visited:
            visited.add(node)  # Tandai sebagai telah dikunjungi
            queue.extend(faq_graph.get(node, []))  # Tambahkan anak node ke dalam queue

    return "Jawaban tidak ditemukan."

# Contoh data FAQ Knowledge Graph
faq_graph = {
    "What is AI?": ["Machine Learning", "Deep Learning"],
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning"],
    "Deep Learning": ["Neural Networks"],
    "answers": {
        "Neural Networks": "Neural Networks are AI models inspired by the human brain.",
        "Supervised Learning": "Supervised Learning uses labeled data for training."
    }
}

# Contoh penggunaan untuk mencari jawaban
query = "What is AI?"
print("Jawaban:", bfs_find_answer(faq_graph, query))  # Output: Jawaban dari FAQ Graph
