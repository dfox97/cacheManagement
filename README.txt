In computers, memory is located in different parts of the computer; memory on disk is far away from the CPU and takes a long time to access, but offers a large amount of storage; cache memory is close to the CPU so is faster to access, but does not offer a lot of storage space.

Pages from memory are requested. The idea is that when a page from memory is requested, the cache is searched and if it is present in the cache, this is called a “hit”. If it is not present, then this is called a “miss”, and the page must be retrieved from disk (main) memory and placed in the cache. The cache will only hold 8 pages (an int represents a page). This means that if the cache is full, you must decide which page to evict, according to the management techniques explained below.


First In First Out (FIFO)
When a request comes in to a FIFO cache, the cache is searched for the requested page. If it is present, then this is a “hit”. If it is not present, then this is a “miss”.

The FIFO cache management technique will place any “miss” into the cache up until the cache is full (your cache should only hold 8 pages).

When the cache is full, the page that has the longest time since it was added is evicted (removed) from the cache.

Least Frequently Used (LFU)
When a request comes in to an LFU cache, the cache is searched for the requested page. If it is present, then this is a “hit”. If it is not present, then this is a “miss”.

The LFU cache management technique will place any “miss” into the cache up until the cache is full (your cache should only hold 8 pages).

Each “hit” against a cached page is logged, and used in deciding which page to evict.

When the cache is full, the page that has the fewest “hits” is evicted (removed) from the cache. In case of two pages having the same amount of hits, the lowest numbered page should be evicted.

Program Structure
Your program must have the following functions and variables:

A gobal scope list called “cache”

A global scope list called “requests”

A method fifo() which will run the FIFO cache management on cache and requests

A method lfu() which will run the LFU cache management on cache and requests

Clarification: After each method has been used for the given requests, the cache should be cleared.


The main body of your program should ask the user for an int repeatedly until 0 is entered. These ints should be placed in to requests.

The user should then be presented with options: press 1 for fifo, or 2 for lfu. Q should quit the program.

The appropriate method (fifo() or lfu()) should then be called. The method should iterate over requests, and “requesting” each “page” (represented simply as an int) from the cache.

If the “page” is present, then this is a “hit” and the word “hit” should be printed to screen.

If the “page” is not present, then this is a “miss” and the word “miss” should be printed to screen.

In the event of a miss, the correct “page” should be removed from cache and the newly reqested “page” should be correctly inserted into cache. In reality, this means that you will remove an int from cache and insert a new int into cache.




At the end of processing all requests, you should then print the final state of cache and exit back to the main menu.


