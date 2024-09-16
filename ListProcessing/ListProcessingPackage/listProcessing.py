# listProcessing.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

def initializeStudents():
    """
    Create a dataset of students to work with.
    @return list: The initialized list. Actually, a list of lists
    """
    data = []    # An empty list
    student = ["Smith", "Bob", "M02635916", "Information Systems"]
    data.append(student)
    student = ["Miller", "Mary", "M02635922", "Information Systems"]
    data.append(student)
    student = ["Burlew", "Cecelia", "M02635987", "BANA"]
    data.append(student)
    student = ["Cheaney", "Calbert", "M04435987", "Computer Science"]
    data.append(student)
    return data

if __name__ == "__main__":
    print(initializeStudents())