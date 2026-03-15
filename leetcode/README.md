# LeetCode — How to Start & What to Solve

> Don't grind randomly. Follow patterns. Understand, don't memorize.

---

## When to Start

```
Phase 1 (Python Roadmap):
  Week 1–4:  ❌ SKIP — focus on Python
  Week 5–6:  ✅ START — 1 easy/day (alongside DSA lessons)
  Week 7–10: ✅ CONTINUE — 1 easy/day (keep DSA sharp)

Phase 2 (ML Roadmap):
  Month 0–3: ❌ SKIP — focus on math & ML
  Month 4–6: ✅ RESUME — 3–4 easy/medium per week
  Month 7–9: ✅ CONTINUE — 3–4 medium per week
  Month 10+: ✅ INTERVIEW MODE — timed medium problems
```

---

## The 5-Step Method (For Every Problem)

```
1. READ the problem carefully (5 min)
   - Identify input/output
   - Note constraints (array size, value range)
   - Look at examples

2. THINK before coding (5 min)
   - What pattern does this look like?
   - What data structure fits?
   - What's the brute force? Can you do better?

3. CODE your solution (15 min)
   - Write clean, readable code
   - Use meaningful variable names
   - Add comments for tricky parts

4. STUCK > 15 min? → Read the solution
   - Don't waste hours — read, understand, then...
   - Close it and REDO from scratch without looking
   - This is where learning happens

5. NEXT DAY: Redo yesterday's problem from memory
   - If you can't → you didn't learn it
   - If you can → move on
```

---

## Pattern Order (Solve In This Sequence)

### Pattern 1: Arrays & Hashing (Start Here)
| # | Problem | Difficulty | Key Concept |
|---|---------|-----------|-------------|
| 1 | Two Sum | Easy | Hash map lookup |
| 2 | Contains Duplicate | Easy | Set |
| 3 | Valid Anagram | Easy | Frequency counting |
| 4 | Group Anagrams | Medium | Hash map + sorting |
| 5 | Top K Frequent Elements | Medium | Hash map + heap |
| 6 | Product of Array Except Self | Medium | Prefix/suffix |

### Pattern 2: Two Pointers
| # | Problem | Difficulty | Key Concept |
|---|---------|-----------|-------------|
| 7 | Valid Palindrome | Easy | Two pointers inward |
| 8 | Merge Sorted Array | Easy | Two pointers from end |
| 9 | Two Sum II (Sorted) | Medium | Two pointers |
| 10 | 3Sum | Medium | Sort + two pointers |
| 11 | Container With Most Water | Medium | Greedy two pointers |

### Pattern 3: Sliding Window
| # | Problem | Difficulty | Key Concept |
|---|---------|-----------|-------------|
| 12 | Best Time to Buy and Sell Stock | Easy | Track min |
| 13 | Longest Substring Without Repeating | Medium | Sliding window + set |
| 14 | Longest Repeating Character Replacement | Medium | Sliding window + count |

### Pattern 4: Stack
| # | Problem | Difficulty | Key Concept |
|---|---------|-----------|-------------|
| 15 | Valid Parentheses | Easy | Stack matching |
| 16 | Min Stack | Medium | Two stacks |
| 17 | Evaluate Reverse Polish Notation | Medium | Stack |
| 18 | Daily Temperatures | Medium | Monotonic stack |

### Pattern 5: Binary Search
| # | Problem | Difficulty | Key Concept |
|---|---------|-----------|-------------|
| 19 | Binary Search | Easy | Classic |
| 20 | Search Insert Position | Easy | Modified binary search |
| 21 | First Bad Version | Easy | Binary search on condition |
| 22 | Search in Rotated Sorted Array | Medium | Modified binary search |

### Pattern 6: Linked List
| # | Problem | Difficulty | Key Concept |
|---|---------|-----------|-------------|
| 23 | Reverse Linked List | Easy | Pointer manipulation |
| 24 | Merge Two Sorted Lists | Easy | Dummy node |
| 25 | Linked List Cycle | Easy | Fast/slow pointers |
| 26 | Remove Nth Node From End | Medium | Two pointers with gap |

### Pattern 7: Trees
| # | Problem | Difficulty | Key Concept |
|---|---------|-----------|-------------|
| 27 | Maximum Depth of Binary Tree | Easy | DFS recursion |
| 28 | Invert Binary Tree | Easy | DFS |
| 29 | Same Tree | Easy | DFS comparison |
| 30 | Subtree of Another Tree | Easy | DFS + same tree |
| 31 | Binary Tree Level Order Traversal | Medium | BFS with queue |
| 32 | Validate BST | Medium | DFS with bounds |

### Pattern 8: Graphs (BFS/DFS)
| # | Problem | Difficulty | Key Concept |
|---|---------|-----------|-------------|
| 33 | Number of Islands | Medium | DFS/BFS on grid |
| 34 | Clone Graph | Medium | BFS + hash map |
| 35 | Course Schedule | Medium | Topological sort |

### Pattern 9: Dynamic Programming (Later — Month 7+)
| # | Problem | Difficulty | Key Concept |
|---|---------|-----------|-------------|
| 36 | Climbing Stairs | Easy | Basic DP |
| 37 | House Robber | Medium | 1D DP |
| 38 | Coin Change | Medium | Classic DP |
| 39 | Longest Increasing Subsequence | Medium | DP / binary search |
| 40 | Unique Paths | Medium | 2D DP |

---

## Progress Tracker

| # | Problem | Pattern | Solved | Date | Notes |
|---|---------|---------|--------|------|-------|
| 1 | Two Sum | Array/Hash | ☐ | | |
| 2 | Contains Duplicate | Array/Hash | ☐ | | |
| 3 | Valid Anagram | Array/Hash | ☐ | | |
| 4 | Group Anagrams | Array/Hash | ☐ | | |
| 5 | Top K Frequent | Array/Hash | ☐ | | |
| 6 | Product Except Self | Array/Hash | ☐ | | |
| 7 | Valid Palindrome | Two Pointers | ☐ | | |
| 8 | Merge Sorted Array | Two Pointers | ☐ | | |
| 9 | Two Sum II | Two Pointers | ☐ | | |
| 10 | 3Sum | Two Pointers | ☐ | | |
| 11 | Container Most Water | Two Pointers | ☐ | | |
| 12 | Buy Sell Stock | Sliding Window | ☐ | | |
| 13 | Longest Substring | Sliding Window | ☐ | | |
| 14 | Longest Repeating | Sliding Window | ☐ | | |
| 15 | Valid Parentheses | Stack | ☐ | | |
| 16 | Min Stack | Stack | ☐ | | |
| 17 | Reverse Polish | Stack | ☐ | | |
| 18 | Daily Temperatures | Stack | ☐ | | |
| 19 | Binary Search | Binary Search | ☐ | | |
| 20 | Search Insert | Binary Search | ☐ | | |
| 21 | First Bad Version | Binary Search | ☐ | | |
| 22 | Rotated Array | Binary Search | ☐ | | |
| 23 | Reverse Linked List | Linked List | ☐ | | |
| 24 | Merge Two Lists | Linked List | ☐ | | |
| 25 | Linked List Cycle | Linked List | ☐ | | |
| 26 | Remove Nth Node | Linked List | ☐ | | |
| 27 | Max Depth Tree | Trees | ☐ | | |
| 28 | Invert Tree | Trees | ☐ | | |
| 29 | Same Tree | Trees | ☐ | | |
| 30 | Subtree Check | Trees | ☐ | | |
| 31 | Level Order | Trees | ☐ | | |
| 32 | Validate BST | Trees | ☐ | | |
| 33 | Number of Islands | Graphs | ☐ | | |
| 34 | Clone Graph | Graphs | ☐ | | |
| 35 | Course Schedule | Graphs | ☐ | | |
| 36 | Climbing Stairs | DP | ☐ | | |
| 37 | House Robber | DP | ☐ | | |
| 38 | Coin Change | DP | ☐ | | |
| 39 | Longest Increasing | DP | ☐ | | |
| 40 | Unique Paths | DP | ☐ | | |

**Solved: 0 / 40 | Target: 50+ by Month 11**

---

## Common Mistakes

1. ❌ **Grinding randomly** — Follow the pattern order above
2. ❌ **Spending 2 hours on one problem** — 15 min stuck = read solution, redo
3. ❌ **Memorizing solutions** — Understand the PATTERN, not the code
4. ❌ **Skipping the redo** — Redoing from memory is where learning happens
5. ❌ **Only doing easy** — Move to medium once you're comfortable with a pattern
6. ❌ **Not explaining out loud** — Talk through your approach like an interview

## Best Resources

- **NeetCode 150** — neetcode.io (curated, grouped by pattern, video explanations)
- **Blind 75** — the classic interview list
- **LeetCode Explore** — guided learning paths
- **NeetCode YouTube** — best video explanations for each problem

---

## Stats

```
Current Streak: ___ days
Total Solved:   ___ / 50 target
Easy:           ___
Medium:         ___
Favorite Pattern: _______________
Weakest Pattern:  _______________
```

---

*Start date: _________ | Target: 50+ problems by interview time*
