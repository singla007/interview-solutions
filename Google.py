# Define a class `SparseVector` to represent sparse 1-d vectors.
# 1. It should take a sequence of integers for initialization.
# 2. The class should provide an instance method to compute the dot product given another instance of `SparseVector` and return the result.
# 3. Optimize the dot product method for very long, very sparse vectors (think 1% values out of millions are non-zero).
# Sparse vector:
# A vector is called sparse if a large proportion of the values are 0s.
# Dot product:
# Given two vectors X = [x1, x2, …, xN] and Y = [y1, y2, y3, …, yM], the dot product of X and Y is
# 1. Not defined if N != M
# 2. Defined as x1*y1 + x2*y2 + … + xN*yM otherwise.
# You are not allowed to use Numpy or any other scientific computation library.


import threading


class SparseVector:
    def __init__(self,vector_list):
        self.vector_dict = {i:val for i,val in enumerate(vector_list) if val!=0}
        self.vector_len = len(vector_list)
        self.thread_result = 0
        
    def dot_product(self, vector2):
        
        if self.vector_len!=vector2.vector_len:
            return None
        product_result = 0
        thread_list = []
        for i, val in self.vector_dict.items():
            # product_result += val*vector2.vector_dict.get(i,0)
            thread = threading.Thread(target=self.thread_multiplication, args=(val, vector2.vector_dict.get(i,0)))
            thread_list.append(thread)
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
            
        return self.thread_result
    
    def thread_multiplication(self,ele1,ele2):
        self.thread_result+= ele1*ele2
        
vector1 = SparseVector([1,0,0,0,3]) #N , Z O(z)
vector2 = SparseVector([5,0,0,0,1])
print(vector1.dot_product(vector2))
