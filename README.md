# Longest increasing sub-sequence

The longest increasing sub-sequence is a more general sub-set of a sequence than the longest increasing substring that you are already familiar with.

We can think of sub-sequences of a sequence `x` as an increasing list of indices `is` where `is` is increasing and so is `[x[i] for i in is]`. A sub-string is one where the indices in `is` are consequtive, i.e. `is = [k, k+1, k+2, ...]` for some `k`. A general sub-sequence doesn't have to obey that rule.

A very simple (and *very* inefficient) way to find the longest common sub-sequence is to generate every possible sub-sequence, i.e. every possible list `is` of increasing indices into `x`, check if `[x[i] for i in is]` is increasing, and then pick the longest of these. (We don't care how you resolve conflicts this time.)

Can you work out how to do this? Then go to `src/liseq.py` and try it out.

If you made it this far, you are done with all the other exercises for the week, so I'll give you one extra task. Try to write tests for your function. I have left a function for it in `src/test_liseq.py`.
