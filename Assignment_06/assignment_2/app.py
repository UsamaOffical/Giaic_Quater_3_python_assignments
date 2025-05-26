class Counter:
    count = 0  # Class variable to keep count of objects

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Example usage
c1 = Counter()
c2 = Counter()
Counter.display_count()
