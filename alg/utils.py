from abc import ABC, abstractmethod


def benchmark(func):
    import time

    def wrapper(self, *args):
        time_start = time.time()
        result = func(self, *args)
        time_finish = time.time()
        timing = "%f seconds" % (time_finish - time_start)
        return {'result': result, 'timing': timing}

    return wrapper


class AlgBase(ABC):

    @abstractmethod
    def realize(self):
        pass


class BubbleAlgorithm(AlgBase):

    def __init__(self):
        pass

    @benchmark
    def realize(self, nlist):
        for passnum in range(len(nlist)-1, 0, -1):
            for i in range(passnum):
                if nlist[i] > nlist[i+1]:
                    temp = nlist[i]
                    nlist[i] = nlist[i+1]
                    nlist[i+1] = temp
        return nlist


class InsertionAlgorithm(AlgBase):

    @benchmark
    def realize(self, nlist):

        for i in range(1, len(nlist)):

            key = nlist[i]

            j = i - 1
            while j >= 0 and key < nlist[j]:
                nlist[j + 1] = nlist[j]
                j -= 1
            nlist[j + 1] = key
        return nlist


class MergeAlgorithm(AlgBase):

    @benchmark
    def realize(self, nlist):
        new_mas = MergeAlgorithm.merge_sort(nlist)
        return new_mas

    @staticmethod
    def merge_sort(nums):

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left_list = MergeAlgorithm.merge_sort(nums[:mid])
        right_list = MergeAlgorithm.merge_sort(nums[mid:])

        return MergeAlgorithm.merge(left_list, right_list)

    @staticmethod
    def merge(left_list, right_list):
        sorted_list = []
        left_list_index = right_list_index = 0

        left_list_length, right_list_length = len(left_list), len(right_list)

        for _ in range(left_list_length + right_list_length):
            if left_list_index < left_list_length and right_list_index < right_list_length:

                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1

                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1

            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

        return sorted_list


simple_dict = {'Bubble': BubbleAlgorithm,
               'Insertion': InsertionAlgorithm,
               'Merge': MergeAlgorithm,
               }


def alg_parser(alg):
    return simple_dict[alg]()


