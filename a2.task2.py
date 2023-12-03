#TASK2
import sys

class Processor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.output_file = "out2.py"

    def process_file(self):
        with open(self.input_file, 'r') as file:
            content = file.read()
        buffer = self.linearize_content(content)
        with open(self.output_file, 'w') as file:
            file.write(buffer)
        print(f"Contents of {self.output_file}:\n")
        print(buffer)

    def linearize_content(self, content):
        buffer = []
        for char in content:
            if char != '\n':
                buffer.append(char)
        buffer.append('$')  
        return ''.join(buffer)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    processor = Processor(input_file)
    processor.process_file()
if __name__ == "__main__":
    main()
