import math


def __gen_st__(arr, st, i, s, e, hook):
    if s == e:
        st[i] = arr[s]
    else:
        mid = math.floor((s + e) / 2)
        st[i] = hook(
            __gen_st__(arr, st, 2 * i + 1, s, mid, hook),
            __gen_st__(arr, st, 2 * i + 2, mid + 1, e, hook))

    return st[i]


class stree(object):
    def __init__(self, arr, hook=min, default=2**31):
        """Segment tree module

        arr :       array to convert into segment tree
        hook :      the hook function @ each intermediate node,
                    you can keep this as min for min segment tree
        default :   default to return in case of error
        """
        # save the array for book keeping
        self.arr = arr
        # and save the length of the array
        self.n = len(arr)
        # and the hook
        self.hook = hook
        # and set default
        self.default = default
        # initialize segment-tree with None values
        self.segtree = [self.default] * (
            2 * (2 ** math.ceil(math.log2(self.n))) - 1)
        # and generate the tree
        __gen_st__(arr, self.segtree, 0, 0, self.n - 1, self.hook)

    def __query__(self, s, e, qs, qe, i):
        if qs <= s and qe >= e:
            return self.segtree[i]

        if e < qs or s > qe:
            return self.default

        # calc mid
        mid = math.floor((s + e) / 2)

        return self.hook(
            self.__query__(s, mid, qs, qe, 2 * i + 1),
            self.__query__(mid + 1, e, qs, qe, 2 * i + 2))

    def query(self, start, end):
        if start > end or start < 0 or end > self.n - 1:
            return self.default
        else:
            return self.__query__(0, self.n - 1, start, end, 0)

