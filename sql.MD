**Explain how indexing can degrade performance.**

1.Indexing improves **read performance**, but it can degrade performance in certain situations. Here’s how and why:

1.Slower insert,delete,update operations
2.need to update/delete the entries of the tables and inserting will create new entry.
3.due to this will get slower write-heavy systems
4.If more indexes will burden for storage consumption due to this it will affect the efficiency
4.Slower bulk operations like bulk inserts,batch updates ,data imports
5.can be much slower with many indexes because each row triggers index updates.

💡 Best practice: Drop non-essential indexes before bulk loads and recreate them afterward.
    6.Too many indexes can confuse the query optimizer.
 **Ineffective or Low-Selectivity Indexes**

 Indexing columns with very few distinct values (like gender or status) may:

 Provide little performance benefit

 Still incur maintenance cost