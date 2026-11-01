
document=""
undo_stack=[]
redo_stack=[]
while True:
    command=input("command (type/undo/redo/quit): ").strip().lower()
    if command=="type":
        text=input("text: ")
        undo_stack.append(document)
        document+=text
        redo_stack.clear()
        print("document:", document)
    elif command=="undo":
        if not undo_stack:
            print("nothing")
        else:
            redo_stack.append(document)
            document=undo_stack.pop()
            print("document:", document)
    elif command=="redo":
        if not redo_stack:
            print("nothing")
        else:
            undo_stack.append(document)
            document=redo_stack.pop()
            print("document:", document)
    elif command=="quit":
        break
    else:
        print("invalid command")