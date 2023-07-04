from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    @classmethod
    def add_elements(cls, element, lst):
        if element not in lst:
            lst.append(element)

    def add_category(self, category: Category) -> None:
        return Storage.add_elements(category, self.categories)

    def add_topic(self, topic: Topic) -> None:
        return self.add_elements(topic, self.topics)

    def add_document(self, document: Document) -> None:
        return self.add_elements(document, self.documents)

    def edit_category(self, category_id: int, new_name: str) -> None or str:
        try:
            c_category = next(filter(lambda x: x.id == category_id, self.categories))
        except StopIteration:
            return "No such category id"

        c_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None or str:
        try:
            c_topic = next(filter(lambda x: x.id == topic_id, self.topics))
        except StopIteration:
            return "No such topic id"

        c_topic.topic = new_topic
        c_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str) -> None or str:
        try:
            c_document = next(filter(lambda x: x.id == document_id, self.documents))
        except StopIteration:
            return "No such document id"

        c_document.file_name = new_file_name

    @classmethod
    def delete_elements(cls, current_id, lst):
        try:
            c_id = next(filter(lambda x: x.id == current_id, lst))
        except StopIteration:
            return "No such id"

        lst.remove(c_id)

    def delete_category(self, category_id: int) -> None:
        Storage.delete_elements(category_id, self.categories)

    def delete_topic(self, topic_id: int) -> None:
        self.delete_elements(topic_id, self.topics)

    def delete_document(self, document_id: int) -> None:
        self.delete_elements(document_id, self.documents)

    def get_document(self, document_id: int) -> str:
        try:
            c_document = next(filter(lambda x: x.id == document_id, self.documents))
        except StopIteration:
            return "No such document id"

        return str(c_document)

    def __repr__(self) -> str:
        result = [str(doc) for doc in self.documents]

        return "\n".join(result)
