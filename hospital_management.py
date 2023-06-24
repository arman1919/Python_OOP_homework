from abc import ABC, abstractmethod



class patient:
    def __init__(self,name, age) -> None:
        self.name = name
        self.age = age
        self.medical_history = []
    
    def __str__(self) -> str:
        history = ''
        for i in self.medical_history:
            history += i +"\n"
        
        return history




class doctor:
    def __init__(self,name,contact_information) -> None:
        self.name = name
        self.contact_information = contact_information


    def add_medical_operation(self,medical_operation,medical_staff):
        if medical_operation == "group_therapy":
            return group_therapy("group_therapy",medical_staff)
        
        elif medical_operation == "x_ray":

            return x_ray(medical_operation,medical_staff)

        else:
            raise TypeError

    def add_patient_to_medical_operation(self,patient,medical_operation):
        
        medical_operation.add_patients(patient)
         



class medical_staff:
    def __init__(self,name,position) -> None:
        self.name = name
        self.position = position

    def start_treatment(self,medical_operation):
        medical_operation.healing()


class medical_operation(ABC):
    def __init__(self,name,medical_staff) -> None:
        self.name = name
        self.medical_staff = medical_staff
        self.patients_list  = []
        
    def add_patients(self,patient):
        self.patients_list.append(patient)


    @abstractmethod
    def healing(self):
        pass


class group_therapy(medical_operation):
    def __init__(self, name, medical_staff) -> None:
        super().__init__(name, medical_staff)
    
    def healing(self):
        for i in self.patients_list:
            i.medical_history.append("Group therapy")
            print (f"Medic {self.medical_staff.name} treated {i.name}")
        self.patients_list.clear()
    


class x_ray(medical_operation):
    def __init__(self, name, medical_staff) -> None:
        super().__init__(name, medical_staff)
    
    def healing(self):
        patient =  self.patients_list[0]

        print (f"Medic {self.medical_staff.name} treated {patient.name}")
        patient.medical_history.append("X-Ray")
        self.patients_list.pop(0)
        
    

Alex = patient("Alex",25)
Stiv = patient("Stive",30)
Jim =  patient("Jim",40)

Doc = doctor("Arcji","Archi@mail.ru")

medic1 = medical_staff("Mary","psychiatrist")
medic2 = medical_staff("Andro","x-ray specialist")

Group_therapy = Doc.add_medical_operation("group_therapy",medic1)
X_ray = Doc.add_medical_operation("x_ray",medic2)



Doc.add_patient_to_medical_operation(Alex,Group_therapy)
Doc.add_patient_to_medical_operation(Stiv,Group_therapy)
Doc.add_patient_to_medical_operation(Jim,X_ray)
Doc.add_patient_to_medical_operation(Alex,X_ray)


medic1.start_treatment(Group_therapy)
medic2.start_treatment(X_ray)
medic2.start_treatment(X_ray)
print()

#medical_history
print(Alex)
print()
print(Stiv)
print()
print(Jim)