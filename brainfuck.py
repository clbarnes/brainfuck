from collections import deque


class Brainfuck:
    def __init__(self, s):
        self.cursor = 0
        self.pointer = 0
        self.buffer = deque([0])

        self.s = s

        self.fns = {
            '<': self.langle,
            '>': self.rangle,
            '+': self.plus,
            '-': self.minus,
            ',': self.comma,
            '.': self.stop,
            '[': self.lbrack,
            ']': self.rbrack
        }

        self.execute()

    def langle(self):
        if self.pointer > 0:
            self.pointer -= 1
        else:
            self.buffer.appendleft(0)
        self.cursor += 1
        return ''

    def rangle(self):
        self.pointer += 1
        if self.pointer >= len(self.buffer):
            self.buffer.append(0)
        self.cursor += 1
        return ''

    def plus(self):
        self.buffer[self.pointer] = self.buffer[self.pointer] + 1 if self.buffer[self.pointer] < 127 else 0
        self.cursor += 1
        return ''

    def minus(self):
        self.buffer[self.pointer] = self.buffer[self.pointer] - 1 if self.buffer[self.pointer] > 0 else 127
        self.cursor += 1
        return ''

    def comma(self):
        val = ord(input('Input: ')[0])
        val = val if val <= 127 else 0
        self.buffer[self.pointer] = val
        self.cursor += 1
        return ''

    def stop(self):
        val = chr(self.buffer[self.pointer])
        print(val, end='')
        self.cursor += 1
        return val

    def lbrack(self):
        self.cursor = self.s.find(']', self.cursor)
        self.cursor += 1
        return ''

    def rbrack(self):
        self.cursor = self.s.rfind('[', 0, self.cursor)
        self.cursor += 1  # maybe?
        return ''

    def execute(self):
        output = ''
        while self.cursor < len(self.s):
            output += self.fns[s[self.cursor]]()
        print('')


if __name__ == '__main__':
    s = ''
    output = 'Hello world!'
    for c in output:
        s += '+'*ord(c) + '.>'
    
    bf = Brainfuck(s)

