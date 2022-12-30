from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_ON_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / PhotoAlbum.MAX_PHOTOS_ON_PAGE))

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            page_lenght = len(self.photos[page])
            if page_lenght < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {page_lenght}"
        
        return "No more free slots"

    def display(self):
        output = []

        for p in self.photos:
            output.append("-" * 11)
            output.append(("[] " * len(p)).rstrip())
        
        output.append("-" * 11)
        
        return "\n".join(output)
