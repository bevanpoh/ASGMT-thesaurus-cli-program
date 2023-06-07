# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================

import random

# An array which maintains a sorted order of its items
# Used by SortedDict, Synonyms
class SortedArray(list):
    def __init__(self, items=None):
        super().__init__(items or [])

        if len(self) > 0:
            self.sort()

    # =============================================================== #
    # Properties
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #
    def __contains__(self, item):
        position = self.find(item)

        if position == len(self):
            return False

        return self[position] == item

    # =============================================================== #
    # Methods
    # =============================================================== #
    def insert(self, item):
        position = self.find(item)

        super().insert(position, item)

    # binary search self to return position of match or next biggest item
    def find(self, toFind):
        toSearch = self

        lowerBound = 0
        upperBound = len(toSearch) - 1

        while lowerBound <= upperBound:
            guess = lowerBound + (upperBound - lowerBound) // 2

            # early exit to prevent unecessary guesses
            if toFind == toSearch[guess]:
                return guess

            # +-1 since we eliminated equality from the earlier return
            if toFind < toSearch[guess]:
                upperBound = guess - 1
            else:
                lowerBound = guess + 1

        return lowerBound

    # knuth shuffle algorithm
    def shuffle(self, inplace=True):
        if not inplace:
            # copy items
            toShuffle = self[:]
        else:
            toShuffle = self

        for i in range(1, len(toShuffle)):
            r = random.randint(0, i)

            # randomly swap an item with one of the items before it
            if r != i:
                toShuffle[i], toShuffle[r] = toShuffle[r], toShuffle[i]

        return None if inplace else toShuffle

    # quicksort algorithm
    def sort(self, inplace=True):
        if not inplace:
            # copy items
            arr = self[:]
        else:
            arr = self

        # already sorted array
        if len(arr) < 2:
            return None if inplace else arr

        # explicit stack to store (left, right) indexes
        stack = []
        stack.append((0, len(arr) - 1))

        while len(stack) > 0:
            left, right = stack.pop()

            pivot_position = SortedArray.__qsort_partition(arr, left, right)

            if pivot_position > left: # at least two items swapped to lower
                stack.append((left, pivot_position))
            if right > pivot_position + 1: # at least two items swapped to higher
                stack.append((pivot_position + 1, right))

    ## hoare's parition algorithm
    def __qsort_partition(arr, left, right):
        pivot = arr[(left + right) // 2]
        i = left - 1
        j = right + 1

        while True:
            # while True: increment/decrement to simulate do {} while
            # otherwise checks will be made before increment/decrement and
            # risk of infinite loop when both pointers are on equal elements
            while True:
                i += 1

                if i >= right or arr[i] >= pivot:
                    break

            while True:
                j -= 1

                if j <= left or arr[j] <= pivot:
                    break

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                return j

