#Kaun Banega Crorepati (small project)
questions = ["1.Accroding to the Hindu religion, What's the meaning of the name 'RAMAN'","2.How many colors are their in the RAINBOW","3.Total Number of states in country 'INDIA'","4.What is tha capital of INDIA","5.Goitre is a disease caused due to the deficiency of?","6.What is the largest island in the world is","7.Which state is known as Orchid Paradise in India?","8.Which is the most widely spoken language in the world?","9.Who invented Penicillin","10.Which is an essential element of photosynthesis?","11.which State is the first state in India to achieve 100 % rural electrification in 'INDIA'"]

options = ["a) Adorable Person\t b) Charming Person\t\n c) Kind hearted Person\t d) Bad Person","a) 3\t b) 6\t\n c) 8\t d) 7","a) 21\t b) 26\t\n c) 28\t d) 29","a) Hydrabad\t b) Delhi\t\n c) Bengaluru\t d) Lucknow","a) Carbs\t b) Minerals\t\n c) Protein\t d) Iodine","a) Greenland\t b) Borneo\t\n c) Madagascar\t d) New Guinea","a) Bihar\t b) Arunachal Pradesh\t\n c) Karnataka\t d) Kerala","a) English\t b) French\t\n c) Mandarin(Chinese)\t d) Japanese","a) Peter Sine\t b) Alex Anem\t\n c) Jhon ded\t d) Alexander Fleming","a) Scandium (Sc)\t b) Potassium (K)\t\n c) Carbon dioxide (CO2)\t d) Magnesium (Mg)","a) Haryana\t b) Rajasthan\t\n c) Gujarat\t d) Kerala"]

answers = ["c", "d", "d", "b","d","a","b","c","d","c","a"]
# print(options[0])
amt = 0

print("* * * * * * * * * KAUN BANEGA CROREPATI * * * * * * * * *\n")
for i in range(len(questions)):
   print(questions[i],"\n")
   print(options[i],"\n")  
   x = input("Enter the option: ")

   if (x!=answers[i]):
    print("Wrong Answer")
    print("Thanks for playing ,You Won ",amt," Ruppess")
    print("The amount you won will be credited in your given bank account in 2-3 business days")
    exit("Bye Bye")
   else:
      if(amt>=10000):
       amt  *= 2
      elif(i==0): 
       amt += 10000
      print("Congrats ,Correct Answer")
      print("You won",amt,"ruppess\n")

   if(amt==80000):
     print("* * * * * * * Second Round * * * * * * *\n")
   elif(amt==640000):
     print("* * * * * * * Third Round * * * * * * *\n")
   elif(amt==5120000):
     print("* * * * * * * Final Round * * * * * * *\n")
