from base import Book


class PrintedBook(Book):
    def __init__(self, title: str, author: str, year: int, pages: int, price: float,
                 binding: str, circulation: int):
        super().__init__(title, author, year, pages, price)
        self.binding = binding
        self.circulation = circulation

    def get_shipping_weight(self) -> float:
        return self.pages * 0.01

    def __str__(self):
        return f"[Печатная] {self.title} - {self.author} ({self.year}) | {self.pages} стр. | {self.price:.2f} руб. | Переплёт: {self.binding} | Тираж: {self.circulation}"


class Ebook(Book):
    def __init__(self, title: str, author: str, year: int, pages: int, price: float,
                 file_format: str, file_size_mb: float):
        super().__init__(title, author, year, pages, price)
        self.file_format = file_format
        self.file_size_mb = file_size_mb

    def get_download_time(self, speed_mbps: float = 10) -> float:
        return (self.file_size_mb * 8) / speed_mbps

    def __str__(self):
        return f"[Электронная] {self.title} - {self.author} ({self.year}) | {self.pages} стр. | {self.price:.2f} руб. | Формат: {self.file_format} | {self.file_size_mb} МБ"


class AudioBook(Book):
    def __init__(self, title: str, author: str, year: int, pages: int, price: float,
                 duration_hours: float, narrator: str):
        super().__init__(title, author, year, pages, price)
        self.duration_hours = duration_hours
        self.narrator = narrator

    def get_remaining_time(self, listened_hours: float = 0) -> float:
        return max(0, self.duration_hours - listened_hours)

    def __str__(self):
        return f"[Аудио] {self.title} - {self.author} ({self.year}) | {self.price:.2f} руб. | Читает: {self.narrator} | {self.duration_hours} ч."