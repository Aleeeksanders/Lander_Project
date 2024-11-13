import json
import os
import random

# Dentro de nlp_processor.py
from modules.nlp.knowledge_manager import KnowledgeManager

class DatasetIntegrator:
    def __init__(self, dataset_path='cornell_movie_dialogues.txt', knowledge_file='modules/nlp/knowledge_base.json'):
        self.dataset_path = dataset_path
        self.knowledge_file = knowledge_file
        self.knowledge = {}
        self.load_knowledge()

    def load_knowledge(self):
        """Carga la base de conocimiento desde un archivo JSON."""
        if os.path.exists(self.knowledge_file):
            with open(self.knowledge_file, 'r', encoding='utf-8') as file:
                self.knowledge = json.load(file)
        else:
            self.knowledge = {"conversaciones": [], "faq": []}

    def save_knowledge(self):
        """Guarda la base de conocimiento en un archivo JSON."""
        with open(self.knowledge_file, 'w', encoding='utf-8') as file:
            json.dump(self.knowledge, file, ensure_ascii=False, indent=4)

    def process_dataset(self):
        """Procesa el archivo de diálogos y agrega pares de pregunta-respuesta a la base de conocimiento."""
        if not os.path.exists(self.dataset_path):
            print("Dataset no encontrado. Verifica la ruta.")
            return
        
        with open(self.dataset_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        for i in range(0, len(lines) - 1, 2):  # Toma pares de líneas
            question = lines[i].strip()
            answer = lines[i + 1].strip()

            # Agrega a la base de conocimiento
            self.add_to_knowledge(question, answer)
        
        self.save_knowledge()
        print("Dataset integrado exitosamente en la base de conocimiento.")

    def add_to_knowledge(self, question, answer):
        """Agrega un par de pregunta-respuesta a la base de conocimiento."""
        for item in self.knowledge["conversaciones"]:
            if item["query"].lower() == question.lower():
                if answer not in item["response"]:
                    item["response"].append(answer)
                return

        # Si la pregunta no existe, se añade
        self.knowledge["conversaciones"].append({"query": question, "response": [answer]})

# Uso del script
if __name__ == "__main__":
    integrator = DatasetIntegrator(dataset_path='ruta/al/archivo/cornell_movie_dialogues.txt')
    integrator.process_dataset()
