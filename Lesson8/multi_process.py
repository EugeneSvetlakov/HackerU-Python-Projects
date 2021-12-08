from multiprocessing import Pool
import concurrent.futures
import time

d = {
    u'а': u'a',
    u'б': u'b',
    u'в': u'v',
    u'г': u'g',
    u'д': u'd',
    u'е': u'e',
    u'ё': u'e',
    u'ж': u'zh',
    u'з': u'z',
    u'и': u'i',
    u'й': u'y',
    u'к': u'k',
    u'л': u'l',
    u'м': u'm',
    u'н': u'n',
    u'о': u'o',
    u'п': u'p',
    u'р': u'r',
    u'с': u's',
    u'т': u't',
    u'у': u'u',
    u'ф': u'f',
    u'х': u'h',
    u'ц': u'ts',
    u'ч': u'ch',
    u'ш': u'sh',
    u'щ': u'sch',
    u'ъ': u'',
    u'ы': u'y',
    u'ь': u'',
    u'э': u'e',
    u'ю': u'yu',
    u'я': u'ya'
}


def complex_function(letter):  # A
    result = letter
    for i in range(5):
        for k in d.keys():
            if k == letter:
                result = d[letter]
            elif k.upper() == letter:  # "a".uuper() -> "A" == A
                result = d[letter.lower()].upper()  # d["a"] -> "a".upper()
    return result


def work(line):
    return "".join([complex_function(a) for a in line])


def worker_single(source: list):
    res = ""
    for line in source:
        res += "\n" + work(line)
    return res


def worker_thread(source: list):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # futures = [executor.submit(work, line) for line in source]
        # return "\n".join(f.result() for f in futures)
        results = executor.map(work, source)  # [arg1,arg2,arg3] arg1 = (1,2,3)
        return "\n".join(r for r in results)


def worker_process(source: list, stones=4):
    with Pool(stones) as p:
        return "\n".join(p.map(work, source))


if __name__ == '__main__':
    # word = input("input word in russion: ")
    # r = "".join([complex_function(a) for a in word])
    # print(r)
    print("Start")
    f = open("./Lesson8/war_numered.txt", encoding="utf-8")
    source = f.read().split("\n")
    f.close()
    t = time.time()
    # res = worker_single(source)  # 66.621
    res = worker_thread(source)  # 105.952
    # res = worker_process(source)  # 22.173
    print(f"time {time.time() - t}")
    print("Done")
    f = open("./Lesson8/war_tr.txt", 'w')
    f.write(res)
    f.close()
