class Solution:
    def interpret(self, command: str) -> str:
        try:
            return command.replace("()", "o").replace("(al)","al")
        except:
            print("Invalid Input")


def main():
    command = input("Enter goal :")
    p1 = Solution()
    print(p1.interpret(command))    

main()