class Patient:
    def __init__(self, patient_id, name, age, disease, fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.fee = fee
    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.fee)
    def total_bill(self):
        print("Total Bill:", self.fee)
p = Patient(1, "Vaishnavi", 20, "Fever", 500)
p.display()
p.total_bill()