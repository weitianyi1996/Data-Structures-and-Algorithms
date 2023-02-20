# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count  # m, total number of buckets, each bucket will append a list includes values that need to be stored
        # store all strings in one list
        # self.elems = []
        self.hash_table = [[] for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        # print all results under the same chain(hash values) at once
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            # when print, need to print in reverse!
            self.write_chain(self.hash_table[query.ind][-1::-1])
        else:
            try:
                # if already saved, then find query.s index in list elems! for delete purpose!
                ind = self.hash_table[self._hash_func(query.s)].index(query.s)
            except ValueError:  # string not in element
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    # self.elems.append(query.s)
                    self.hash_table[self._hash_func(query.s)].append(query.s)
            else:
                # this is delete operation!
                if ind != -1:
                    self.hash_table[self._hash_func(query.s)].pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

