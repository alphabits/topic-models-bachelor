Project outline
===============

The main theme of the project is Topic Models. The primary subject is the Latent Dirichlet Allocation (LDA) model and the hierarchical LDA model (hLDA) and the project is oriented towards both theory and implementation. 

In the theory part of the project a general understanding of graphical models and thorough knowledge about the LDA and hLDA models should be obtained. 

For the implementation part of the project the goal is first to learn and implement various inference algorithms in python. The implementations are not expected to be better in any way, than existing implementation and the aim is only to learn the general concepts of the various inference algorithms. Since the implementations in python are only expected to run acceptably on small datasets (~1000 documents with ~1000 words), the final part of the project will focus on inference in LDA using MapReduce. Existing implementations will be used and if time permits the problem of inference in hLDA models with MapReduce will be tackled.

List of tasks
-------------

Week 1 and 2
............

  * :doc:`Read about general theory of graphical models </week-1>`

  * Read about theory of LDA and hLDA

Week 2, 3 and 4
...............

  * Read about main inference algorithms for graphical models

  * Read about inference algorithms for LDA and hLDA

  * Create python implementation of one or more inference algorithms

Week 4 and 5
............

  * Use python implementations to calculate similar courses based on course list data scraped from the online dtu course list. 

  * Compare the computational performance of our implementation with the performance of the Gensim implementation. 

  * Assess the quality of the found course similarities using the known relations between courses.


Week 6 and 7
............

  * Read about MapReduce

  * Read about Hadoop, Mahout and Clojure

Week 7, 8 and 9
...............

  * Use Mahout's implementation of LDA to find topics in a Wikipedia data set

  * Assess the quality of the topics found using data about the categories already in the Wikipedia dataset

Week 10 and 11
..............

  * Use existing implementations of inference algorithms for hLDA to find a topic hierarchy in a subset of the Wikipedia data set

Week 12, 13 and 14
..................

  * Create a MapReduce implementation of hLDA inference algorithm and compare computational performance with non-MapReduce implementations
