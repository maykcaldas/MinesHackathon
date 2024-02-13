from dotenv import load_dotenv
load_dotenv()

from ai_uni.University import University
from ai_uni.Faculty.Professor import Professor

questions = {
    1: "What is the difference between interpreted and compiled programming languages?",
    2: '''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
'''
}


TASK = "What is this student's grade? Assign a grade following the question's rubric. And provide feedback where the student need to improve."
ID=1

prompt1 = f'''
{TASK}
Question ID: {ID}
Question: {questions[ID]}

Student's answer:  "The main difference between interpreted and compiled programming languages is that interpreted languages are faster because they are translated directly into machine code while the program runs. Compiled languages, on the other hand, are a bit slower because they need to be written into an intermediate code before they can be executed by the computer. This means you gotta wait for the whole compilation process before you can even run your program. So, basically, interpreted is like on-the-fly and super quick, while compiled is more like slow and steady."
'''

prompt2 = f'''
{TASK}
Question ID: {ID}
Question: {questions[ID]}

Student's answer: "Interpreted and compiled programming languages are distinct in their approach to processing and executing code. Compiled languages, such as Java and C++, are converted into machine code through a process known as compilation. This process occurs before the program is run, allowing compiled languages to often run faster because the code is already translated into a form that the computer's processor can directly execute.

On the other hand, interpreted languages, like Python and JavaScript, are not converted into machine code beforehand. Instead, these languages use an interpreter, a program that reads and executes the code line by line at runtime. This can result in slower execution speeds compared to compiled languages, as the interpretation process takes time. However, interpreted languages are generally considered more flexible and easier to debug, since they allow for changes to be made to the code while it is running.

It's important to note that some languages can be both interpreted and compiled. For example, Python code can be compiled into bytecode, which is then interpreted by the Python Virtual Machine. This hybrid approach aims to balance the execution speed of compiled languages with the flexibility of interpreted languages.

In summary, the key difference lies in when and how the source code is converted into a form that the computer can understand and execute: compiled languages undergo this process before runtime, leading to faster execution but less flexibility, whereas interpreted languages undergo this process during runtime, resulting in slower execution but increased flexibility.
'''

prompt3 = f'''
{TASK}
Question ID: {ID}
Question: {questions[ID]}

Student's answer: "Basically, the main difference between interpreted and compiled programming languages is how they convert the code we write into a language that the computer can understand.

With a compiled language, before you can run your program, you have to use a compiler to translate your entire code into machine language, which is the binary code that computers understand. This is done all at once and creates an executable file. So, when you want to run your program, the computer just runs this already compiled file. Examples of compiled languages are C and C++.

On the other hand, interpreted languages don't compile into machine language in advance. Instead, they are translated on-the-fly, line by line, while the program is running. This is done by an interpreter, which reads the code and executes it directly. So, every time you run an interpreted language program, it's being translated in real-time. Python and JavaScript are examples of interpreted languages.

The main takeaway is that compiled languages usually run faster since they are already translated into machine code when you run them. But interpreted languages are more flexible and easier to debug because they're being translated as they run."
'''

prompt4 = f'''
{TASK}
Question ID: {ID}
Question: {questions[ID]}

Student's answer: "Essentially, the primary distinction between interpreted and compiled programming languages lies in their method of converting the code we write into a format that the computer can interpret.

With a compiled language, to execute your program, a compiler is not always necessary to transform your code into machine language, the binary code that computers comprehend. This process is done in stages and generates a source file. Therefore, when you wish to execute your program, the computer may need to compile this file each time. Examples of compiled languages include Java and Python.

Conversely, interpreted languages are compiled into machine language beforehand. They are translated as a whole, rather than on-the-fly, and not line by line, while the program is running. This task is managed by a compiler, which reads the code and compiles it directly. Thus, each time you run a program written in an interpreted language, it has been pre-translated. JavaScript and C are instances of interpreted languages.

The key point is that interpreted languages tend to execute quicker since they are pre-compiled into machine code before execution. However, compiled languages offer greater flexibility and are simpler to debug because they compile the code as it runs."
'''

# ID=2
prompt5 = f'''
{TASK}
Question ID: {ID}
Question: {questions[ID]}

Student's answer:

To solve the following problem, I will use a brute force approach. I will iterate through the list of numbers and for each number, I will check if there is another number in the list that, when added to the current number, equals the target. If I find such a pair, I will return the indices of the two numbers.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, numi in enumerate(nums):
            for j, numj in enumerate(nums[i+1:], i+1):
                if numi+numj == target: return [i,j]
'''

prompt6 = f'''
{TASK}
Question ID: {ID}
Question: {questions[ID]}

Student's answer:

To solve the following problem, I will use a brute force approach. I will iterate through the list of numbers and for each number, I will check if there is another number in the list that, when added to the current number, equals the target. If I find such a pair, I will return the indices of the two numbers.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, numi in enumerate(nums):
            for j, numj in enumerate(nums, i):
                if numi+numj == target: return [i,j]
'''

uni = University()
prof = Professor()

prof.run(prompt3)
#uni.run(prompt1)