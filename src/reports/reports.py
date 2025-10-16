from abc import ABC, abstractmethod
from tabulate import tabulate


class BaseReport(ABC):
    @abstractmethod
    def generate(self, data):
        pass

    @abstractmethod
    def display(self, result):
        pass


class AverageRatingReport:
    def generate(self, data: list[dict[str, str]]) -> list[tuple]:
        brand_ratings = {}
        for row in data:
            brand = row.get("brand")
            rating = row.get("rating")

            if brand not in brand_ratings:
                brand_ratings[brand] = []
            brand_ratings[brand].append(float(rating))

        result = []
        for brand, ratings in brand_ratings.items():
            avg_rating = sum(ratings) / len(ratings)
            result.append((brand, round(avg_rating, 2)))

        result.sort(key=lambda x: x[1], reverse=True)

        return result

    def display(self, result: list[tuple]) -> None:
        if result:
            headers = ["", "brand", "rating"]
            table_data = [
                [index, *values] for index, values in enumerate(result, 1)
            ]

            print(
                tabulate(
                    table_data,
                    headers=headers,
                    tablefmt="grid",
                    stralign="left",
                )
            )
        else:
            print("Empty result")
