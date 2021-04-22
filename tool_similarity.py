#!/usr/bin/env python

import numpy as np


class Similarity:
    """
        self.molecule
        self.denominator
        These two parameters are for the convenience of calculating similarity
    """
    def __init__(self):
        self.dis = 0
        self.molecule = 0                       # 分子
        self.denominator = float('inf')         # 分母
        self.precision = 4

    '''
        If you want to get similarity, you can finally call this function.
    '''
    def calculate(self):
        return round(self.molecule/self.denominator, self.precision)

    '''
        The two strings are equal in length.
        Hamming distance refers to number of characters that need to be replaced to transform one string into another.
        Simply put, compare whether the characters in each position of two strings are equal.
        eg. A = "abc"  B = "bbc"
    '''
    def hamming_distance(self, A, B):
        if len(A) != len(B):
            return -1
        n = len(A)
        self.dis = 0
        for i in range(n):
            if A[i] != B[i]:
                self.dis += 1
        self.molecule = n - self.dis
        self.denominator = n
        return self.dis

    '''
        The editing distance is the minimum number of operation steps required to replace, add and delete 
        a character string into another character string. Also called Levenshtien distance.
        eg. A = "facebook"  B = "bread"
    '''
    def editing_distance(self, A, B):
        m = len(A)
        n = len(B)
        LD = [[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    LD[i][j] = 0
                elif i != 0 and j == 0:
                    LD[i][j] = i
                elif i == 0 and j != 0:
                    LD[i][j] = j
                else:
                    LDi = LD[i - 1][j] + 1
                    LDj = LD[i][j - 1] + 1
                    LDS = LD[i - 1][j - 1] if A[i] == B[j] else LD[i - 1][j - 1] + 1
                    LD[i][j] = min(LDi, LDj, LDS)
        self.dis = LD[m - 1][n - 1]
        self.molecule = m + n - self.dis
        self.denominator = m + n
        return self.dis

    '''
        Cosine distance, also known as cosine similarity, uses the cosine of the angle between two vectors 
        in vector space as a measure of the difference between two individuals.
        eg. A=[2,2,1,0], B=[1,0,1,1]        value range [-1,1]
    '''
    def cosine_distance(self, vec1, vec2, adjusted=True):
        # if adjusted:
        #     n = len(vec1)
        #     for i in range(n):
        #         mid = (vec1[i]+vec2[i])/2
        #         vec1[i] -= mid
        #         vec2[i] -= mid
        self.molecule = np.dot(vec1, vec2)
        self.denominator = np.linalg.norm(vec1)*np.linalg.norm(vec2)
        self.dis = 1 - self.calculate()
        return self.dis

    '''
        Euclidean distance is the "ordinary" (straight line) distance between two points in Euclidean space.
    '''
    def euclidean_distance(self, vec1, vec2):
        self.dis = np.linalg.norm(vec1 - vec2)
        self.molecule = self.dis
        self.denominator = 1
        return self.dis

    '''
        The ratio of the number of intersection elements of two sets A and B in the union of A and B is called 
        Jaccard coefficient of these two sets, which is represented by the symbol J(A,B). 
        Jaccard similarity coefficient is an index to measure the similarity between two sets.
    '''
    def jaccard_distance(self, x, y):
        # self.molecule = np.double(np.bitwise_and((x != y), np.bitwise_or(x != 0, y != 0)).sum())
        # self.denominator = np.double(np.bitwise_or(x != 0, y != 0).sum())
        self.molecule = len(x & y)
        self.denominator = len(x | y)
        # print('*', self.molecule)
        # print('*', self.denominator)
        self.dis = 1 - self.calculate()
        return self.dis
