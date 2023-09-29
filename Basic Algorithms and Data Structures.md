# <u>Basic Algorithms and Data Structures</u>

## Binary Search (Search Array)

Binary search is an efficient way of searching for elements within a sorted array. Typically we are given an array, and an element called the `target` to search for.

At its core, binary search divides the array in the middle, called `mid` and compares the value at `mid` to the `target` value. If the `mid` value is lower than the `target`, it eliminates the left half of the array and searches on the right of `mid`. If `mid` is higher than the `target`, we search to the left. We either find the `target` or determine that the `target` doesn't exist in the array.

In interviews and algorithmic problems, there are two common variations of binary search problems:

1. **Search Array** - a sorted array, and a `target` is given and the task is to determine if the target is found in the array.
2. **Search Range** - a range of numbers is given without a specific `target`.

### Mechanics of Binary Search

Now that we know the general idea behind binary search, we can determine how it would work logistically. The `target` value is given as the input but we need to calculate `mid`. `mid` is *initially* calculated by adding the **left-most** index to the **right-most** index and then dividing the result by 22. This allows us to have two equal sections of the array (recall this is exactly what we did with merge sort, except in this case we are not allocating any new space). In the case of binary search, we will have the following:

1. `L` - the left-most index of the current subarray.
2. `R` - the right-most index of the current array.
3. `mid` - `L + R / 2`, the index at which the current sub-array divides itself into two equal halves.

> `L` and `R` are sometimes referred to as `low` and `high`. It doesn't really matter which one you choose as long as they are understood by the interviewer.

The idea now is that we will keep searching for the `target` until we either find the `target`, or our `L` pointer crosses the `R` pointer, in which case the `target` doesn't exist.

### 1. Target exists in the array

Let's take the above concept and apply it to an example. Take the array `arr = [1,2,3,4,5,6,7,8]`, and 55 as our `target`.

We know that our `L` will start at the 0th index and `R` will start at 7th index, at `arr.length - 1`. Calculate the `mid` by (7+0) / 2=3(7+0) / 2=3. Now we can compare the value at index 33 to our target element.

44 is less than 55, indicating that we need to look for a larger number, and since the array is sorted, the larger numbers reside on the right. Therefore, we need to move our `L` to `mid + 1`, which determines our lower boundry. The `R` pointer stays where it is.

On the next iteration, calculating `mid` gives us 55. Looking at the 5th index, now our element, 66, is greater than 55. Therefore, our `R` needs to move to `mid - 1` since we need to look for a smaller element. The `L` pointer points to the 4th index and `R` pointer also points to the 4th index. The new `mid` results in 4 and indeed, our target exists at the 4th index, so we can return `mid`.

![alt text](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/84ece94d-88ad-4e76-9361-fde39487d800/sharpen=1)

A better formula for calculating the `mid` value is `L + (R - L)\ /\ 2`. This formula guarentees that our `mid` doesn't exceed the maximum integer value but also making sure that it isn't negative. This article from [Google Research](https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html) provides an intuitive explanation.

### 2. Target does not exist in the array

Let's dig a little deeper into what happens if our `target` does not exist in the array. Let's take the same array, `arr = [1,2,3,4,5,6,7,8]` and the `target` 99.

Our left pointer would end up out of bounds.

![alt text](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/719bef09-3014-4649-f7a2-745eee643800/sharpen=1)

### Time Space Complexity

The work being done is very similar to that of the merge-sort algorithm where we are dividing the array in half until we reach an array of size 11. The time complexity for binary search will be $O(logn)$

### Sample Code

```python
arr = [1, 3, 3, 4, 5, 6, 7, 8]

# Python implementation of Binary Search
def binarySearch(arr, target):
    L, R = 0, len(arr) - 1

    while L <= R:
        mid = (L + R) // 2

        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else:
            return mid
    return -1

```

## Binary Search (Search Range)

### Concept

Imagine your friend gave you a range from 1 - 100 and asked you to guess the number they were thinking of. There are three outcomes. Either your guess is correct, too small or too big.

If your guess is too small, you will have to guess higher and if your guess it too big, you will have to guess lower. The difference here is that you do not know what number your friend is thinking of (aka the `target` value). All you have is feedback from them each time you guess, and you adjust your next guess accordingly.

The question here is, how would we go about setting our boundaries? Well, we can apply the standard binary search template that we learned in the previous chapter, except instead of checking if your `mid` equals `target`, you would ask your friend if your guess is correct.

Of course, your friend has a procedure for determining if your guess is too small or too big, which is simple. All they do is compare your guess to the number they are thinking of and let you know if you should guess higher or lower. The code for that method would look like the following:

```python
# Binary search on some range of values
def binarySearch(low, high):

    while low <= high:
        mid = (low + high) // 2

        if isCorrect(mid) > 0:
            high = mid - 1
        elif isCorrect(mid) < 0:
            low = mid + 1
        else:
            return mid
    return -1

```

As observed, based on the return value we get from the `isCorrect` function, we can choose to adjust our `high` and `low` accordingly, which, as stated in the previous chapter is just another way of representing the `L` and `R` pointers.

This technique can be confusing and can come across as very subtle because you have to figure out how to modify the typical implementation of binary search. For questions like these, a predefined method API is given, in this case, `isCorrect` and you are required to treat the function as a black-box and use it within your own binary search method.

### Time Space Complexity

The work being done is the same as the previous section, which is standard binary search procedure. Therefore, this procedure is also in $O(logn)$



### Past Year Paper Question:

**<u>2122 Sem1 Part2:</u>**

```python
def local_peak_function_version(a:int, b:int,survey:callable) -> int:   
    """Perform a binary search to find the index of a local peak in a list of integers
    Args:
        a (int): left bound of the search range
        b (int): right bound of the search range
        survey (callable): a callable function that generates a list of integers
    Returns:
        int: returns a value of local peak
    """
    
    #initialise the left and right pointers
    l , r = a , b-1
    
    # base case
    if a==b: 
        return a
    
    # leftmost
    if r > l and survey(a)>survey(a+1):
        return a
    #rightmost
    if b >= 1 and survey(b) > survey(b-1):
        return b
    # entering the binary search
    while l <= r:
        m = (l+r) // 2 
        
        if survey(m) >= survey(m-1) and survey(m) >= survey(m+1):
            return m
        elif survey(m-1) >= survey(m):
            r = m-1
        else:
            l = m+1
                
    return None
```







## Insertion Sort

Insertion sort is one sorting algorithm used to sort data in different data structures. It is one of the simplest sorting algorithms that works best when the data size is small (we will discuss why this is the case soon).

------

### Concept

Say that we have an array of size 55, populated with values: `[2,3,4,1,6]`. Our goal is to sort the array so we end up with `[1,2,3,4,6]`. Insertion sort says to break the arrays into sub-arrays and sort them individually, which results in a sorted array. If we had an array of size 11, that would already be sorted because there is no other element to compare it to. As such, we assume that the first element is sorted because we treat it as its own subarray.

The next subarray will be of size 22, which is `[2,3]`. To perform the sort, the two elements will need to be compared. For an array of size 22, this is trivial. However, when we get to the full array of size 55, there is no way to keep track of where each element is without using pointers. So, let's take two pointers, `i` and `j`.

- `j` will always be behind `i` such that it will never cross `i`.
- The `i` pointer points of the index `n-1` where `n` is the size of the current sub-array.
- The `j` pointer starts off with being one index behind `i` and as long as `j` does not go out of bounds, that is, it is not at a negative index, and the `j+1` element is smaller than the `jth` element, we keep decrementing `j`. This will ensure that we have sorted all the elements before the `ith` index before moving to the next sub-array (iteration). This is demonstrated in the pseudocode below.

```python
# Python implementation of Insertion Sort
def insertionSort(arr):
	# Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them 
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j -= 1
    return arr

```

![alt text](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/f6edc4d8-ebbe-4276-a4d6-b7272268dd00/sharpen=1)

### Stability

Stability in a sorting algorithm refers to the relative order of the elements after the sorting is done. Take `[7,3,7]` for example. There are two 7s, one at the `0th` index and the other at the `2nd` index. We know that the relative order of these two 7s will stay the same since 3 will swap with the 7 at the `0th` index and then the while loop will never be implemented.

This is called a **stable** sorting algorithm. Insertion sort is stable, meaning that it is guarenteed that the relative order will remain the same. In an unstable sorting algorithm, this is not guarenteed and we shall see why in a few chapters.



### Time Space Complexity

For performing insertion sort on any data set of size $n$, in the best case, the array is already sorted which would cost .$O(n)$ This is because we will still have to go through every element in the array but our while loop would never execute. Can you think of the worst case scenario? In the worst case, all of the elements are sorted in reverse order, which means the while loop will execute $n$ times inside the for loop. This leads to an $O(n^2)$ time complexity.

#### A Deeper Dive - why $O(n^2)$

In the worst case, insertion sort performs $n^2$ operations, where $n$ is the size of the array. In the first for loop iteration, we sort the first two elements, then 3, 4, and finally 5. Well, if all of elements are in a reverse order, not only do we have to go through the entire array - the for loop, but also perform swap at every single step, which in total will be $n$. So in total, we can conclude that this is $n^2$. For sure, there is a very neat mathematical proof, but for the purpose of this course, this explanation is enough.



## Merge Sort

The concept behind merge sort is very simple. Keep splitting the array into halves until the subarrays hit a size of one, sort them, and merge the sorted arrays, which will result in an ultimate sorted array. You might have figured out that this sounds exactly like the fibonacci sequence using recursion, and you would be right! We can, and will be using recursion to perform this. More specifically, two branch recursion.

Let's take an array of size 55 as an example, `[3,2,4,1,6]`. Our job is to make sure that we sort this in an increasing, or non-decreasing order if we had duplicates. We will be splitting the array like the following.

![alt text](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/55728d04-816e-4176-985c-e82da4112b00/sharpen=1)

As observed, we have two branches. Let's work on sorting and merging the left branch first. The work required here is that we will have to hit the base case first, after which we can begin sorting and merging the arrays together, achieving `[2,3,4]` as a result. Once our recursion reaches the base case, we have two subarrays, `[3]` and `[2]`. We need a way to compare these two elements to know where to put them in their original subarray, which is `[3,2]`. For this, copies of both the subarrays is created and using two-pointers, values are compared and put in the original subarray in the sorted order. This can be seen in the pseudocode below.

```python
def mergeSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    # The middle index of the array
    m = (s + e) // 2

    # Sort the left half
    mergeSort(arr, s, m)

    # Sort the right half
    mergeSort(arr, m + 1, e)

    # Merge sorted halfs
    merge(arr, s, m, e)
    
    return arr
```

### Visualization and Pseudocode

#### The `mergeSort()` recursive call

As we learned with two branch recursion, we solve both the branches and 'piece' back together the solutions to the subproblems to arrive at the ultimate solution. Once we have the subarray `[3,2]` sorted to `[2,3]` - this is the `mergeSort(arr, s, m)` part. Now, we can move on to sorting the `[4]`, which corresponds to the `mergeSort(arr, m + 1, e)`. It is important to note the sequence in which the calls are executed. The `merge()` call will not be executed until both the recursive `mergeSort()` calls have returned for the current subarray. The first visual below shows sorting and merging the left half. The second visual shows sorting and merging the second half to get the ultimate sorted array.

![alt text](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/23d6fbdf-2fe5-4ff6-2c55-473b789a9600/sharpen=1)

![alt text](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/d497f50f-b72f-4038-06e3-fbbf60ac1000/sharpen=1)

#### The `merge()` function and three pointers

As observed in the visual above, we have three pointers, `k`, `j` and `i`.

- `k` keeps track of where the next element in `arr` needs to be placed.
- `i` points to the element in the `leftSubarray` that is currently being compared to the `j` element in the `rightSubarray`.
- One of `i` or `j` will increment depending on which element in smaller.
- `k` will increment regardless because `arr` will have an element placed inside of it regardless of which one of `i` or `j` increments.

This is clear in the visual above and demonstrated in the `merge()` function pseudocode below.

```python
# Merge in-place
def merge(arr, s, m, e):
    # Copy the sorted left & right halfs to temp arrays
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    i = 0 # index for L
    j = 0 # index for R
    k = s # index for arr

    # Merge the two sorted halfs into the original array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # One of the halfs will have elements remaining
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

```

### Time Complexity

Merge Sort runs in $O(logn)$. How so? Let's do some analysis. Recall from the fibonacci example when we kept splitting each sub-problem into two other sub-problems. We have a similar case here because our recursive tree is a tree with branching-factor of 2, except we are going the opposite direction. If  $n$is the length of our array at any given level, our subarrays in the next level have a length $n/2$

From our example above, we go from $n=4$ to $n=2$ to $n=1$ which is the base case. The question here is how many times can we divide $n$  by 22 until we hit the base case i.e. This would look like $n/2^x$ where $x$ is the number of times we need to divide $n$ by two until we get to one. Indeed,

$n/2^x = 1$

> Isolate $n$ by multiplying both sides by $2^x$

$n = 2^x$

> To solve for $x$, take $log$ of both sides

$logn = log2^x$

> According to $log$ rules, we can simplify this to:

$logn = 2logx$

> $log 2$ is basically asking $2$ to the power of what is equal to $2$, which is just $1$

$logn = x$

> The ultimate answer

$x = logn$

Having solved for $x$, our resulting answer is  $logn$which is the complexity for the `mergeSort` recursive call. We are not done yet, however.

Let's analyze the `merge` subroutine. The merge subroutine will take $n$ steps because at any level of the tree, we have  $n$elements to compare and sort, where $n$ is the length of the original array.

This results in a $O(n log n)$time complexity. The visual below gives more detail on how we arrived to our result. 

![alt text](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/600da4fb-21e7-4559-af19-afb78ec85100/sharpen=1)

### Stability

Merge Sort proves to be a **stable** algorithm because if we have a pair of duplicates, say, 7, the 7 in the left subarray will always end up in the merged array first followed by the 7 in the right subarray. This is because when we compare the `ith` element in the left subarray to the `jth` element in the right subarray for equality, we pick the one in the left subarray, maintaining the relative order. Recall the following pseudocode from the `merge()` subroutine.

```python
if leftSubarray[i] <= rightSubarray[j]:
    arr[k] = leftSubarray[i]
    i += 1

```







## Quick Sort

The idea behind quicksort is to pick an index, which is called the `pivot`, and partition the array such that every value to the left is less than or equal to the `pivot` and every value to the right is greater than the pivot.

### Picking a pivot value

Generally, there are several tested and tried options when it comes to picking a pivot:

- Pick the first index
- Pick the last index
- Pick the median (pick the first, last and the middle value and find their median and perform the split at the median)
- Pick a random pivot

You may be asking which pivot to pick? This is dependent on the data itself, both the size and the initial order. For coding interviews we can keep things simple, so in this chapter we will use the last index as our pivot.

### Implementation

We will pick a `pivot` if we haven't already hit the base case which is array of size `1` and pick a `left` pointer, which will point to the left-most element of the current subarray to begin with. Then, we will iterate through our array and if we find an element smaller than our `pivot` element, we will swap the current element with the element at our `left` pointer and increment the `left` pointer.

Once this condition terminates, we will bring the `left` element to the end of the array and bring the pivot element to the `left` position. This makes sense because once we have exhausted all the elements that are smaller than the `pivot` element, and put them to the left of the pivot, `left` will now be at the first element that is greater than the pivot. And, every element after it will also be greater than the pivot. This is why we move `left` element to the end and then bring the pivot element to the `left`.

This results in all the elements less than or equal to the `pivot` to be on the left and the rest on the right.

> There is also a variation of Quicksort called randomized Quicksort, where the pivot is picked randomly, or the array is shuffled if you like, and this reduces the chance of hitting the worst case. This results in $O(n log n)$ in the worst case instead of the typical implementation where it is $O(n^2)$. This [Stackoverflow](https://stackoverflow.com/questions/41513856/can-someone-clarify-the-difference-between-quicksort-and-randomized-quicksort#:~:text=The advantage of randomized quicksort,O(n log n).) post provides an interesting explanation behind it all.

Let's take the array `[6,2,4,1,3]` to sort.

### Performing a partition

![alt text](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/4807fbac-d636-4b43-654d-345988be0500/sharpen=1)

As seen above, in the resulting array, we will have sorted the array such that all elements to the left are smaller than the `pivot` with the rest being on the right.

> We are not going to visualize all of the steps but this process will be run recursively until we hit the base-case. It is important to notice that we are not allocating any new memory for these partitions. We are just moving around pointers to work on a smaller part of the original array each time until we end up with a sorted array.

The pseudocode for this looks like the following.

```python
# Implementation of QuickSort
def quickSort(arr, s, e):
    if e - s + 1 <= 1:
        return

    pivot = arr[e]
    left = s # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot
    
    # Quick sort left side
    quickSort(arr, s, left - 1)

    # Quick sort right side
    quickSort(arr, left + 1, e)

    return arr

```

#### Time Complexity

The analysis of quicksort is similar to merge sort. It also turns out to be $O(n log n)$ except only in the best case. The best case is that we pick a `pivot` such that we can always perform the partition in the middle. If the array is perfectly partitioned in the middle every single time and the pivot is the median, it is possible to keep getting $O(n log n)$ as the ultimate result.

Picking a pivot where the `pivot` element is the smallest or the largest element will result in the worst case performance of $O(n^2)$. This is because in the worst case, picking the highest or the lowest element in the list would result in the worst pivot and picking the worst pivot each time would mean you have $n$ groups to iterate through, hence the $O(n^2) complexity.

------

#### Stability

Quicksort is not a stable algorithm because it exchanges non-adjacent elements.

Take the array `[7,3,7,4,5]` where we have two 7s, one at the 0th index and one at the 2nd index. In this case, if our pivot is the 4th and the last index, we will end up with `[3,4,7,7,5]` where the 7 from the 0th index is now at 3rd index, which means that the relative order of the 7's has been reversed.







## Bucket Sort

### Concept

Imagine we have an array of size 6 and it contains values of an inclusive range of 0 - 2. The idea behind bucket sort is to create a "bucket" for each one of the numbers and map them to their respective buckets.

There will be a bucket for 0, 1 and 2. This bucket, which is just a position in a specified array will contain the frequencies of each one of the values within the range. For the sake of this example, we only have three values and accordingly we will have three buckets.

> The term bucket will really just translate into a position in an array where we will map these frequencies.

Once each one of the buckets is filled with the frequency of each one of the values, we will overwrite all the values in the original array such that they end up in the sorted order. This makes more sense looking at the pseudocode below:

```python
def bucketSort(arr):
    # Assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1
    
    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr

```

- The `i` pointer will keep track of the next insertion position for our original array, `arr`.
- The `n` pointer keeps track of the current position of the `counts` array.
- The `j` pointer keeps track of the number of times that `counts[n]` has appeared.

So, knowing that, we have our `counts` array which is `[2,1,3]`. And, our original input array is `[2,1,2,0,0,2]`.

At the first iteration, $n = 0$, which corresponds to 2 in `counts`. Our inner loop will run two times, overwriting `arr[0]` and `arr[1]` to be `0`. This makes perfect sense because we had two zeros and putting them in `arr` in an adjacent manner will result in them being sorted. This process will continue for each number and the ultimate state of `arr` will be `[0,0,1,2,2,2]` which is the ultimate goal.



![alt text](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/1521e7e2-4f63-4326-38cd-f32bcd9d3400/sharpen=1)

#### Time Complexity

You may be looking at the nested for loop and immediately going, that is $O(n^2)$. That is not quite right. Let's do some analysis. We know that for the first for loop, we are performing $n$ steps since we are going through all the elements and counting frequency.

The first for loop will run $n$ times where $n$ is the length of the `counts` array. However, the inner loop will only run until `counts[n]`, which is a different everytime. The first time it will be 22, then 11 and then 33. Therefore, our algorithm belongs belongs to $O(n)$

> It should be noted that nested for loops don't always mean a time complexity of $O(n^2)$ As we saw saw above, it is important to analyze how many times the inner for loop executes on each outer for loop iteration. More information on this can be found in the lessons section for Big-O Notation.

------

#### Stability

Since we are overwriting the original array, there is no way to preserve the relative order of the values. There is no swapping that takes place either. Hence, it will stay unstable.



## Summary

| Algorithm      | Big-O Time Complexity | Note                                                         |
| -------------- | --------------------- | ------------------------------------------------------------ |
| Insertion Sort | $O(n^2)$              | If fully, or nearly sorted, $O(n)$                           |
| Merge Sort     | $O(n log n)$          |                                                              |
| Quick Sort     | $O(n log n)$          | Picking the largest or the smallest element as the pivot e.g. reverse sorted - $O(n^2)$ |
| Bucket Sort    | $O(n)$                | Assuming you have a value within a specified range           |





## Graphs

(Not that important but may be helpful for understanding the application of Matrix DFS and BFS later on)

### Graph Terminology

In graphs, nodes are referred to as **vertices** and the pointers connecting these nodes are referred to as **edges**. There are no restrictions in graphs when it comes to where the nodes are placed, and how the edges connect those nodes together.

It is also possible that the nodes are not connected by any edges and this would still be considered a graph - a null graph.

The number of edges, $E$, given the number of vertices $V$ will always be less than or equal to $V^2$. $E<=V^2$ This is because each node can at most point to itself, and every other node in the graph. If we have a node `A`, `B` and `C`, `A` can point to itself, `B` and `C`. The same goes for `B` and `C`, so the rule checks out.

If the pointers connecting the edges together have a direction, we call this a **directed graph.** If there are edges but no direction, this is referred to as an **undirected graph**. For example, trees and linked lists are directed graphs because we had pointers like `prev`, `next` and `left_child`, `right_child`.

![hello](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/74daad67-5e27-476e-af6b-291ab5b80400/sharpen=1)

### Formats of Graphs in Interviews

A graph can be represented in different ways. It is an abstract concept that is made concrete using different data structures. Most commonly, graphs are represented using the following:

1. Matrix
2. Adjacency Matrix
3. Adjacency List

### Matrix

A matrix is a two-dimensional array with rows and columns, and a graph can be represented using a matrix. In the code below, each array, separated by commas, represents each row. Here we have four rows and four columns. Everything is indexed by 00 and the idea is that we should be able to access an arbitrary row, column, or a specific element given a specified row or column. Accessing the second row can simply be done by `grid[1]` and accessing the second column may be done by `grid[0][1]`.

```python
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

```

How can this be used to represent a graph? As we mentioned, graphs are abstract and can be defined in many ways. Let's say that all of the 0's in our grid are vertices. To traverse a graph, we are allowed to move up, down, left and right. If we are to connect the 0s together, using our edges, we would end up getting a bunch of connected zeroes, which are connected components, and that denotes a graph. We shall discuss matrix traversal in the next chapter.



![hello](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/f3c04f37-7656-4836-f263-3ae19258c100/sharpen=1)

### Adjacency Matrix

This is the less common input format. Here, the index of the array represents a vertex itself. Let's take an example:

```python
adjMatrix = [[0, 0, 0, 0],
             [1, 1, 0, 0],
             [0, 0, 0, 1],
             [0, 1, 0, 0]]

```

Because the indices themselves represent a vertex, 00 denotes that an edge does not exist between a given `v1, v2`, and 11 denotes the opposite. `adjMatrix[1][2] == 0` means there is no edge between vertex `1` and `2`. Also, `adjMatrix[2][1] == 0` means there is no edge between vertex `2` and `1`. We can conclude the following from this:

```python
# an edge exists from v1 to v2
adjMatrix[v1][v2] = 1

# an edge exists from v2 to v1
adjMatrix[v2][v1] = 1

# No edge exists from v1 to v2
adjMatrix[v1][v2] = 0

# No edge exists from v2 to v1
adjMatrix[v2][v1] = 0

```

To actualize the above adjacency matrix, we can look at the following visual.

![hello](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/02f2aedd-88d5-461d-9fdd-0bffc2e81400/sharpen=1)

The issue with this is that it is a giant memory hog. Because it is a square matrix, the time complexity is $O(V^2)$, where $V$ is the number of vertices. This makes sense since the number of edges is also equal to the number of nodes.



### Adjacency List

These are typically the most common way of representing graphs. This is also a two dimensional array. The convenience here is that we can declare it using a class called `GraphNode` and it contains a list attribute called `neighbors`, using which we can access all of a given vertex's neighbor.

```python
# GraphNode used for adjacency list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

```

This ends up being more space efficient because we only care about nodes that are connected.

![hello](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/85b20b68-357a-4a6d-7c7a-e09256693200/sharpen=1)

## Matrix DFS

How do we go about applying DFS to graphs? This is best shown with an example.

Suppose we are given the following question to solve:

> Q: Count the unique paths from the top left to the bottom right. A single path may only move along 0's and can't visit the same cell more than once.

```python
matrix = [[0,0,0,0],
          [1,1,0,0],
          [0,0,0,1],
          [0,1,0,0]]

```

In this problem, it is all a matter of choices. You might think of this as similar to backtracking and you would be right. We have mentioned before that DFS is recursive in nature and and we will be using recursion for this. Firstly, we need to think of our base case(s). Well, we know that we can move in all four directions except diagonally. This means that if we go out of bounds, we can return zero.

We know that this will be a brute-force DFS with backtracking since at any point in our path, we might not have a valid way to reach the bottom right, in which case, we will have to backtrack.

For starters, let's establish about our base cases. Since we are trying to find the number of unique paths, we need to keep count of the valid paths from each vertex.

### The base cases

#### 1. A unique path does not exist

Since we are allowed to move in all four directions, it is possible that during our traversal, we end up going out of bounds. This means either our column, `c`, or our row, `r` becomes negative, or goes beyond the length of our matrix. It does not matter which of `r` and `c` goes out of bounds because we need a valid `c` **AND** a valid `r` to perform our search. We cannot perform a search on `matrix[-1][3]`.

If we have already visited a coordinate, or the current coordinate is 1, then a valid path does not exist through that coordinate.

So because a valid path does not exist in all of the aforementioned cases, we will return 0, which denotes absence of a unique path. We shall see this in our code soon.

#### 2. A unique path does exist

If we have not returned 00 from the first case, and we have reached the right-most column and the bottom-most row, it must be the case that we have found a valid path. Remember, our definition of a valid path is if a path exists from `matrix[0][0]` to `matrix[3][3]`. We can now return 11 and this will increment our count for the number of unique paths.



### Implementation

To ensure that we don't visit a coordinate more than once, we add it to a global HashSet, once visited.

Then, at any given coordinate, we can recursively perform our DFS on `r+1`, `r-1`, `c+1` and `c-1`. If our recursive call returns 11, our `count` will be incremented and if it returns 00, adding it to count will make no difference.

At each recursive call, we can remove all of the rows and columns that led us to an invalid path. This way, we can ensure to visit them again, but take a different direction and explore if a valid path exists from that direction.

In the code below, we have our aforementioned base cases set up. We then add the current row and column to our set. Our count is initialized with 00 because we need to keep track of all the possible unique paths we have to our destination at any given vertex. Once our recursive calls return, we can remove the visited vertices from our set. Again, this is because they can be part of another unique path, just from a different source. So, when we backtrack, we can visit them again.

```python
# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Count paths (backtracking)
def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    count = 0
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    visit.remove((r, c))
    return count

```

To visualize the above on our matrix, we can break down our algorithm into finding the initial unique path, and then backtracking to find another potential unique path.

### 1. Find the first unique path

![recursive-dfs](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/7717e227-5da3-4b91-fe73-b25065d78c00/sharpen=1) 

### 2. Backtrack to find another potential unique path

> The red dotted line represents another unique path which is reached from `matrix[0][3]`.

 ![recursive-dfs](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/c1fd94d4-7a68-4e8d-4f91-5a5f3ec92c00/sharpen=1)

Our function returns 22, denoting there exist 22 unique paths from `(0,0)` to `(3,3)`.

### Time Complexity

By now, we know that we only consider the worst case. In the worst case, we might need to visit every single row and column. At every coordinate, we can move in all four directions. Each one of the coordinates that are reached by moving in each those four directions will also be able to move up, down, left or right. We have four options from each position. If we are to create a decision tree out of this, each node will have at most four children. The tree has a branching factor of 44 and the height of the tree is the size of the matrix which is just $n*m$, where $n$ is the number of rows and $m$ is the number of columns.

Therefore, we get $4^{nm}$

> The space complexity will be the entire call stack since this is recursive. Therefore, it will be $O(n*m)$



### Leetcode Question 200. Number of Islands

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

```python
## Using DFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands




```

```python
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited=set()
        islands=0

         def bfs(r,c):
             q = deque()
             visited.add((r,c))
             q.append((r,c))
           
             while q:
                 row,col = q.popleft()
                 directions= [[1,0],[-1,0],[0,1],[0,-1]]
               
                 for dr,dc in directions:
                     r,c = row + dr, col + dc
                     if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r ,c) not in visited:
                       
                         q.append((r , c ))
                         visited.add((r, c ))

         for r in range(rows):
             for c in range(cols):
               
                 if grid[r][c] == "1" and (r,c) not in visited:
                     bfs(r,c)
                     islands +=1 

         return islands
```



### LeetCode Question 695. Max Area of Island

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return *the maximum **area** of an island in* `grid`. If there is no island, return `0`.



**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg" alt="img" style="zoom:50%;" />

```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

**Example 2:**

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area

```



### Past Year Paper Questions:

**<u>2223 Sem2 Part 3:</u>**

In the first example map0, there are two independent islands with perimeters 8 and 6 respectively. Hence, the maximum perimeter of all the islands on that map is 8. In this task, write a function max_island_perimeter(mp) which returns the maximum island perimeter of map mp. 

Note that two land squares belong to the same island if and only if they are connected horizontally or vertically, but NOT diagonally. For instance, map1 has three islands as shown on the right, and the lower right inverted U-shaped island gives the maximum island perimeter of 14. If there is no island/land in the map, return 0. 

```python
def max_island_perimeter(mp:list) -> int:
      row = len(mp)
      col = len(mp[0])
      perimeter = 0
      visited = set()
      
      def dfs(r,c):
            if r not in range(row) or c not in range(col) \
               or mp[r][c] == 0: return 1 # the perimeter depends on the number of neighboring 0s
            if (r,c) in visited: return 0
            if mp[r][c] == 1:
                  visited.add((r,c))
                  return dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1) # recursive
            return 0
      for r in range(row):
            for c in range(col):
                  if mp[r][c] == 1:
                        perimeter = max(perimeter, dfs(r,c))
         
      return perimeter
```

2122 Sem2 Part4:

```python
def build_graph(map_data: list):
    graph = {}
    for line in map_data:
        locations = line.split()
        if len(locations) >= 2:
            start, *rest = locations  # Get the first element as start and the rest as destinations
            if start not in graph:
                graph[start] = []
            graph[start].extend(rest)  # Add destinations to the graph
    return graph

def find_paths_dfs(graph:dict, current:str, goal:str, visited:set, path:list, paths:list)-> int:
    visited.add(current)
    path.append(current)

    if current == goal:
        paths.append(path.copy())
    else:
        for neighbor in graph.get(current, []):
            for neighbor in graph.get(current, []):
                if neighbor in path:
                    # Backtrack by removing the current node from the path
                    path.pop()
                else:
                    # Recursively explore the neighbor
                    find_paths_dfs(graph, neighbor, goal, visited, path, paths)



def strategic_count(mapfile:str, start_location:str='CountryA', goal_location:str='capitalB'):
    with open(mapfile, 'r') as file:
        map_data =  [line.strip() for line in file] # this will contain a list of all the lines in the file
    
    graph = build_graph(map_data)
    visited = set()
    paths, path = [], [] # how to get to the goal
    find_paths_dfs(graph, start_location, goal_location, visited, path, paths)
    
    
    if paths:
        return len(paths)
    else:
        return 0
    
   
paths contains the following:
[['CountryA', 'VillageA', 'BuildingD', 'capitalB'],
 ['CountryA', 'VillageA', 'TowerE', 'capitalB'],
 ['CountryA', 'IntersectionB', 'TowerE', 'capitalB'],
 ['CountryA', 'IntersectionB', 'BuildingD', 'capitalB']]
    
```





## Matrix BFS

The type of graph questions where BFS will shine is usually when the question asks us to find the **<u>shortest path.</u>**

> Q: Find the length of the shortest path from top left of the grid to the bottom right.

We can also use DFS to do this but it is more brute-force. BFS is more efficient since the first time a vertex is discovered during the traversal, the distance from our source would give us the shortest path. Let us see the set up of the code, given the following matrix.

```python
# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

```

### The initial set up

Similar to the previous chapter, we take the dimensions of our row and columns, which tells us where our bounds are. We will use a set to keep track of visited vertices. We will use a deque (deck) to keep track of all visited vertices at each level and determine what level we are at currently. We can initialize our deque to the first vertex, `(0, 0)` and mark it as visited. This is our starting point.



```python
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

```

### BFS on the graph

We are asked to find the length of the shortest path. After our initial set up, we can initialize a `length` variable to `0`. Then, just like BFS on trees, we can run a while loop for our queue and take a snapshot of the length of the queue. Here, when we pop from our queue, we get a `r` (row) and `c` (column). With trees, the next step was to visit the children of the popped node. Here, we visit the neighbors of the popped vertex. We will only have to do this if we have not already reached the bottom right, which is when `r == ROWS - 1` and `c == COLS - 1`.

In the best case, we might be able to move in all four directions without going out of bounds. For this, we can keep a 2-D array - `neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]`. Though not technically the neighbors, the array just represents the directions we can move in - right, left, up, down, respectively.

The code in the `if` statement is the same as what we had in DFS. If we are out of bounds, the coordinate is blocked or the vertex is already visited, we continue to the next iteration. Otherwise, we append all the neighbors to the queue and add them to the hashset to ensure we don't visit them again. Notice how we add to the hashset as soon as we append to the queue. This way, we will never have the same element occur twice in our queue, which helps in making it more efficient in time complexity, which we will discuss later. The next piece of code after the initial setup looks like this.

```python
length = 0
while queue:
    for i in range(len(queue)):
        r, c = queue.popleft()
        if r == ROWS - 1 and c == COLS - 1:
            return length

        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in neighbors:
            if (min(r + dr, c + dc) < 0 or
                r + dr == ROWS or c + dc == COLS or
                (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                continue
            queue.append((r + dr, c + dc))
            visit.add((r + dr, c + dc))
    length += 1

```

Tying it all together, we will end up with the following.

```python
# Shortest path from top left to bottom right
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or
                    r + dr == ROWS or c + dc == COLS or
                    (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1

```

We can visualize this algorithm applied to our matrix below. The numbers and circles in the same color represent the length of the path at that specific vertex.

![matrixbfs](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/8a6996dc-78e0-45ac-bd1e-b06afc6ade00/sharpen=1)

### Time Complexity

Since we are never visiting a coordinate twice, in the worst case, we end up visiting each coordinate at most once. If $n$ is the number of rows and $m$ is the number of columns, this gives us a time complexity of $O(n*M)$



### Leetcode Quesstion 1091. Shortest Path in Binary Matrix

Given an `n x n` binary matrix `grid`, return *the length of the shortest **clear path** in the matrix*. If there is no clear path, return `-1`.

A **clear path** in a binary matrix is a path from the **top-left** cell (i.e., `(0, 0)`) to the **bottom-right** cell (i.e., `(n - 1, n - 1)`) such that:

- All the visited cells of the path are `0`.
- All the adjacent cells of the path are **8-directionally** connected (i.e., they are different and they share an edge or a corner).

The **length of a clear path** is the number of visited cells of this path.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/02/18/example1_1.png)

```python
Input: grid = [[0,1],[1,0]]
Output: 2
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/02/18/example2_1.png)

```python
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
```

**Example 3:**

```python
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
```



````python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0, 0, 1)]) # r, c, length
        visit = set((0, 0))
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0],
                  [1, 1], [-1, -1], [1, -1], [-1, 1]]
        while q:
            r, c, length = q.popleft()
            if (min(r, c) < 0 or max(r, c) >= N or
                grid[r][c]):
                continue
            if r == N - 1 and c == N - 1:
                return length
            for dr, dc in direct:
                if (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
        return -1

````



### Leetcode Question 994. Rotting Oranges

You are given an `m x n` `grid` where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1`.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2:**

```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

**Example 3:**

```
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
```

 ```python
 class Solution:
     def orangesRotting(self, grid: List[List[int]]) -> int:
         q = collections.deque()
         fresh = 0
         time = 0
 
         for r in range(len(grid)):
             for c in range(len(grid[0])):
                 if grid[r][c] == 1:
                     fresh += 1
                 if grid[r][c] == 2:
                     q.append((r, c))
 
         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
         while fresh > 0 and q:
             length = len(q)
             for i in range(length):
                 r, c = q.popleft()
 
                 for dr, dc in directions:
                     row, col = r + dr, c + dc
                     # if in bounds and nonrotten, make rotten
                     # and add to q
                     if (
                         row in range(len(grid))
                         and col in range(len(grid[0]))
                         and grid[row][col] == 1
                     ):
                         grid[row][col] = 2
                         q.append((row, col))
                         fresh -= 1
             time += 1
         return time if fresh == 0 else -1
 
 ```

