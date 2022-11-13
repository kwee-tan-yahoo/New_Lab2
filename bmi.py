def calculate_bmi(height, weight):
    print("\nHeight = " + str(height))
    print("Weight = "+ str(weight))
    bmi = weight/height/height
    print("BMI = " + str(bmi))
    if (bmi <18.5):
        print("Under weight")

    elif (bmi>25.0):
        print("Over weight")

    else:
        print("Normal weight")



calculate_bmi(weight=60, height=1.67)

