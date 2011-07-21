def ispalindrome(word):
    return word == word[::-1]
def main():
    largest = 0
    for i in range(100,999):
        for j in range(100,999):
            curr = i * j
            if ispalindrome(str(curr)) and curr > largest:
                largest = curr
    print largest
main()
            
