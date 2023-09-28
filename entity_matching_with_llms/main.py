from langfuse import Langfuse


def main():
    # Create a LangFuse object
    lf = Langfuse("str", "str")

    print(f"{lf}")


main()
