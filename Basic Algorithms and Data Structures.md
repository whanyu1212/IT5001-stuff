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

On the next iteration, calculating `mid` gives us 55. Looking at the 5th index, now our element, 66, is greater than 55. Therefore, our `R` needs to move to `mid - 1` since we need to look for a smaller element. The `L` pointer points to the 4th index and `R` pointer also points to the 4th index. The new `mid` results in 44 and indeed, our target exists at the 4th index, so we can return `mid`.

![image-20230928193308501](/Users/hanyuwu/Library/Application Support/typora-user-images/image-20230928193308501.png)

A better formula for calculating the `mid` value is `L + (R - L)\ /\ 2`. This formula guarentees that our `mid` doesn't exceed the maximum integer value but also making sure that it isn't negative. This article from [Google Research](https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html) provides an intuitive explanation.

### 2. Target does not exist in the array

Let's dig a little deeper into what happens if our `target` does not exist in the array. Let's take the same array, `arr = [1,2,3,4,5,6,7,8]` and the `target` 99.

Our left pointer would end up out of bounds.

![image-20230928193541295](/Users/hanyuwu/Library/Application Support/typora-user-images/image-20230928193541295.png)

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

![image-20230928194902193](/Users/hanyuwu/Library/Application Support/typora-user-images/image-20230928194902193.png)

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

<img src="/Users/hanyuwu/Library/Application Support/typora-user-images/image-20230928200812074.png" alt="image-20230928200812074" style="zoom:50%;" />

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

![image-20230928201135629](/Users/hanyuwu/Library/Application Support/typora-user-images/image-20230928201135629.png)

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

Let's analyze the `merge` subroutine. The merge subroutine will take $n$ steps because at any level of the tree, we have  $n$elements to compare and sort, where �*n* is the length of the original array.

This results in a $O(n log n)$time complexity. The visual below gives more detail on how we arrived to our result. 

![image-20230928203845793](/Users/hanyuwu/Library/Application Support/typora-user-images/image-20230928203845793.png)

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

![image-20230928204509482](/Users/hanyuwu/Library/Application Support/typora-user-images/image-20230928204509482.png)

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



![image-20230928205129870](/Users/hanyuwu/Library/Application Support/typora-user-images/image-20230928205129870.png)

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

