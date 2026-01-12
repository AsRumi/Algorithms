# Boyer-Moore Algorithm

This is a pattern matching algorithm. Given a pattern P, it scans text T to find exact matches.

In contrast to a naive implementation where each character is tested for a match, this algorithm skips alignments that are proven to be fruitless.

Boyer-Moore compares the target string starting from right to left while moving through the text from left to right, using information from comparison to avoid making needless comparisons.

### Conditions to skip alignments (Bad Character Rule):

- Until you get a match
- Target moves past the mismatched character

### Good suffix rule

- When you shift alignments, you need to keep the already matched substring/subarray intact. This means, if there exists a substring in target to the left of current matched substring which also matches with text, move target to the right till that substring is aligned with text. If no such substring exists, move the target according to the bad character rule.

In practice, the algorithm uses **maximum of shifts** given by both the rules to save time and effort.
