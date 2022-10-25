import hashlib

key = "f092cf8544eb4cada6dd9cf84d8439da"


def make_md5(data):
    md5 = hashlib.md5()
    md5.update(data.encode("utf8"))
    return md5.hexdigest()


def make_random_sorted(n,seed):
    l = [[make_md5(key+"({}/{})".format(i,n)+seed),i] for i in range(n)]
    l.sort()
    return [item[1] for item in l]


def total_random_sorted(n,seeds):
    l2 = [make_random_sorted(n,seed) for seed in seeds]
    totals = [[0 for j in range(n)] for i in range(n)]
    for sort in l2:
        for i in range(n):
            totals[i][sort[i]] += 1
    return totals


if __name__ == "__main__":
    test_num = 10
    print(total_random_sorted(test_num,["{}".format(i) for i in range(100000)]))
    for i in range(10):
        print(make_random_sorted(test_num,"{}".format(i)))