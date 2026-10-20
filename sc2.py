#Name:
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

height = float(input("enter height meters: "))
weight = float(input("enter weight kilograms: "))


BMI = weight / (height ** 2)
BMI = round(BMI, 2)


if BMI < 18.5:
    print("underweight")
elif BMI >= 18.5 or  BMI <= 24.9 :
    print("normal")
if BMI >= 25 or  BMI <= 29.9 :
    print("overweight")
if BMI >= 30:
    print("obese")












# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI