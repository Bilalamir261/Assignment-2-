#TASK 3
import sys

class LexicalAnalyzer:
    def __init__(self, input_file):
        self.input_file = input_file
    
    def check_lexemes(self):
        with open(self.input_file, 'r') as file:
            content = file.read()
        lexemes = self.extract_lexemes(content)
        print("Lexemes:")
        for lexeme in lexemes:
            print(f"Lexeme: {lexeme}")

    def extract_lexemes(self, content):
        lexemes = []
        current_lexeme = ""
        for char in content:
            if char.isalnum() or char == '_':
                current_lexeme += char
            else:
                if current_lexeme:
                    lexemes.append(current_lexeme)
                    current_lexeme = ""

                if char.isspace():
                    continue
                else:
                    lexemes.append(char)

        return lexemes

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    lexical_analyzer = LexicalAnalyzer(input_file)
    lexical_analyzer.analyze_lexemes()
if __name__ == "__main__":
    main()
