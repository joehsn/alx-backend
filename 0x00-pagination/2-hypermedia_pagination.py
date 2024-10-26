#!/usr/bin/env python3
"""
2. Hypermedia pagination task's module.
"""

import csv
from math import ceil
from typing import List, Tuple, TypedDict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    total_size = page * page_size
    return total_size - page_size, total_size


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    Page_type = TypedDict('Page_type', {
        'page_size': int,
        'page': int,
        'data': List[List],
        'next_page': int | None,
        'prev_page': int | None,
        'total_pages': int,
    })

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Page_type:
        """
        Retrieves a page of data in dictionary.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size
        total_pages: int = ceil(len(self.dataset()) / page_size)
        next_page = None if page + 1 > total_pages else page + 1
        prev_page = None if page - 1 < 1 else page - 1
        data = self.get_page(page, page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
