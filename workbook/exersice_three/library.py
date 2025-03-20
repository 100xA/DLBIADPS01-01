import json
import xml.etree.ElementTree as ET
import os

def load_data_from_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def parse_xml_to_list(xml_data: str) -> list[dict]:
    root = ET.fromstring(xml_data)
    books_list = []
    for book_elem in root.findall("book"):
        title = book_elem.find("title").text if book_elem.find("title") is not None else ""
        author = book_elem.find("author").text if book_elem.find("author") is not None else ""
        year_str = book_elem.find("year").text if book_elem.find("year") is not None else "0"
        try:
            year = int(year_str)
        except ValueError:
            year = 0
        books_list.append({
            "title": title,
            "author": author,
            "year": year
        })
    return books_list

def parse_json_to_list(json_data: str) -> list[dict]:
    data = json.loads(json_data)
    return data.get("library", [])

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_path = os.path.join(script_dir, "library.xml")
    json_path = os.path.join(script_dir, "library.json")
    
    xml_content_abs = load_data_from_file(xml_path)
    json_content_abs = load_data_from_file(json_path)
    
    books_from_xml = parse_xml_to_list(xml_content_abs)
    books_from_json = parse_json_to_list(json_content_abs)
    
    print("Books from XML:")
    for book in books_from_xml:
        print(f"- {book['title']} by {book['author']} ({book['year']})")

    print("\nBooks from JSON:")
    for book in books_from_json:
        print(f"- {book['title']} by {book['author']} ({book['year']})")

if __name__ == "__main__":
    main()
