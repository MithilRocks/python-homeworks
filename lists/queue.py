def enqueue(l1, data):
    l1.append(data)

def dequeue(l1):
    value = l1[0]
    l1.remove(value)
    return value

def isempty(l1):
    return l1 == []

def isfull(l1):
    return len(l1) == 10

def peep(l1):
    return l1[-1]

def menu():
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peep")
    print("4. Display")
    print("5. Exit")
    menu_item = eval(input("Enter your option: "))
    return menu_item

def simulate_queue():
    l1 = []
    while True:
        choice = menu()

        if choice == 1:
            data = eval(input("Enter your data to enqueue: "))
            enqueue(l1, data)
        elif choice == 2:
            if not isempty(l1):
                data = dequeue(l1)
                print("{} dequeued".format(data))
            else:
                print("Queue is empty. Enqueue data to use this.")

        elif choice == 3:
            if not isempty(l1):
                data = peep(l1)
                print("Top most data in queue is {}".format(data))
            else:
                print("Queue is empty.")
        elif choice == 4:
            print("The entire queue is: {}".format(l1))
        else:
            return

if __name__ == "__main__":
    simulate_queue()