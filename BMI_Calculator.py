height = float(input("Enter height in inches: "))
weight = float(input("Enter weight in lbs: "))

def BMI(height,weight):
    bmi = weight/(height**2) * 703
    if(bmi < 16):
        return  'Severly Underweight', bmi

    elif (bmi >= 16 and bmi < 18.5):
        return 'Underweight', bmi

    elif (bmi >=18.5 and bmi < 25):
        return 'Healthy', bmi

    elif (bmi >= 25 and bmi <30):
        return 'Overweight', bmi

    elif (bmi >= 30):
        return 'Obese', bmi

quote, bmi = BMI(height,weight)
print('Your BMI is: {} and You are: {}'.format(bmi, quote))