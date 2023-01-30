class_list = []

def Read_DB(classroom: str):
    with open(f'8Seminar_2\{classroom}', 'r', encoding='UTF-8') as file:
        global class_list
        list = file.readlines()
        for line in list:
            subject = {}
            pupils = {}
            line = line.strip().split(';')
            for i in range(1, int(len(line)-1/2), 2):
                grade = line[i+1].split(',')
                pupils[line[i]] = grade
            
            subject[f'{line[0]}'] = pupils
            class_list.append(subject)

def Lesson(subject: int, pupils: int, grade: int):

    subject_number = subject
    for k in (class_list[subject]).keys():
        subject = k

    (((class_list[subject_number])[subject])[pupils]) = (((class_list[subject_number])[subject])[pupils]).append(grade)

    return (((class_list[subject_number])[subject])[pupils])
