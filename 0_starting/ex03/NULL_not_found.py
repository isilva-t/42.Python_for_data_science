def NULL_not_found(object: any) -> int:

    match object:
        case None:
            print(f"Nothing: {object} {type(object)}")
            return 0
        case float() if object != object:
            print(f"Cheese: {object} {type(object)}")
            return 0
        case bool() if object is False: # bool is subclass of int
            print(f"Fake: {object} {type(object)}")
            return 0
        case int() if object == 0:
            print(f"Zero: {object} {type(object)}")
            return 0
        case str() if object == "":
            print(f"Empty: {object} {type(object)}")
            return 0

    print("Type not Found")
    return 1
