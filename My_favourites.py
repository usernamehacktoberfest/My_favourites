# here is the answer of every question

n: str = input("Enter your Name.")
country = input("Enter your Country.")
link= input("Can we connect on linkedin?")
lang = input("Your favourite Programming language?")
web = input("Your favourite website?")
app = input("Your favourite app?")

print("Hii, My Name is {}".format(n))
print("I am from {}".format(country))
print("Yes my link is {}".format(link))
print("My favourite programming language is {}".format(lang))
print("My favourite website is {}".format(web))
print("My favourite application is {}".format(app))

if __name__ == "main":
    n = "Umakshi"
    country = "India"
    link = "www.linkedin.com/in/umakshi-sharma-163302206"
    web = "CodeStudio"
    app = "PyCharm"

    # Python program to find nth magic number
 
# Function to find nth magic number
def nthMagicNo(n):
 
    pow = 1
    answer = 0
 
    # Go through every bit of n
    while (n):
 
        pow = pow*5
 
        # If last bit of n is set
        if (n & 1):
            answer += pow
 
        # proceed to next bit
        n >>= 1 # or n = n/2
     
    return answer
 
 
# Driver program to test above function
n = 5
print("nth magic number is", nthMagicNo(n))

Input: n = 2
Output: 25

Input: n = 5
Output: 130 
