#TASK1
import sys
import re

class Preprocessor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.output_file = "out1.py"

    def dellet_comments(self, content):
        content = re.sub(r'#.*', '', content)  
        content = re.sub(r'""".*?"""', '', content, flags=re.DOTALL)
        return content

    def dellet_blank_lines(self, content):
        lines = content.split('\n')
        nonemptylines = [line for line in lines if line.strip()]
        return '\n'.join(nonemptylines)
    
    def dellet_imports_annotations(self, content):
        lines = content.split('\n')
        updated_lines = [line for line in lines if not line.startswith("import ") and not line.startswith("@")]
        return '\n'.join(updated_lines)



    def dellet_spaces_tabs(self, content):
        content = re.sub(r'\s+', ' ', content)  
        content = content.replace('\t', ' ')  
        return content.strip()


    def _file(self):
        with open(self.input_file, 'r') as file:
            content = file.read()

        content = self.dellet_blank_lines(content)
        content = self.dellet_comments(content)
        content = self.dellet_spaces_tabs(content)
        content = self.dellet_imports_annotations(content)
        with open(self.output_file, 'w') as file:
            file.write(content)
        print(f"Contents of {self.output_file}:\n")
        print(content)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    preprocessor = Preprocessor(input_file)
    preprocessor.preprocess_file()
if __name__ == "__main__":
    main()
