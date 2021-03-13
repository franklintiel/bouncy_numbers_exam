from models import BouncyNumberFinder

if __name__ == '__main__':
    # Example with percentage equal to 0
    instance = BouncyNumberFinder(percentage_required=0)
    print(instance.message)

    # Example with percentage equal to 5
    instance = BouncyNumberFinder(percentage_required=5)
    print(instance.message)

    # Example with percentage equal to 50
    instance = BouncyNumberFinder(percentage_required=50)
    print(instance.message)

    # Example with percentage equal to 90
    instance = BouncyNumberFinder(percentage_required=90)
    print(instance.message)

    # Example with percentage equal to 99
    instance = BouncyNumberFinder(percentage_required=99)
    print(instance.message)
