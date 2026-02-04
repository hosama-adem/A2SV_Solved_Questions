class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0
        current = chars[read]
        start = read

        while read < len(chars):
            if chars[read] == current:
                read += 1
            else:
                count = read - start
                chars[write] = current
                write += 1
                if count > 1:
                    for i in str(count):
                        chars[write] = i
                        write += 1
                current = chars[read]
                start = read

                
        count = read - start
        chars[write] = current
        write += 1
        if count > 1:
            for i in str(count):
                chars[write] = i
                write += 1

        return write
