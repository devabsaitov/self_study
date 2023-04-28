class ContextManager:
    def __enter__(self):
        print("Kirish")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Chiqish")


with ContextManager():
    print("Ichida")
