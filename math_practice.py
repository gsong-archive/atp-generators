import random
import string


def map_unicode(l):
    return map(unicode, l)


def as_letter(pnum):
    return "%s)" % string.lowercase[pnum - 1]


def line1(pnum, low, high):
    n = random.randint(low, high)
    return n, map_unicode([as_letter(pnum), '', n])


def line2(symbol, low, high):
    n = random.randint(low, high)
    return n, map_unicode(['', symbol, n])


def add(pnum):
    LOW = 1
    HIGH = 500
    n1, l1 = line1(pnum, LOW, HIGH)
    n2, l2 = line2('+', LOW, HIGH)
    return l1, l2, n1 + n2


def subtract(pnum):
    LOW = 1
    HIGH = 500
    first_num = random.randint(LOW, HIGH)
    n1, l1 = line1(pnum, first_num, first_num)
    n2, l2 = line2(u'\u2212', LOW, first_num)
    return l1, l2, n1 - n2


def multiply(pnum):
    LOW = 1
    HIGH = 50
    n1, l1 = line1(pnum, LOW, HIGH)
    n2, l2 = line2(u'\u00d7', LOW, HIGH)
    return l1, l2, n1 * n2


def divide(pnum):
    LOW = 1
    HIGH = 12
    divisor = random.randint(LOW, HIGH)
    quotient = random.randint(LOW, HIGH)
    dividend = divisor * quotient
    n1, l1 = line1(pnum, dividend, dividend)
    n2, l2 = line2(u'\u00f7', divisor, divisor)
    return l1, l2, quotient


def print_answers(answers):
    numbered = []
    for i in range(len(answers)):
        w = u'%s\u00A0%s' % (as_letter(i + 1), answers[i])
        numbered.append(w.encode('utf-8'))
    print('== Answer ==')
    print('Answers:\t%s' % '  '.join(numbered))


def main():
    count = 0
    line1 = []
    line2 = []
    answers = []
    while count < 15:
        count += 1
        func = random.choice((add, subtract, multiply, divide))
        l1, l2, answer = func(count)
        line1.append(','.join(l1))
        line2.append(','.join(l2))
        answers.append(answer)
        if not count % 5:
            for l in (line1, line2):
                print(',,'.join(l).encode('utf-8'))
            print
            line1 = []
            line2 = []
    print_answers(answers)


if __name__ == '__main__':
    main()
